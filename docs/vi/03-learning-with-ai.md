> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# 03 — Học với AI

Phần lớn bài viết về chủ đề này hoặc là "AI sẽ thay thế việc học" hoặc là "AI chỉ là một công cụ". Cả hai đều vô dụng. Câu hỏi hữu ích hẹp hơn: **phần nào của vòng lặp học tập mà một agent có thể tiếp quản mà không làm gãy vòng lặp?**

Câu trả lời ngắn: agent rất giỏi ở feedback, giải thích theo yêu cầu, sinh tài liệu luyện tập, và làm critic. Chúng nguy hiểm ở đúng bước tạo ra trí nhớ bền — tự tạo ra câu trả lời.

## Bằng chứng gần đây thật sự cho thấy gì

| Nghiên cứu | Thiết kế | Phát hiện | Độ tin cậy |
| --- | --- | --- | --- |
| Kosmyna et al. (2025), MIT Media Lab, *Your Brain on ChatGPT* | 54 người tham gia, EEG, viết essay qua nhiều buổi; LLM vs search vs chỉ dùng não | Nhóm LLM cho thấy kết nối neural yếu nhất trong lúc viết và sau đó không trích dẫn được từ essay của chính mình. Khi nhóm LLM được chuyển sang chỉ dùng não ở một buổi sau, kết nối vẫn giảm | `[moderate]` — n nhỏ, preprint, một nhiệm vụ |
| Lee et al. (2025), Microsoft Research + CMU, CHI | Khảo sát 319 knowledge worker, 936 ví dụ | *Tự tin vào AI* cao hơn dự đoán ít tư duy phản biện hơn; *tự tin vào bản thân* cao hơn dự đoán nhiều hơn. Người ta offload suy nghĩ khi công cụ có cảm giác đáng tin | `[moderate]` — tự báo cáo |
| Bastani et al. (2024), Wharton | ~1.000 học sinh phổ thông, luyện toán | Gia sư GPT-4 cải thiện hiệu suất luyện tập khoảng ~48% nhưng học sinh làm **tệ hơn 17%** ở bài thi không có quyền truy cập. Biến thể đưa đáp án giúp luyện tập nhiều hơn và không giúp gì cho bài thi | `[moderate]` — thiết kế mạnh, lĩnh vực hẹp |
| Fan et al. (2025), BJET | Viết essay với ChatGPT vs chuyên gia vs không AI | Essay tốt hơn với AI, tự điều chỉnh yếu hơn, không có lợi thế ghi nhớ | `[moderate]` |
| Kestin et al. (2025), Harvard | AI tutor trong một khóa vật lý nhập môn | Gần như nhân đôi mức tiến bộ học tập trong ít thời gian hơn lớp active-learning | `[moderate]` — và đây là phản ví dụ |

Đọc cùng nhau, chúng không mâu thuẫn. Mẫu hình là:

- **AI giải thích và đặt câu hỏi, và giữ lại đáp án, thì giúp.**
- **AI trả lời theo yêu cầu cải thiện hiệu suất và làm suy giảm việc học.**
- **Sự suy giảm là vô hình ngay lúc đó** — bạn cảm thấy nhanh hơn và tốt hơn.

Cú tách 48% tốt hơn khi luyện / 17% tệ hơn khi thi của Bastani là phát biểu rõ nhất về vấn đề: chỉ số bạn nhìn thấy được cải thiện trong khi chỉ số bạn quan tâm lại giảm.

## Huyền thoại 2-sigma, vì mọi AI tutor đều bán nó

Bloom (1984) quan sát rằng dạy kèm một-một tạo ra kết quả cao hơn khoảng hai độ lệch chuẩn so với giảng dạy nhóm thông thường. Con số đơn lẻ đó là nền tảng marketing của toàn bộ ngành AI-tutoring, và nó yếu hơn vẻ ngoài của nó.

- Đó không phải một thí nghiệm. Đó là một phép ngoại suy trên vài nghiên cứu nhỏ, được ghép lại để lập luận cho một chương trình nghiên cứu.
- Các meta-analysis về dạy kèm bởi người thật tìm thấy hiệu ứng nhỏ hơn nhiều — khoảng d ≈ 0,4–0,8 tùy bạn so với cái gì, không phải 2,0. `[strong]`
- **Không hệ thống AI nào đã tái tạo được 2σ trên một phép đo được kiểm soát tốt.** "Nhân đôi mức tiến bộ" của Kestin khớp với d ≈ 0,5–0,9. Rất tốt — và bằng một phần ba trần được tuyên bố.

Hệ quả thực dụng: hãy chờ đợi một cải thiện vừa phải nhưng thật từ một AI tutor được thiết kế tốt, và cảnh giác với bất kỳ sản phẩm nào trích dẫn 2σ. Dù sao thì effect size không phải điểm chính; thiết kế tạo ra nó mới là điểm chính. Gia sư giúp khi chúng giữ lại đáp án, yêu cầu giải thích, và đưa feedback — tất cả những thứ `04` và `09` đưa vào vòng lặp.

## Cơ chế: offloading, không phải lười

Cognitive offloading (Risko & Gilbert, 2016) là chiến lược bình thường của con người khi chuyển công việc trí óc sang môi trường — viết danh sách đi chợ, dùng máy tính bỏ túi. Đó không phải một thất bại đạo đức, và nó thường là thích nghi.

Vấn đề là **retrieval và generation chính là các sự kiện học tập**. Nếu agent tạo ra, agent học. Không có sự chuyển lợi ích ngược lại cho bạn, theo cách có với máy tính bỏ túi, vì máy tính bỏ túi vốn không được cho là sẽ thay đổi khả năng số học của bạn.

Hai mất mát cụ thể:

**Generation effect.** Tài liệu bạn tự tạo ra được nhớ tốt hơn tài liệu bạn đọc (Slamecka & Graf 1978; meta-analysis của Bertsch et al. 2007 `[strong]`). Lời giải thích của agent là tài liệu đọc. Đây là lý do "giải thích cho tôi nghe" cho cảm giác rất hay và dạy được rất ít, và lý do "giải thích lại cho tôi và tôi sẽ nói chỗ nào sai" thì hiệu quả.

**Độ chính xác metacognitive.** Bạn không thể cảm nhận được khác biệt giữa hiểu và nhận ra. Đọc lại khai thác điều này; AI khai thác nó mạnh hơn, vì output trôi chảy, tự tin, và thường đúng. Tín hiệu lỗi của bạn — thứ bảo bạn quay lại học — không bao giờ kích hoạt.

## Những gì agent thật sự giỏi

Dùng chúng ở đây mà không thấy tội lỗi:

1. **Feedback tức thời, cụ thể.** Nút thắt trong deliberate practice là độ trễ của feedback. Một reviewer trả lời trong mười giây đánh bại một người trả lời trong một tuần. Đây là nguồn gốc của kết quả Harvard.
2. **Giải thích cùng một thứ theo bốn cách.** Một gia sư người giỏi làm được điều này; một quyển sách giáo khoa thì không. Yêu cầu cùng một khái niệm ở ba mức trừu tượng là hợp lý và rẻ.
3. **Sinh các bài luyện và câu hỏi đối kháng.** "Cho tôi năm bài trông giống binary search nhưng không phải" là một cách dùng thật.
4. **Làm critic, không phải tác giả.** "Đây là lời giải thích của tôi — tìm chỗ hổng" giữ được generation effect vì *bạn* đã tạo ra trước.
5. **Lên lịch và sổ sách.** Tối ưu FSRS, vệ sinh deck, phát hiện trùng lặp. Thuần overhead, không có giá trị học tập khi tự làm bằng tay.
6. **Đọc thứ bạn chưa đọc được.** Bài báo dày đặc, codebase lạ. Hợp lý, miễn là sau đó bạn tự tái dựng lập luận.

## Những gì agent dở

1. **Trả lời câu hỏi của bạn trước khi bạn thử.** Sai lầm tốn kém nhất, và là hành vi mặc định của mọi giao diện chat.
2. **Nói bạn nên học gì tiếp theo.** Chúng sẽ vui vẻ tạo ra một curriculum 14 giai đoạn. Nó sẽ nghe hợp lý, chung chung, và không khớp với cái bạn thật sự chưa làm được.
3. **Đánh giá năng lực của bạn.** Output trôi chảy không có nghĩa là bạn có kỹ năng. Chỉ một lần truy xuất lạnh hoặc một project thật mới nói được điều đó.
4. **Bất cứ thứ gì mà sai một cách tinh vi thì đắt.** API bịa ra, cú pháp deprecated được trình bày như hiện hành, trích dẫn bịa. Tỷ lệ lỗi đủ thấp để được tin và đủ cao để gây hại.

## Giao thức

Sáu quy tắc. Chúng vừa trên một thẻ.

1. **Thử trước khi hỏi.** Viết câu trả lời, phỏng đoán, đoạn code hỏng của bạn trước. Kể cả một lần thử sai cũng thay đổi tác dụng của lời giải thích lên bạn.
2. **Xin câu hỏi, không xin đáp án.** "Tôi nên trả lời được gì về X?" tốt hơn "giải thích X".
3. **Biến agent thành critic.** Dán lời giải thích, lời giải, thiết kế của bạn. Hỏi cái gì sai, không phải cái gì đúng.
4. **Không bao giờ chấp nhận một fact bạn không tìm được nguồn.** Nếu nó đáng để nhớ thì nó đáng để kiểm chứng với một nguồn gốc — man page, spec, một bài báo.
5. **Tự đóng vòng lặp bằng tay.** Bất cứ thứ gì agent tạo ra, hãy tái tạo nó từ trí nhớ một lần. Việc tái tạo chính là sự kiện học tập.
6. **Giữ một thứ không có agent.** Chọn kỹ năng bạn muốn sở hữu nhất và không bao giờ giao nó đi, kể cả vì tiện. Với một sinh viên CS, đó thường là debugging và system design.

Phép thử xem bạn có đang dùng AI tốt không không phải "nó có giúp tôi xong việc không". Mà là **"tháng sau tôi có làm được việc này mà không có nó không?"** Nếu câu trả lời vẫn là không trong nhiều tháng, công cụ đó không đang tăng cường bạn, nó đang thay thế bạn.

## Phần không thoải mái

Kết quả của MIT và CMU chỉ vào một thứ tệ hơn mất kỹ năng: sự mất mát không được cảm nhận. Người tham gia ở điều kiện LLM không báo cáo là mình tệ đi. Họ báo cáo nhiệm vụ dễ hơn. Đó là định nghĩa của một vòng lặp feedback xấu — cái giá bị trả sau và vô hình, còn lợi ích thì tức thời.

Cách phòng vệ duy nhất là cấu trúc, không phải động lực: những quy tắc buộc phải tạo ra trước khi tiêu thụ, được xây vào thói quen để chúng không phụ thuộc vào ý chí của bạn vào một ngày tồi tệ. Đó là việc của [`09-weekly-loop.md`](09-weekly-loop.md).

## Dùng AI cho Anki, cụ thể

Đây là phần người ta làm sai nhiều nhất, nên nó có tài liệu riêng: [`06-ai-deck-pipeline.md`](06-ai-deck-pipeline.md). Bản ngắn — agent giỏi ở việc *tìm các fact ứng viên và phác thảo prompt*, và dở ở việc *quyết định cái gì đáng nhớ* và ở việc *không bịa*. Vậy pipeline là: agent phác thảo, người chọn, agent audit các lỗi máy móc, người kiểm tra ngẫu nhiên.

→ Tiếp: [04 — Thiết kế thẻ Anki](04-anki-card-design.md)
