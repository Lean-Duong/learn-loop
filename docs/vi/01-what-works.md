> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# 01 — Cái gì vẫn còn hiệu quả

Câu hỏi hữu ích không phải "kỹ thuật học nào tốt" mà là "kỹ thuật nào đã sống sót qua các nỗ lực bác bỏ nó, và trong điều kiện nào thì chúng phản tác dụng".

Tài liệu này tổ chức theo độ mạnh của bằng chứng, không theo mức độ phổ biến. Mốc neo là Dunlosky et al. (2013), bài review mười kỹ thuật trên toàn bộ tài liệu thực nghiệm và xếp hạng chúng theo độ tổng quát và chất lượng bằng chứng. Phần lớn những gì sau đây hoặc xác nhận hoặc tinh chỉnh bài review đó.

## Bản ngắn

| Kỹ thuật | Bằng chứng | Tốt nhất cho | Hỏng khi |
| --- | --- | --- | --- |
| Retrieval practice | `[strong]` | Mọi thứ | Prompt mơ hồ hoặc câu trả lời gồm nhiều phần |
| Spaced repetition | `[strong]` | Fact bền, từ vựng, thành ngữ | Thẻ không atomic; interval bị dồn |
| Interleaving | `[strong]` | Phân loại bài toán, phân biệt | Bạn chưa học từng quy trình riêng lẻ |
| Worked examples | `[strong]` | Người mới trong lĩnh vực quy trình | Bạn đã đủ giỏi (expertise reversal) |
| Self-explanation | `[moderate]` | Tài liệu khái niệm | Bạn giải thích mơ hồ và không bao giờ kiểm tra lời giải thích |
| Elaborative interrogation | `[moderate]` | Fact có cấu trúc nhân quả | Fact là tùy tiện (không tồn tại "vì sao") |
| Deliberate practice | `[moderate]` | Hiệu suất có kỹ năng | Nhiệm vụ không được định nghĩa rõ, hoặc không có feedback |
| Project-based learning | `[moderate]` | Tích hợp, động lực | Nó thay thế việc giảng dạy thay vì đến sau việc giảng dạy |
| Dual coding | `[moderate]` | Tài liệu không gian/cấu trúc | Sơ đồ chỉ để trang trí |
| Sleep and consolidation | `[strong]` | Ghi nhớ mọi thứ | Bạn dùng nó làm cớ để bỏ qua ôn tập |

## Retrieval practice

**Nó là gì.** Tạo ra thông tin từ trí nhớ thay vì để bản thân tiếp xúc lại với nó. Sách đóng, trang giấy trắng, một flashcard, một bài quiz.

**Bằng chứng.** Roediger & Karpicke (2006) cho thấy sinh viên đọc một đoạn văn một lần rồi tự kiểm tra đạt kết quả tốt hơn sinh viên đọc bốn lần, trên một bài test trễ — trong khi nhóm đọc lại *dự đoán* là mình làm tốt hơn. Karpicke & Blunt (2011) thấy retrieval practice đánh bại concept mapping kiểu elaborative ở các câu hỏi transfer, không chỉ ở nhớ nguyên văn. Đây là một trong những phát hiện được lặp lại nhiều nhất trong lĩnh vực này `[strong]`.

Cơ chế không bí ẩn: truy xuất một ký ức sẽ sửa đổi nó, khiến lần sau dễ truy xuất hơn, và chính nỗ lực truy xuất là thứ tạo ra tác dụng. Nhận ra (recognition) không tính. Đọc lời giải rồi gật đầu không tính.

**Với CS.** Retrieval practice là lý do "tôi hiểu khi đọc code" và "tôi viết được từ đầu" là hai kỹ năng khác nhau, và chỉ cái thứ hai sống sót qua một buổi phỏng vấn hay một sự cố. Các dạng thực dụng:

- Đóng editor và viết chữ ký hàm, invariant, độ phức tạp, từ trí nhớ.
- Đoán output của một đoạn code trước khi chạy nó.
- Giải thích failure mode của một hệ thống thành tiếng mà không có ghi chú.
- Tự suy lại một chứng minh hoặc hệ thức truy hồi của thuật toán thay vì đọc lại.

**Failure mode.** Retrieval practice trên một prompt được tạo kém sẽ luyện sai thứ. Nếu câu hỏi là "giải thích TCP", bạn sẽ truy xuất một đoạn văn mơ hồ mãi mãi và không bao giờ nhận ra nó mơ hồ. Prompt phải nêu một đơn vị có thể truy xuất cụ thể. Đây chính là toàn bộ lý do thiết kế thẻ Anki quan trọng (`04-anki-card-design.md`).

## Spaced repetition

**Nó là gì.** Ôn lại theo interval giãn ra, canh đúng ngay trước khi bạn sẽ quên.

**Bằng chứng.** Meta-analysis của Cepeda et al. (2006) trên 254 nghiên cứu: spaced practice đánh bại massed practice một cách ổn định, và khoảng cách tối ưu tỷ lệ với việc bạn cần nhớ tài liệu bao lâu. Cepeda et al. (2008) thấy khoảng cách tối ưu vào khoảng 10–20% của retention interval. `[strong]`

**Với CS.** Những fact sẽ không thay đổi: complexity class, handshake của giao thức, ngữ nghĩa SQL, idiom của ngôn ngữ, collocation tiếng Anh. Spaced repetition là công cụ đúng và gần như là công cụ duy nhất. Nó là công cụ sai cho design judgment và debugging, những thứ cần luyện đa dạng chứ không phải recall (`04`).

**Failure mode.** Giãn cách một thẻ tệ làm nó tệ hơn chứ không tốt hơn: bạn tập lại cùng một câu trả lời sai theo lịch và nó trở nên trôi chảy. Ngoài ra, giãn cách chỉ hiệu quả nếu interval thật sự giãn ra — ôn mọi thứ hằng ngày là massed practice mặc áo hóa trang.

## Interleaving

**Nó là gì.** Trộn các loại bài toán trong một buổi thay vì block một loại.

**Bằng chứng.** Rohrer & Taylor (2007) về luyện toán và Kornell & Bjork (2008) về category induction đều thấy interleaved practice cho hiệu suất tệ hơn trong lúc luyện và tốt hơn ở các bài test trễ `[strong]`. Cảm giác khó chịu chính là mục đích.

**Với CS.** Đây là kỹ thuật bị dùng ít nhất trong việc học lập trình. Làm mười bài binary search liên tiếp dạy bạn pattern-match theo tiêu đề mục. Một set trộn — hai binary search, hai DP, hai graph, hai bài lạ — buộc bạn phải *phân loại* bài toán, và đó mới là kỹ năng thật. Tương tự với debugging: trộn các loại bug đánh bại một tutorial về "năm loại bug".

**Failure mode.** Interleaving trước khi bạn thực hiện được bất kỳ quy trình đơn lẻ nào tạo ra sự lẫn lộn, không phải sự phân biệt. Học quy trình theo kiểu block trước (thường với worked example), rồi mới interleave.

## Worked examples, và expertise reversal effect

**Nó là gì.** Học một lời giải đã làm đầy đủ trước khi thử làm bài.

**Bằng chứng.** Với người mới, worked example đánh bại việc giải bài không hướng dẫn, vì chúng giải phóng working memory cho việc xây schema (lý thuyết cognitive load của Sweller). Nhưng Kalyuga et al. (2003) cho thấy hiệu ứng đảo ngược: khi bạn đã có schema, worked example trở nên dư thừa và *tệ hơn* so với tự giải `[strong]`.

**Với CS.** Điều này giải quyết một cuộc tranh cãi bạn thấy liên tục trên mạng. "Đừng xem lời giải" đúng với người đã có schema và sai với người mới, người mà nếu không thì sẽ mất bốn tiếng mà không học được gì. Quy tắc trung thực: đọc worked example, rồi lập tức tái tạo nó từ trí nhớ, rồi giải một biến thể mà không nhìn. Điểm chuyển là khi bạn đoán được dòng tiếp theo trước khi đọc nó.

**Failure mode.** Ở lại chế độ worked-example mãi mãi. Đó là tutorial hell với chất lượng sản xuất cao hơn (`02`).

## Self-explanation và elaborative interrogation

**Nó là gì.** Tự giải thích *vì sao* một fact đúng, hoặc vì sao một bước tiếp theo bước trước.

**Bằng chứng.** Chi et al. (1994) thấy sinh viên tự giải thích trong lúc học ví dụ thì học được nhiều hơn; Dunlosky et al. xếp cả hai kỹ thuật ở mức hữu dụng trung bình — chúng có giúp, nhưng yếu hơn testing và spacing, và dễ làm sai `[moderate]`.

**Với CS.** Phiên bản hiệu quả là phiên bản đối kháng: "vì sao cái này là O(log n) mà không phải O(n)?", "cái gì hỏng nếu tôi bỏ lock này?", "vì sao tác giả chọn B-tree ở đây thay vì hash index?". Phiên bản không hiệu quả là diễn giải lại đoạn văn bạn vừa đọc.

**Failure mode.** Confabulation. Một lời giải thích sai nhưng tự tin có cảm giác giống hệt một lời giải thích đúng khi nhìn từ bên trong. Đây là lý do self-explanation cần một bước kiểm tra — một bài test, một người khác, hoặc một AI reviewer được dùng như *critic* chứ không phải đáp án (`03`).

## Deliberate practice

**Nó là gì.** Luyện trên một điểm yếu cụ thể, ở rìa năng lực, với feedback tức thời, lặp lại kèm sửa.

**Bằng chứng.** Cách diễn đạt gốc của Ericsson thường bị nói quá. Meta-analysis của Macnamara et al. (2014) thấy deliberate practice giải thích khoảng 26% phương sai trong game, 21% trong âm nhạc, 18% trong thể thao, 4% trong giáo dục, và dưới 1% trong các nghề `[moderate]` — có thật, nhưng không ở đâu gần câu chuyện "10.000 giờ" (`02`).

**Với CS.** Phần hữu ích là cấu trúc: chọn một điểm yếu (ví dụ, lập luận về concurrency), lấy feedback nhanh (test, reviewer, profiler), sửa, lặp lại. Phần vô dụng là đếm giờ.

**Failure mode.** Luyện những thứ bạn đã giỏi vì nó có cảm giác năng suất. Deliberate practice được cho là phải có cảm giác như thất bại.

## Project-based learning

**Nó là gì.** Xây một thứ thật, có ràng buộc, từ đầu đến cuối.

**Bằng chứng.** Meta-analysis của Freeman et al. (2014) trên 225 nghiên cứu STEM thấy active learning tăng điểm thi khoảng ~0,47 SD và giảm tỷ lệ trượt `[strong]` đối với *active learning*; project-based learning nói riêng là `[moderate]`, vì "project" bao trùm mọi thứ từ một bài build có hướng dẫn đến việc bị thả xuống giữa biển.

**Với CS.** Project là nơi các fact riêng lẻ trở thành một hệ thống, và systems thinking là phần AI chưa thương mại hóa (`07`). Nhưng một project không có review và không có ràng buộc dạy bạn ship bất cứ thứ gì compile được.

**Failure mode.** Project-based learning được dùng như *thay thế* cho giảng dạy. Kirschner, Sweller & Clark (2006) là lập luận chuẩn: hướng dẫn tối thiểu không hiệu quả với người mới, và "cứ build cái gì đó đi" là hướng dẫn tối thiểu.

## Teach-back / Feynman

**Nó là gì.** Giải thích khái niệm bằng ngôn ngữ đơn giản cho một người mới tưởng tượng, tìm điểm lời giải thích sụp đổ, quay lại nguồn.

**Bằng chứng.** Đây là một dạng self-explanation cộng retrieval, nên bằng chứng thừa hưởng từ cả hai `[moderate]`. Nhãn "Feynman technique" cụ thể không có tài liệu riêng.

**Với CS.** Hiệu quả với các cơ chế có chuỗi nhân quả (hash table resize thế nào, vì sao TCP handshake cần ba packet). Thất bại với bất cứ thứ gì bạn chỉ có thể chỉ tay vào.

**Failure mode.** Tự giải thích bằng tốc ký riêng của mình, cái đó có cảm giác như đang dạy và thật ra là recognition. Giải thích cho một người thật, hoặc viết ra rồi đọc lại sau một tuần.

## Dual coding

**Nó là gì.** Ghép tài liệu bằng lời với một biểu diễn thị giác hoặc cấu trúc.

**Bằng chứng.** Hỗ trợ ở mức trung bình, mạnh nhất khi hình ảnh mã hóa cấu trúc mà lời nói không mang được hiệu quả `[moderate]`. Phiên bản "learning styles" của ý tưởng này là sai (`02`).

**Với CS.** Memory diagram, state machine, call stack, cấu trúc index. Tự vẽ B-tree là kỹ thuật; nhìn vào một sơ đồ B-tree thì không phải.

## Sleep

**Nó là gì.** Consolidation trong lúc ngủ ổn định và tích hợp những gì bạn học.

**Bằng chứng.** Review của Diekelmann & Born (2010): ngủ sau khi học cải thiện ghi nhớ, và hiệu ứng đủ lớn để có ý nghĩa với thời điểm thi `[strong]`. Thức trắng đêm đổi consolidation lấy exposure và thua.

**Với CS.** Phiên bản thực dụng không hào nhoáng: ôn trước khi ngủ thay vì lúc 2 giờ sáng, và đừng lên lịch một buổi nhồi vào đêm trước bài thi thực hành.

**Failure mode.** Coi giấc ngủ là thay thế cho retrieval. Consolidation củng cố những gì đang có; nó không tạo ra ký ức.

## Desirable difficulties

Cách diễn đạt của Bjork, và là lăng kính đúng cho mọi thứ ở trên: những điều kiện làm hiệu suất *tệ hơn trong lúc học* và ghi nhớ *tốt hơn về sau* — spacing, interleaving, testing, luyện đa dạng, tự tạo ra trước khi được giảng.

Đây là lý do tự đánh giá không đáng tin. Những kỹ thuật có cảm giác hiệu quả (đọc lại, highlight, xem một bài giảng rõ ràng) lại là những kỹ thuật không hiệu quả. Những kỹ thuật tốt sẽ có cảm giác tệ — hãy coi đó là bình thường.

## Điều này nghĩa là gì với bạn

Ba kỹ thuật mang phần lớn giá trị, và chúng kết hợp với nhau:

1. **Retrieval** — bạn tạo ra câu trả lời, không phải nhận ra nó.
2. **Spacing** — bạn quay lại với nó sau đó, theo lịch.
3. **Interleaving** — bạn trộn loại để học cách phân loại, không chỉ thực thi.

Anki triển khai 1 và 2 gần như hoàn hảo. Nó triển khai 3 tệ — đó là việc của bạn, trong cách bạn sắp xếp các buổi luyện. Mọi thứ khác trong tài liệu này hoặc là một sự tinh chỉnh hoặc là một trường hợp đặc biệt.

→ Tiếp: [02 — Cái gì đã lỗi thời](02-what-is-outdated.md)
