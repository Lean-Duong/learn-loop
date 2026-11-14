> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# 07 — Lộ trình CS trong kỷ nguyên AI

Đây không phải một chương trình học. Đây là một lập luận về **cái gì nên đi sâu**, và một đường đi có thứ tự xây nên một hệ thống thay vì hai mươi tutorial.

Tiền đề: một agent giờ có thể tạo ra code đủ tốt cho những bài toán được đặc tả rõ và có biên giới rõ. Cái nó không làm được là sở hữu một hệ thống, nhận ra đặc tả sai, hay debug một lỗi nó không gây ra. Đó là những kỹ năng khan hiếm, và tất cả đều là kỹ năng chiều sâu.

## Cái gì AI đã làm thành hàng hóa

| Bị hàng hóa hóa | Vì sao nó sụp |
| --- | --- |
| CRUD boilerplate, scaffolding, validate form | Đặc tả đầy đủ, nặng mẫu, kiểm tra rẻ |
| Script đơn giản và glue code | Bán kính ảnh hưởng nhỏ, chạy thử là kiểm được |
| Dịch code giữa các ngôn ngữ | Máy móc, và lỗi lộ ra ngay |
| Unit test thường quy cho hành vi hiển nhiên | Sinh ra nhanh hơn viết tay |
| Tóm tắt tài liệu, viết bản nháp README | Ít rủi ro, dễ review |
| Nhớ chính xác chữ ký API | Chi phí tra cứu về zero |

Nếu kế hoạch của bạn là "giỏi những thứ trong danh sách này", bạn đang luyện cho một công việc đang bị tự động hóa ngay trong lúc bạn luyện.

## Cái gì nó chưa làm thành hàng hóa

| Khan hiếm | Vì sao agent dở ở đó |
| --- | --- |
| Debug một hệ thống bạn không viết | Cần một mô hình về hệ thống không nằm trong context window |
| Suy luận về hiệu năng | Cần đo, không phải sinh; agent đoán mò hot path |
| Tính đúng đắn dưới concurrency | Các kiểu thất bại là phi cục bộ và khó test |
| Mô hình hóa dữ liệu | Phụ thuộc yêu cầu tương lai mà không ai viết ra |
| Bảo mật | Cần tư duy đối kháng với một kẻ tấn công không được đặc tả |
| Viết đặc tả | Agent thực thi một spec; quyết định xây cái gì mới là công việc |
| Phán đoán khi review code | Biết trong 40 diff nghe hợp lý thì cái nào sai |
| Biết khi nào không dùng AI | Gu, và trách nhiệm giải trình |

Để ý rằng phần lớn những thứ này là kỹ năng **hệ thống**, không phải kỹ năng **cú pháp**. Đó là toàn bộ bức tranh chiến lược.

## Phần lõi bền vững

Một bằng CS thực sự để làm gì, xếp theo mức độ trả tiền thuê trong kỷ nguyên AI:

| Môn | Học đến đâu | Vì sao |
| --- | --- | --- |
| Cấu trúc dữ liệu & giải thuật | Sâu | Không phải để phỏng vấn — để suy luận về chi phí. Đây là từ vựng của mọi cuộc nói chuyện về hiệu năng |
| Hệ điều hành | Sâu | Process, bộ nhớ, scheduling, syscall. Mọi lỗi production bí ẩn đều sống ở đây |
| Cơ sở dữ liệu | Sâu | Index, query plan, transaction, isolation level. Phần lớn phần mềm chậm là vấn đề database đội lốt |
| Mạng | Sâu | Độ trễ, hành vi TCP, DNS, TLS. Hệ phân tán là mạng với nhiều kiểu thất bại hơn |
| Toán rời rạc, xác suất | Sâu | Xác suất là ngôn ngữ của hiệu năng, caching và ML |
| Compiler / lý thuyết ngôn ngữ | Vừa | Không phải để viết một cái; để hiểu vì sao một ngôn ngữ hành xử như nó hành xử |
| Đại số tuyến tính | Vừa | Chỉ khi bạn chạm vào ML, đồ họa, hoặc search |
| Giải tích | Đọc lướt | Hiếm khi là điểm chịu lực với một kỹ sư đang làm việc |
| Formal methods | Đọc lướt, rồi quay lại | Giá trị cao trong những lĩnh vực cụ thể (protocol, an toàn) |

Mẫu hình: **chi phí, thất bại, và trạng thái**. Mọi thứ đáng học sâu đều nói về cái gì đó tốn bao nhiêu, nó hỏng thế nào, và trạng thái nằm ở đâu.

## Năng lực thời AI (lớp mới)

Đây là phần mà một chương trình học năm 2015 không bao phủ, và nó nhỏ hơn cơn hype gợi ý.

| Kỹ năng | Nó thực sự nghĩa là gì | Độ ổn định |
| --- | --- | --- |
| Viết đặc tả | Biến một mục tiêu mơ hồ thành tiêu chí chấp nhận mà máy có thể bị ràng buộc theo | Ổn định — đây chỉ là tư duy rõ ràng |
| Evaluation | Dựng bộ test cho biết đầu ra có đúng không. Test property-based, differential, và đối kháng | Ổn định |
| Đọc diff có phê phán | Review đầu ra của agent để tìm cái thất bại mà test bỏ sót | Ổn định |
| Context engineering | Quyết định model thấy gì: file, ví dụ, ràng buộc | Biến động |
| Điều phối tool/agent | Ghép agent, tool, retry, và checkpoint con người | Biến động nhanh |
| Ý thức về kiểu thất bại | Ảo giác, sai âm thầm, sửa quá rộng, nói nhảm đầy tự tin | Ổn định về loại, đổi về chi tiết |
| Ý thức về chi phí và độ trễ | Token, caching, batching, streaming | Biến động |

Quy tắc ngón tay cái: **mọi thứ về tư duy thì ổn định; mọi thứ về một framework cụ thể thì biến động.** Học lớp ổn định cho tử tế và coi lớp biến động là thứ đọc lướt hằng tuần.

### Dữ liệu thực sự nói gì

Bản tóm tắt trung thực của bằng chứng 2025–2026: AI giúp trên công việc greenfield, được đặc tả tốt, và có thể *làm chậm* những lập trình viên có kinh nghiệm trên codebase trưởng thành. Cả hai đều đúng cùng lúc.

| Phát hiện | Nguồn | Độ tin cậy |
| --- | --- | --- |
| Nhanh hơn 55.8% trên một bài greenfield được đặc tả tốt (HTTP server) | GitHub Copilot RCT, Peng et al. 2023, [arXiv:2302.06590](https://arxiv.org/abs/2302.06590) | `[moderate]` — một bài, hẹp |
| *Chậm hơn* 19% với dev OSS có kinh nghiệm trên repo trưởng thành của chính họ | METR RCT 2025, [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | `[moderate]` — dev tin rằng họ nhanh hơn |
| 45% lập trình viên nói debug code do AI sinh tốn thời gian; 46% không tin độ chính xác so với 31% tin | Stack Overflow Developer Survey 2025, [survey.stackoverflow.co/2025](https://survey.stackoverflow.co/2025/ai) | `[moderate]` — tự báo cáo, N lớn |
| Trùng lặp code tăng mạnh khi mức độ dùng AI tăng (phân tích 211M dòng thay đổi, gấp ~4× lượng clone) | GitClear 2025, [gitclear.com](https://www.gitclear.com/ai_assistant_code_quality_2025_research) | `[moderate]` — dữ liệu của nhà cung cấp, phương pháp không công bố đầy đủ |
| Việc làm entry-level (22–25) trong các vai trò phơi nhiễm AI giảm so với các nhóm tuổi lớn hơn | Stanford Digital Economy Lab, Brynjolfsson et al. 2025, [digitaleconomy.stanford.edu](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/) | `[moderate]` — tương quan, không nhân quả |

Đọc cùng nhau: công cụ là một hệ số nhân trên **chất lượng đặc tả và khả năng kiểm chứng**. Ở đâu hai thứ đó cao, nó thắng lớn. Ở đâu bài toán là "hiểu và thay đổi một hệ thống bạn không viết", nó có thể làm bạn mất thời gian. Đó chính xác là lý do những kỹ năng khan hiếm bên dưới là những thứ đáng luyện.

Hai câu sáo rỗng cần bỏ: *"AI won't replace you, someone using AI will"* — dữ liệu 2025 không ủng hộ phiên bản đầy tự tin của câu này. Và *"just learn to prompt"* — prompting là một kỹ năng hai tuần, không phải một sự nghiệp.

### Thang evaluation

"Evaluation" là kỹ năng thời AI mà người ta hay gọi tên rồi không định nghĩa được. Nó là một cái thang, rẻ nhất trước:

| Mức | Bạn viết gì | Bắt được | Chi phí |
| :-: | --- | --- | --- |
| 1 | Test ví dụ: đầu vào đã biết → đầu ra đã biết | Hỏng hiển nhiên | Vài phút |
| 2 | Test property-based: invariant trên đầu vào được sinh ra | Ca biên bạn không tưởng tượng nổi | Vài giờ |
| 3 | Test differential: so sánh với một implementation tham chiếu chậm nhưng đúng | Khác biệt tinh vi trong code đã tối ưu | Vài giờ |
| 4 | Test golden / replay: ghi lại đầu vào và đầu ra thật, diff mỗi lần thay đổi | Regression trong tính năng LLM, nơi không có một đáp án đúng duy nhất | Vài ngày |
| 5 | Review diff bởi con người với rubric viết sẵn | Cái thất bại mà test đã mã hóa là chấp nhận được | Luôn luôn |

Mức 4 là mức không ai dạy và mọi tính năng AI đều cần. Nếu sản phẩm của bạn gọi một model, bạn không thể khẳng định bằng nhau — bạn khẳng định *tính ổn định* và *các cận*.

### Công việc có agent hỗ trợ thực sự hỏng thế nào

| Thất bại | Nó trông như thế nào | Bạn phát hiện thế nào |
| --- | --- | --- |
| API bịa | Gọi đầy tự tin vào một method không tồn tại | Compile + type check, mọi lần |
| Sai âm thầm | Code chạy, đầu ra sai một cách tinh vi | Test khẳng định ngữ nghĩa, không phải hình dạng |
| Sửa quá rộng | Mười hai file bị đổi cho một sửa lỗi một dòng | Đọc toàn bộ diff trước khi chấp nhận |
| Chơi test | Agent sửa test cho khớp với bug | Review diff của test với cùng mức nghi ngờ như với source |
| Chỉ thị bị chèn | Một comment hoặc docstring trong repo lái agent | Coi nội dung repo là đầu vào không đáng tin |
| Chi phí chạy loạn | Vòng retry, context khổng lồ, không có ngân sách | Giới hạn cứng token/thời gian cho mỗi task |

Không cái nào trong số này là lạ. Chúng là bề mặt thất bại bình thường, và mỗi cái có một biện pháp đối phó rẻ. Học các biện pháp đó trước khi học các framework.

## Xương sống: một hệ thống, tiến hóa dần

Thay vì một danh sách chủ đề, hãy xây một hệ thống và liên tục làm nó khó hơn. Mỗi giai đoạn thêm một ràng buộc buộc bạn phải học lớp tiếp theo. Đây là cấu trúc duy nhất tạo ra chiều sâu mà không cần đề cương.

**Hệ thống:** một service nhỏ bạn sở hữu từ đầu đến cuối. Một URL shortener là đủ. Một pastebin là đủ. Điều quan trọng là bạn vận hành nó và nó có thể hỏng.

| Giai đoạn | Thời gian | Ràng buộc thêm vào | Bạn buộc phải học | Cột mốc dự án |
| --- | --- | --- | --- | --- |
| 1 | 4–6 tuần | Phải chạy từ command line, có test | Một ngôn ngữ cho tử tế, git, testing, xử lý lỗi | CLI tool, 80% test coverage, lịch sử sạch |
| 2 | 6–8 tuần | Phải phục vụ HTTP cho client thật | Mạng, ngữ nghĩa HTTP, statelessness, validate đầu vào | Server xử lý 1k req/s cục bộ |
| 3 | 8–10 tuần | Dữ liệu phải sống qua restart, và query phải nhanh | Database, index, query plan, transaction | Store bền vững với một index bạn giải thích được |
| 4 | 6–8 tuần | Phải xử lý người dùng đồng thời mà không làm hỏng dữ liệu | Concurrency, locking, isolation, idempotency | Load test tìm ra race condition của bạn |
| 5 | 6–8 tuần | Phải quan sát được và deploy được | Logging, metrics, tracing, CI/CD, container | Đã deploy, với dashboard bạn thực sự đọc |
| 6 | 6–8 tuần | Phải sống sót qua một sự cố | Phân tích thất bại, capacity, rollback, postmortem | Một incident report viết về chính lần sập của bạn |

Khoảng 9–12 tháng làm bán thời gian. Cuối cùng bạn có một hệ thống bạn hiểu tới tận các kiểu thất bại, thứ đáng giá hơn mười tutorial.

**Những gì cố tình chưa học:** nội thân Kubernetes, năm framework frontend, microservices pattern, blockchain, "AI agents" như một sản phẩm, ngôn ngữ mới nhất. Không cái nào là tiên quyết cho chiều sâu, và tất cả đều là chỗ ẩn náu thoải mái.

### Vì sao là xương sống chứ không phải danh sách chủ đề

Một danh sách chủ đề cho phép bạn học phần thú vị và bỏ qua phần đau. Một hệ thống áp đặt thứ tự: bạn không thể hiểu index trước khi query chậm, và không thể hiểu race condition trước khi có concurrency. Ràng buộc sinh ra chương trình học.

## Anki khớp ở đâu

| Làm thẻ cho nó | Đừng làm thẻ cho nó |
| --- | --- |
| Độ phức tạp của các thao tác có tên | Đánh đổi thiết kế |
| Field của protocol và thứ tự handshake | Quy trình debug |
| Ngữ nghĩa SQL (`NULL` trong aggregate, isolation level) | Trực giác tuning query |
| Lệnh git và tác dụng của chúng | Quyết định kiến trúc |
| Hành vi syscall và ý nghĩa errno | "Cách tổ chức một dự án" |
| Idiom ngôn ngữ lặp lại | Bất cứ thứ gì bạn chỉ tra một lần |

Ranh giới giống như `04`: **sự kiện ổn định, tùy ý, và cần nhớ nguội.** Mọi thứ ở cột phải được học bằng làm, ôn bằng viết, và giữ bằng dùng.

Một tín hiệu tốt cho thấy bạn làm thẻ đúng: deck lớn chậm và dự án của bạn khó dần. Tín hiệu xấu: deck lớn nhanh và dự án vẫn giữ nguyên quy mô.

## Bằng chứng năng lực năm 2026

| Tín hiệu năng lực | Nhiễu |
| --- | --- |
| Một hệ thống chạy được với ràng buộc thật (tải, thất bại, khối lượng dữ liệu) | Một bản clone của app trong tutorial |
| Một design document giải thích đánh đổi bạn thực sự đối mặt | Một danh sách 20 công nghệ trên CV |
| Một bài viết sự cố có root cause | Chồng chứng chỉ |
| Một PR open-source sống sót qua review | "Built a todo app in 5 frameworks" |
| Một benchmark bạn tự chạy, có phương pháp | Khẳng định hiệu năng mà không đo |
| Code mà người khác phải bảo trì | Code chỉ mình bạn đọc |

Sợi chỉ chung: **bằng chứng rằng có một thứ gì đó khó và bạn đã xử lý được nó.** Agent khiến việc tạo ra khối lượng trở nên dễ. Khối lượng giờ là tín hiệu rẻ nhất, nên nó đáng giá ít nhất.

## Rủi ro thật

**Trôi chảy nông.** Bạn có thể tạo ra phần mềm chạy được mà không hiểu nó. Nó qua test, ship, và hỏng ở quy mô lớn theo cách bạn không chẩn đoán nổi. Biện pháp đối phó là xương sống: vận hành một thứ gì đó, và để nó hỏng.

**Phụ thuộc.** Lần đầu bạn offline hoặc model sập, bạn sẽ biết mình thực sự biết gì. Giữ một kỹ năng không cần agent (`03`).

**Mù evaluation.** Nếu bạn không nói được đầu ra có đúng không, bạn không phải đang làm kỹ thuật, bạn đang đánh bạc. Dựng test trước khi dựng tính năng.

**Gu bị bào mòn.** Phán đoán thiết kế đến từ việc đã bảo trì code dở. Nếu bạn không bao giờ bảo trì thứ gì, bạn sẽ tiếp tục chọn phương án demo đẹp nhất.

Không cái nào trong số này được giải quyết bằng cách học chăm hơn. Chúng được giải quyết bằng cách sở hữu một thứ đủ lâu để nó trở nên đáng xấu hổ.

→ Tiếp: [08 — Tiếng Anh cho lập trình viên](08-english-for-developers.md)
