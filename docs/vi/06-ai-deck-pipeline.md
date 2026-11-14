> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# 06 — Pipeline tạo deck bằng AI

Tự động hóa việc tạo thẻ đáng làm vì đúng một lý do: viết thẻ tốt thì chậm, và phần lớn cái chậm đó là máy móc. Phán đoán thì không máy móc, nên pipeline phải giữ con người trong vòng lặp ở bước phán đoán và loại con người khỏi mọi bước còn lại.

Điều gì hỏng khi không có pipeline: bạn xin một agent 100 thẻ, nhận 100 thẻ nghe hợp lý, import chúng, và dành sáu tháng học thuộc bốn cái ảo giác cùng chín mươi thứ vặt vãnh.

## Cái gì nên tự động hóa, cái gì không

| Bước | Tự động? | Vì sao |
| --- | --- | --- |
| Tìm các sự kiện ứng viên trong một nguồn | Có | Đọc để tìm sự kiện trích xuất được là việc máy móc |
| Quyết định cái gì đáng nhớ | **Không** | Đây là toàn bộ kỹ năng. Giao việc này đi là bạn không học được gì về chính việc học của mình |
| Phác câu hỏi/câu trả lời | Có | Chọn từ ngữ là máy móc một khi sự kiện đã được chọn |
| Kiểm tra tính atomic | Có | Dựa trên quy tắc; agent áp dụng tốt |
| Kiểm tra lộ đáp án | Có | Dựa trên quy tắc |
| Khử trùng lặp | Có | Hashing và so khớp gần đúng |
| Kiểm chứng sự kiện | **Một phần** | Agent có thể đối chiếu với đoạn nguồn được trích; không thể tin nó kiểm chứng với thế giới thật |
| Lấy mẫu kiểm tra ngẫu nhiên | **Không** | Con người. Lấy mẫu 10%, đọc nguội |

Phân công lao động: **agent đề xuất, con người quyết, agent kiểm toán.**

## Pipeline

```
 source doc
    │
    ├─ 1. EXTRACT   agent lists candidate facts, each with a quoted source span
    │
    ├─ 2. SELECT    human keeps the ones worth remembering  ← the real step
    │
    ├─ 3. DRAFT     agent writes atomic cards from the selected facts
    │
    ├─ 4. AUDIT     agent applies the mechanical checklist (04 + checklist file)
    │
    ├─ 5. DEDUP     hash the fronts against existing decks + sample deck
    │
    ├─ 6. VERIFY    agent re-checks each card against its quoted span
    │
    ├─ 7. SAMPLE    human reads a random 10% cold and grades them
    │
    └─ 8. EXPORT    TSV + manifest  (data/deck-schema.md)
```

Bước 1, 3, 4, 5, 6 có thể chạy không cần người. Bước 2 và 7 thì không.

### Hai bước kiểm tra người ta hay bỏ qua

**Kiểm tra render.** Một thẻ trông ổn trong JSON có thể render ra rác trong Anki, một cách âm thầm. Trước khi xuất, hãy khẳng định một cách máy móc:

- HTML tag cân bằng; mọi `<`, `>`, `&` literal trong code đều được escape thành `&lt;`,
  `&gt;`, `&amp;` (một `<T>` không escape sẽ bị parse như tag và biến mất).
- Toán chỉ dùng `\(...\)` hoặc `\[...\]`. Nếu chuỗi chứa `[$]`, thẻ sẽ cố render một ảnh LaTeX, thứ mặc định bị tắt và **hỏng âm thầm** — thẻ chỉ hiện ra trống trơn.
- Các id cloze liên tục từ `c1`, và không phần thân cloze nào chứa `}}`.
- Không có `::` bên trong đáp án cloze mà không escape (`std::variant` trở thành
  cloze hint; hãy viết `std:<!-- -->:variant`).
- Các file media được tham chiếu đều tồn tại.

**Trọng tài một hơi.** Đưa cho một model thứ hai *chỉ mặt trước* và hỏi: "Could a competent student answer this in one breath, without seeing anything else? Score 1–5." Dưới 4 là loại. Cái này bắt được thất bại mà các kiểm tra dựa trên quy tắc không bắt được: một thẻ atomic, không lộ đáp án, mà vẫn không trả lời được vì mơ hồ hoặc thiếu ngữ cảnh. Kiểm tra quy tắc xác minh hình thức; cái này xác minh khả năng trả lời.

### Vì sao source span là bắt buộc

Mọi sự kiện ứng viên phải mang theo đúng câu trích nó được lấy ra — **tối đa khoảng 40 từ, và câu trích phải chứa câu trả lời, không chỉ chứa chủ đề.** Một span nói "PostgreSQL uses MVCC" không đỡ nổi một thẻ hỏi tên isolation level.

Việc này làm ba thứ cùng lúc:

1. Nó khiến ảo giác trở nên phát hiện được — một thẻ không có span là cờ đỏ ngay từ cấu trúc.
2. Nó cho phép một lần kiểm toán sau đó đọc lại đoạn văn thay vì tin cái thẻ.
3. Nó khiến việc tái tạo trở nên khả thi khi nguồn thay đổi.

Một thẻ không có source span thì không vào deck. Không có ngoại lệ.

## Prompt templates

Đây là điểm khởi đầu, không phải kinh thánh. Chúng được viết để dán thẳng vào.

### 1. Extract

```
You are extracting candidate facts for spaced-repetition cards from a
technical document.

RULES
- Only extract facts that are STABLE (true in a year), ARBITRARY (must be
  memorized, not derivable), and NEEDED COLD (must be recalled without lookup).
- Skip: opinions, design trade-offs, multi-step procedures, anything requiring
  judgment, anything that is obvious from the name.
- Every candidate must include the exact sentence(s) it came from, quoted.

OUTPUT (markdown table)
| # | Fact (one sentence) | Type (definition/complexity/idiom/semantics/comparison) | Quote | Line ref |

Do not write cards yet. Do not invent facts. If the document is thin, return
fewer rows — 5 real candidates beat 30 weak ones.
```

### 2. Draft cards

```
Write Anki cards for the selected facts below.

HARD RULES
- One fact per card. If the answer contains "and", split it.
- The front must name its subject. No pronouns.
- The answer must be producible in under 10 seconds.
- No enumeration ("name the four...").
- The answer must not appear in the question.
- Prefer Cloze when the fact lives in a sentence; Basic otherwise.
- Escape < > & in code as &lt; &gt; &amp;. Indent code with spaces, never tabs.
- MathJax: \(...\) inline, \[...\] display. Never $...$.

OUTPUT (TSV, tab-separated, no header)
NoteType<TAB>Front<TAB>Back<TAB>Tags

For each card also output one manifest line: row, source_span, confidence.
```

### 3. Audit

```
Audit these cards against the checklist. For each card output PASS or FAIL
with the failing check number and a one-line fix.

CHECKS
1  one fact only            9  no near-duplicate
2  answer < 10 seconds      10 no multi-step reasoning
3  front names its subject  11 anchor present if needed
4  answer not in question   12 simplest note type
5  recall, not recognition  13 code escaped, spaces not tabs
6  no enumeration           14 MathJax syntax correct
7  source span present      15 four tag axes present
8  confidence matches source

Be strict. A card that "could be improved" is a FAIL. Return only the table and
a count of passes and fails.
```

Prompt audit là chỗ chứa phần lớn giá trị. Agent từ chối theo tiêu chí tường minh tốt hơn rõ rệt so với việc sinh ra mà không có tiêu chí.

## Các kiểu thất bại và cách bắt chúng

| Thất bại | Triệu chứng | Cách bắt |
| --- | --- | --- |
| **Sự kiện bịa** | Thẻ nêu một API/hành vi không tồn tại; nghe hoàn toàn hợp lý | Không có source span, hoặc span không chứa khẳng định đó. Đọc lại span, đừng bao giờ đọc lại thẻ |
| **Lỗi thời mà tưởng là hiện hành** | Thẻ dạy một API đã bị deprecate như thể nó đang dùng được | `lifecycle::evolving` + một tag `audit::YYYY`; kiểm tra lại hằng năm |
| **Thẻ vặt vãnh** | Đáp án hiển nhiên từ câu hỏi hoặc từ tên gọi | Audit check 4; và bước chọn của con người |
| **Gần trùng lặp** | Cùng một sự kiện, ba cách diễn đạt | Hash mặt trước + độ tương đồng văn bản đã chuẩn hóa. **Đừng dựa vào kiểm tra trùng lặp của chính Anki** — nó so khớp chuỗi chính xác chỉ trên field đầu tiên, nên bỏ sót mọi cách diễn đạt khác |
| **Thẻ mồ côi** | "It returns null" không có chủ thể | Audit check 3 |
| **Thẻ nhận dạng** | "Is X true?" / trắc nghiệm | Audit check 5 |
| **Thẻ nhiều bước** | Đòi phải lần theo một vòng lặp hoặc một phép suy dẫn | Audit check 10 |
| **Deck phình** | 300 thẻ từ một tài liệu 1.000 từ | Trần: tối đa 1 thẻ cho mỗi 100 từ nguồn, và hãy kỳ vọng ít hơn nhiều |
| **Lộ đáp án** | Câu hỏi nhắc lại từ khoá chính trong đáp án | Audit check 4 |

Thất bại tệ nhất là cái đầu tiên, và đó là cái duy nhất một agent không thể tự bắt một cách đáng tin. Spaced repetition khiến ảo giác trở nên *bền vững*, nên bước kiểm chứng không phải chi phí phụ không bắt buộc — nó là lý do pipeline được phép tồn tại.

## Mật độ

Một trần hữu ích: **tối đa một thẻ cho mỗi 100 từ nguồn.** Một tài liệu 2.000 từ cho ra tối đa 20 thẻ, và một lần trích xuất tốt thường cho ra 5–8. Nếu một agent trả về 60, nó đang làm thẻ cho những câu nói lại, không phải cho kiến thức.

Theo dõi tỉ lệ chấp nhận của bạn (thẻ được nhận ÷ thẻ được phác). Một pipeline khỏe nằm quanh 30–50%. Trên 80%, bước audit của bạn quá dễ dãi. Dưới 15%, prompt trích xuất của bạn đang kéo về sai loại sự kiện.

## Các chỉ số cần giữ trong manifest

- **Tỉ lệ chấp nhận** — sức khỏe của bước trích xuất.
- **Tỉ lệ ảo giác** — số thẻ bị loại vì span không đỡ nổi chúng.
  Nên có xu hướng về zero; nếu không, model hoặc nguồn là vấn đề.
- **Tỉ lệ trùng lặp** — nên giảm khi chỉ mục dedup của bạn lớn lên.
- **Số thẻ trên mỗi tài liệu nguồn** — bắt được sự phình to.

## Khi nào không nên tự động hóa

Chỉ tự động hóa sau khi bạn đã tự viết được một thẻ tốt bằng tay và giải thích được vì sao nó tốt. Trước đó, thẻ của agent sẽ trông ổn với bạn và bạn không có cơ sở nào để loại chúng. Tháng đầu tiên là viết tay vì một lý do (`04`).

Ngoài ra: đừng bao giờ tự động hóa việc *chọn* học cái gì. Một agent sẽ vui vẻ tạo một deck 200 thẻ cho một chủ đề bạn không cần. Deck trở thành một nghĩa vụ, và nghĩa vụ thì bị bỏ.

## Hợp đồng xuất file

Theo [`data/deck-schema.md`](../../data/deck-schema.md):

- `data/decks/<name>.tsv` — bốn cột, phân tách bằng tab, UTF-8 không BOM.
- `data/decks/<name>.manifest.json` — nguồn gốc, độ tin cậy, trạng thái review.

Một deck không thể kiểm toán là một deck bạn sẽ không bảo trì.

→ Tiếp: [07 — Lộ trình CS](07-cs-roadmap.md)
