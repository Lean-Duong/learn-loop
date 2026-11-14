> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# 04 — Thiết kế thẻ Anki

Anki là một scheduler. Nó không có ý kiến gì về việc một thẻ có đáng ôn hay không. Bạn cung cấp phán đoán đó, và đó là toàn bộ cuộc chơi: một deck toàn thẻ dở sẽ sản xuất ra kiến thức sai trôi chảy, theo đúng lịch, trong nhiều năm.

Tài liệu này là phần bạn không được đọc lướt.

## Nguyên tắc duy nhất

**Một thẻ chỉ nên kiểm tra đúng một đơn vị có thể truy xuất, được gợi ý đủ rõ để câu trả lời không mơ hồ.**

Mọi thứ bên dưới chỉ là hệ quả.

Vì sao "một đơn vị" không phải là chuyện câu nệ:

- Anki lên lịch cho một thẻ như một khối. Nếu một thẻ chứa ba sự kiện mà bạn biết hai, bạn sẽ chấm nó "hard" mãi mãi. Nó trở thành một **leech** — thẻ bạn trượt lặp đi lặp lại — và bạn chẳng học được gì từ việc lặp lại ngoài sự bực bội.
- Độ khó của việc truy xuất nuôi mô hình lên lịch. Một thẻ khó vì nó *là ba câu hỏi bị ghim vào nhau* sẽ dạy cho scheduler điều sai về bạn.
- Kiến thức một phần là vô hình. Bạn sẽ tin rằng mình biết thẻ đó.

## Bốn thuộc tính

| Thuộc tính | Phép thử | Sửa gì nếu trượt |
| --- | --- | --- |
| **Atomic** | Câu trả lời có thể phát biểu thành một câu, không có chữ "and"? | Tách thành hai thẻ |
| **Cued** | Mặt trước có xác định duy nhất câu trả lời? | Thêm chi tiết phân biệt vào mặt trước |
| **Standalone** | 8 tháng nữa, không có ngữ cảnh, bạn có hiểu nó không? | Gọi tên chủ thể một cách tường minh |
| **Retrievable** | Bạn có thể tạo ra nó trong dưới ~10 giây? | Đó là bài luyện tập, không phải thẻ |

Giới hạn "10 giây" không nói về tốc độ. Nó là đại diện cho *một đơn vị truy xuất duy nhất*. Nếu để tạo ra câu trả lời bạn phải dựng lại cả một chuỗi, thì bạn đang luyện một phép suy dẫn, và Anki là cái hộp sai để chứa nó.

## Note types

| Loại | Dùng khi | Ví dụ |
| --- | --- | --- |
| `Basic` | Hướng của câu hỏi cố định | "Binary search worst case?" → O(log n) |
| `Basic (and reversed)` | Cả hai chiều đều thực sự hữu ích | thuật ngữ ↔ định nghĩa, khi việc tạo ra thuật ngữ từ định nghĩa là quan trọng |
| `Cloze` | Sự kiện nằm trong một câu | "... membership in a Python `list` is O({{c1::n}})..." |

Thẻ đảo chiều bị dùng quá nhiều. "What is O(log n)?" có vô số câu trả lời — đó là một thẻ đảo tồi. Chỉ đảo khi chiều đảo *cũng* là một sự kiện duy nhất.

Cloze là mặc định tốt nhất cho tài liệu kỹ thuật vì nó giữ lại ngữ cảnh khiến sự kiện có nghĩa. Rủi ro là lạm dụng cloze: xóa một từ khỏi câu mà bạn không hiểu sẽ tạo ra thẻ kiểm tra việc nhận dạng hình dạng từ. Câu bao quanh phải thực sự làm việc.

## Mẫu theo loại nội dung

| Nội dung | Mẫu | Tốt | Dở |
| --- | --- | --- | --- |
| Định nghĩa | Basic, thuật ngữ → định nghĩa một câu | "What does *idempotent* mean for an HTTP method?" | "Define idempotency, statelessness, and safety" |
| Độ phức tạp | Basic, tên thuật toán + trường hợp → cận | "Merge sort, worst case?" → O(n log n) | "What is the complexity of sorting?" |
| Idiom code | Cloze bên trong một đoạn code thật | "`x in s` is O({{c1::1}}) for a `set`, O({{c1::n}}) for a `list`" | "How do you check membership in Python?" |
| Toán | Basic hoặc cloze với MathJax | "Master theorem, $T(n)=2T(n/2)+n$ → {{c1::Θ(n log n)}}" | "State the master theorem" |
| So sánh | Basic, một trục phân biệt | "`rebase` vs `merge`: which rewrites commit hashes?" | "Compare rebase and merge" |
| Tiếng Anh | Cloze trên collocation, trong một câu | "We need to {{c1::mitigate}} the risk, not eliminate it" | "What does mitigate mean?" |
| Cách hỏng | Basic, triệu chứng → nguyên nhân | "Query suddenly slow after adding an index on a low-cardinality column. Likely cause?" | "List reasons a query is slow" |

Để ý hình dạng: mọi thẻ tốt đều gọi tên chủ thể của nó và hỏi một thứ. Mọi thẻ dở đều là một đề bài tiểu luận con.

## Vấn đề liệt kê

Đây là lỗi phổ biến nhất, và là lỗi AI tạo ra nhiều nhất.

**Dở:** "What are the four ACID properties?"
Bạn sẽ học *rằng có bốn cái*. Bạn sẽ không học một cách đáng tin atomicity, consistency, isolation, durability — và nếu bỏ sót một cái, bạn không thể biết mình sót cái nào.

**Sửa — một thẻ cho mỗi thuộc tính, mỗi thẻ từ một góc khác nhau:**

- "A transaction that transfers money debits one account and credits another,
  and a crash occurs between the two. Which ACID property is violated?" →
  atomicity
- "Which ACID property guarantees that concurrent transactions produce the same
  result as some serial order?" → isolation
- "Cloze: Durability guarantees that committed data survives {{c1::a crash or
  power loss}}."

Cùng một kiến thức, bốn đơn vị truy xuất, bốn lịch sử lên lịch độc lập.

Quy tắc chung: **đừng bao giờ hỏi một tập hợp; hãy hỏi một thành viên, hoặc hỏi điều gì phân biệt một thành viên này với thành viên khác.**

## Mạng nhiều góc

Với bất cứ thứ gì quan trọng, một thẻ là không đủ — một thẻ kiểm tra một liên kết. Dựng 3–5 thẻ trên các góc độc lập (thiết kế prompt của Matuschak):

1. **Definition** — nó là gì?
2. **Mechanism** — vì sao nó hoạt động theo cách này?
3. **Precondition** — khi nào nó áp dụng / không áp dụng?
4. **Contrast** — khác biệt then chốt so với lựa chọn gần nhất là gì?
5. **Failure** — điều gì xảy ra khi một ràng buộc bị vi phạm?

Năm góc không phải năm bản sao. Mỗi cái là một đường truy xuất riêng vào cùng một khái niệm, và chính điều đó làm khái niệm trở nên vững chắc, chứ không phải thẻ.

## Ngữ cảnh: vấn đề thẻ mồ côi

Thẻ viết khi đang đọc một đoạn văn thừa hưởng đại từ của đoạn văn đó. Sáu tháng sau, "it" và "this function" vô nghĩa.

**Dở:** "What does it return when the list is empty?"
**Tốt:** "In Python, `min([])` raises what?"

Cách sửa là máy móc: mọi mặt trước của thẻ phải gọi tên chủ thể. Nếu chủ thể là một ký hiệu code, hãy đưa ký hiệu đó vào.

Lỗi liên quan là **sự kiện không neo**: "The default timeout is 30 seconds." Của cái gì? Một sự kiện không có neo thì không thể truy xuất được trong thế giới thật, chỉ trong deck — mà deck thì bị xóa.

## Những gì không nên thành thẻ

| Không thành thẻ | Vì sao | Thay vào đó |
| --- | --- | --- |
| Giải bài toán ("find the bug in this 40-line function") | Suy luận nhiều bước; thẻ sẽ kiểm tra cả chuỗi | Bài luyện tập, đan xen |
| Phán đoán thiết kế ("should you use a queue here?") | Phụ thuộc ngữ cảnh mà một thẻ không chứa nổi | Viết một design note; thảo luận |
| Khối code lớn | Nhớ 30 dòng không phải một đơn vị truy xuất | Nhớ *hình dạng*: chữ ký, invariant, độ phức tạp |
| "Hiểu" | Không phải một đơn vị truy xuất | Truy xuất *các thành phần* của sự hiểu |
| Bất cứ thứ gì tra 3 giây là ra và không bao giờ cần offline | Phình deck thuần túy | Không gì cả |
| Sự kiện từ một blog post duy nhất bạn chưa kiểm chứng | Rủi ro ảo giác tích lũy theo số lần lặp | Kiểm chứng trước (`06`) |

Một bộ lọc hữu ích: **biết chắc thứ này có làm thay đổi việc tôi làm không?** Nếu không, đó là chuyện vặt. Chuyện vặt thì được phép, nhưng nên gắn tag `tier::exam` hoặc bỏ, đừng trộn vào deck quan trọng.

## Chính sách leech

Trượt 8+ lần không phải vấn đề kỷ luật, đó là vấn đề của thẻ. Ba cách xử lý, theo thứ tự:

1. Xóa nó. Có những sự kiện thuộc về một tài liệu tham chiếu, không thuộc về trí nhớ.
2. Tách nó thành hai thẻ nhỏ hơn.
3. Thêm một gợi ý khiến câu trả lời thực sự xác định được.

Đừng cố cày tiếp. Cày một leech tốn thời gian ôn tập và dạy bạn sợ cái deck.

## Viết tay trước

Tháng đầu tiên, hãy tự viết mọi thẻ. Đây không phải chuyện tình cảm — đó là cách duy nhất để hiệu chuẩn cảm giác "atomic" và "cued" là như thế nào. Người bắt đầu bằng deck do AI tạo sẽ không bao giờ phát triển được phán đoán để kiểm toán chúng, mà việc kiểm toán mới là phần quan trọng (`06`).

Sau một tháng, bạn sẽ đọc một đoạn văn và thấy ba cái thẻ trong đó. Lúc đó hãy tự động hóa.

## Tóm tắt một trang

- Một sự kiện mỗi thẻ.
- Gọi tên chủ thể.
- Hỏi một thứ, không hỏi một danh sách.
- Câu trả lời phải tạo ra được trong mười giây.
- Không làm thẻ cho bất cứ thứ gì cần suy luận nhiều bước.
- Nếu bạn trượt nó tám lần, thẻ sai, không phải bạn.
- Kiểm tra mọi thẻ theo
  [`templates/card-quality-checklist.md`](../../templates/card-quality-checklist.md).

→ Tiếp: [05 — Lịch ôn Anki](05-anki-scheduling.md)
