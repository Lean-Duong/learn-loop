> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# 08 — Tiếng Anh cho lập trình viên

Hai mục tiêu khác nhau bị lẫn ở đây, và sự lẫn lộn đó làm mất nhiều năm:

- **Tiếng Anh như một môn học** — ngữ pháp, thi cử, bốn kỹ năng cân bằng.
- **Tiếng Anh như một công cụ** — đọc một spec, theo kịp một talk hội nghị, viết một
  commit message rõ ràng, sống sót qua một buổi phỏng vấn.

Với một sinh viên CS, phiên bản công cụ trả tiền trước và trả tiền liên tục. Phiên bản môn học đáng làm, nhưng không nên là điểm vào, vì nó chậm, trừu tượng, và dễ bị bỏ.

Tài liệu này nói về phiên bản công cụ, với Anki là lớp giữ lại.

## Cái gì thực sự dự đoán tiến bộ

| Yếu tố | Bằng chứng | Ghi chú |
| --- | --- | --- |
| Lượng input hiểu được | `[moderate]` | Meta-analysis về extensive reading (Nakanishi 2015) cho thấy hiệu ứng thật nhưng ở mức vừa |
| Kích thước vốn từ | `[strong]` | Ngưỡng bao phủ là con số được thiết lập vững nhất trong lĩnh vực |
| Gặp lặp lại một từ trong ngữ cảnh | `[strong]` | Học ngẫu nhiên cần khoảng 8–10 lần gặp (Webb & Chang) |
| Output có phản hồi | `[moderate]` | Giả thuyết output của Swain; viết/nói buộc phải truy xuất |
| Học có chủ đích các từ tần suất cao | `[strong]` | 2.000 word family tần suất cao nhất bao phủ ~80% văn bản đang chạy |
| Bài tập ngữ pháp tách rời | `[practice]` | Chuyển giao thấp; ngữ pháp học tốt hơn như sản phẩm phụ của input + output |

Con số hữu ích nhất: **98% bao phủ** là ngưỡng mà ở đó bạn đọc được không cần trợ giúp mà không phải dừng liên tục (Hu & Nation 2000; Laufer & Ravenhorst-Kalovski 2010). Với tiểu thuyết đó là khoảng 8.000–9.000 word family. Với tài liệu kỹ thuật, vốn từ hẹp hơn và lặp nhiều hơn, nên ngưỡng đến sớm hơn nhiều — đó là lý do một sinh viên CS có thể đọc docs của một framework thành thạo rất lâu trước khi đọc nổi một cuốn tiểu thuyết.

**Hệ quả thực tế:** đừng cố học "từ vựng tiếng Anh" nói chung. Học (a) khoảng 2.000 từ thông dụng nhất cho đến hết, rồi (b) văn phong kỹ thuật bạn thực sự gặp. Mọi thứ còn lại tốt hơn là thu nạp qua đọc.

## Bốn sợi (Four Strands), áp dụng

Khung của Nation nói một khóa học cân bằng cần bốn loại việc. Áp dụng cho một lập trình viên có 20 phút mỗi ngày:

| Sợi | Tỉ trọng | Với bạn nó trông như thế nào |
| --- | --- | --- |
| Input tập trung vào nghĩa | ~40% | Đọc docs, changelog, RFC, thông báo lỗi, blog post. Nghe talk ở tốc độ 1× |
| Output tập trung vào nghĩa | ~20% | Viết commit message, mô tả PR, comment code, một ghi chú kỹ thuật ngắn bằng tiếng Anh |
| Học tập trung vào ngôn ngữ | ~25% | Anki cho từ tần suất cao, collocation, và thuật ngữ kỹ thuật bạn gặp hoài |
| Phát triển độ trôi chảy | ~15% | Đọc lại một thứ dễ thật nhanh; shadow một talk; giải thích lại một khái niệm bằng tiếng Anh không dừng |

Thất bại phổ biến là 100% input. Bạn có thể đọc tiếng Anh nhiều năm và vẫn đông cứng khi phải tạo ra một câu, vì sản sinh là một kỹ năng khác với một đường truy xuất khác.

## Vì sao Anki giúp ở đây, và chỗ nó không giúp

Anki xuất sắc cho phần vốn từ mang tính **tùy ý**. Rằng `mitigate` nghĩa là "make less severe" là một quy ước; không có cách nào suy ra nó. Các ánh xạ tùy ý đúng là thứ spaced repetition sinh ra để làm.

Anki dở cho phần mang tính **cấu thành** — cấu trúc câu, diễn ngôn, văn phong. Những thứ đó cần input và output, không phải truy xuất.

Nên quy tắc là: **làm thẻ cho đơn vị tùy ý, đọc cho mọi thứ còn lại.**

### Những dạng thẻ hiệu quả

**1. Cloze trên collocation (thẻ tiếng Anh giá trị cao nhất).**
> We need to {{c1::mitigate}} the risk, not eliminate it.

Cái này dạy cả từ *và* collocation của nó (*mitigate a risk*, không phải *reduce a
risk* trong văn viết trang trọng). Thẻ ở mức từ bỏ sót hoàn toàn điều này.

**2. Thuật ngữ kỹ thuật trong một câu thật.**
> The request is {{c1::idempotent}}, so retrying it is safe.

Tốt hơn "What does idempotent mean?" vì nó cũng mã hóa luôn cách *dùng*.

**3. Cặp tương phản.**
> `affect` is a {{c1::verb}}; `effect` is usually a {{c1::noun}}.

**4. Word family / hình thái học.**
> `robust` → noun: {{c1::robustness}}. The system lacks robustness.

**5. Truy xuất theo ngữ cảnh đọc (dùng tiết kiệm).**
> In a code review, "this is a nit" means {{c1::a minor style point, not a blocker}}.

Cái cuối là kiến thức về văn phong — giá trị cao với một lập trình viên, và gần như không bao giờ được dạy.

### Những dạng thẻ không hiệu quả

| Thẻ dở | Vì sao |
| --- | --- |
| "What does *ubiquitous* mean?" | Từ hiếm tách rời; bạn sẽ gặp nó hai lần một năm |
| Từ → chỉ bản dịch tiếng Việt | Bạn học một ánh xạ, không học cách dùng. Cũng phá thói quen chỉ dùng tiếng Anh |
| "List 5 synonyms of big" | Liệt kê; và từ đồng nghĩa hiếm khi thay thế được cho nhau |
| Một thẻ cho mọi từ lạ trong một bài báo | Deck phình, 90% không bao giờ được ôn |
| Thẻ quy tắc ngữ pháp ("when do you use present perfect?") | Quy tắc không phải đơn vị truy xuất; chúng cần ví dụ |

Rủi ro phình to là đặc thù và nghiêm trọng với tiếng Anh. Một sinh viên đọc một bài báo có thể tạo 40 thẻ. Mười hai trong đó đáng giữ. Bộ lọc: **tháng này tôi có dùng từ này khi viết hoặc khi nói không?** Nếu không, đừng làm thẻ — tra lại sau, hoặc để ngữ cảnh dạy nó.

## Đọc: thói quen đòn bẩy cao nhất

Với một lập trình viên, đọc là kỹ năng tích lũy. Cụ thể:

1. **Luôn đọc tài liệu bằng tiếng Anh.** Đừng bao giờ chuyển sang bản dịch.
   Tài liệu là thể loại duy nhất cho bạn input dày, lặp lại, giàu ngữ cảnh đúng
   trên thứ từ vựng bạn cần.
2. **Đọc thông báo lỗi chậm.** Chúng là một bộ từ vựng có kiểm soát — đúng 200 cụm
   đó lặp lại suốt cả sự nghiệp. Học cách parse chúng chính xác đáng giá hơn mọi
   cuốn sách ngữ pháp.
3. **Đọc một RFC hoặc design doc mỗi tháng**, kể cả chỉ một phần. Văn phong
   ("MUST", "SHOULD", "in the absence of") là văn phong của mọi spec bạn sẽ đọc.
4. **Đọc changelog.** Miễn phí, ngắn, và dạy bạn cách ngôn ngữ versioning hoạt động.

Mục tiêu: 20–30 phút mỗi ngày với văn bản tiếng Anh thật mà bạn thực sự muốn đọc. Truyện tranh, forum, và man page đều tính. Graded reader thì không, với bạn — bạn đã qua mức đó và chúng sẽ làm bạn chán đến mức bỏ.

## Nghe và nói

- **Nghe:** talk hội nghị (1×, không phụ đề trước, rồi bật phụ đề). Mục tiêu là
  parse được lời nói liền mạch, không phải hiểu ý — bạn đã biết ý rồi.
- **Shadowing:** phát 30 giây, lặp lại thành tiếng đồng thời, khớp nhịp điệu.
  Đây là cách sửa nhanh nhất khoảng cách "đọc được mà không nói được" `[practice]`
  nhưng nó đã được thiết lập vững trong giảng dạy phát âm.
- **Nói:** phiên bản rẻ nhất là nói chuyện với một AI bằng tiếng Anh về chính công
  việc của bạn — giải thích một quyết định thiết kế, một bug, một đánh đổi. Bạn
  đang luyện sản sinh, không phải luyện hội thoại. Ghi lại và nghe lại một lần.

Nói quan trọng nhất cho phỏng vấn, sự kiện tiếng Anh có mức cược cao nhất trong đời một lập trình viên. Hãy luyện mô tả dự án của bạn bằng tiếng Anh trước khi bạn cần đến nó.

## Một vòng lặp tiếng Anh tối thiểu

| Khi nào | Làm gì | Phút |
| --- | --- | --- |
| Hằng ngày | Deck tiếng Anh trên Anki (chỉ thẻ đến hạn) | 5 |
| Hằng ngày | Đọc một thứ bạn muốn đọc, bằng tiếng Anh | 20 |
| Hằng tuần | Viết một đoạn kỹ thuật bằng tiếng Anh (PR, ghi chú, comment) | 15 |
| Hằng tuần | Shadow một đoạn talk | 10 |
| Hằng tháng | Đọc lại một ghi chú cũ của bạn và sửa tiếng Anh trong đó | 15 |

Đó là dưới 40 phút một ngày và đủ để tiếp tục tiến bộ trong nhiều năm, vì tất cả đều là dùng thật chứ không phải học.

## Cái bẫy

Cái bẫy là coi tiếng Anh như một điều kiện tiên quyết: "Tôi sẽ học tiếng Anh, rồi mới học lập trình cho tử tế." Thứ tự đó ngược và chậm. Hãy làm việc kỹ thuật bằng tiếng Anh ngay từ ngày đầu, một cách dở tệ, với từ điển mở bên cạnh. Từ vựng đến vì bạn cần nó, và đó là lý do duy nhất từ vựng từng đọng lại.

→ Tiếp: [09 — Vòng lặp hằng tuần](09-weekly-loop.md)
