> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# learn-loop

Một knowledge base nhỏ, có quan điểm rõ ràng về **cách học** — dành cho một sinh viên CS phải sống sót trong thị trường việc làm đã có AI agent, nhớ được những gì mình học, và làm tất cả bằng tiếng Anh.

Không phải một khóa học. Không phải một hệ thống năng suất. Một tài liệu tham chiếu bạn đọc một lần, rồi để mở trong lúc học.

---

## Vì sao có repo này

Ba thứ thay đổi cùng lúc:

1. **Generative AI xóa bỏ cái giá của việc không biết** — bạn tra bất kỳ cú pháp nào trong bốn giây. Điều đó làm *việc ghi nhớ* có cảm giác là tùy chọn, và hầu hết mọi người lặng lẽ ngừng xây kiến thức bền.
2. **Bằng chứng về học tập đã ổn định suốt hai mươi năm** và vẫn bị phần lớn lời khuyên học tập trên mạng phớt lờ, vì những lời khuyên đó tối ưu cho *cảm giác* học chứ không phải *sự thật* là đã học.
3. **Spaced repetition là đòn bẩy duy nhất có hiệu ứng lớn và được lặp lại** — nhưng cũng là thứ dễ bị phá nhất. Một deck toàn thẻ tệ còn tệ hơn không có deck, vì nó đốt những fact sai vào trí nhớ theo lịch.

Vậy mục tiêu hẹp: giữ những phương pháp hiệu quả, bỏ những phương pháp không, và dùng Anki theo cách tạo ra những thẻ đáng ôn lại sau hai năm.

## Dành cho ai

Một sinh viên IT người Việt (tôi) mà:

- muốn sâu ở vài lĩnh vực, không phải rộng ở hai mươi lĩnh vực;
- đọc tiếng Anh thoải mái nhưng muốn luyện thêm;
- dùng AI agent hằng ngày và không muốn kỹ năng của chính mình teo đi;
- sau này sẽ đưa repo này cho một agent để sinh tài liệu học và flashcard.

Nếu bạn không phải người đó, phần phương pháp vẫn dùng được. Phần Anki và tiếng Anh giả định người đọc có nền kỹ thuật.

---

## Đọc theo thứ tự này

| # | Tài liệu | Trả lời câu hỏi | Đọc khi nào |
| :-: | --- | --- | --- |
| 01 | [Cái gì vẫn còn hiệu quả](docs/vi/01-what-works.md) | Phương pháp nào có bằng chứng thật đằng sau | Đầu tiên. Mọi thứ khác giả định bạn đã đọc cái này |
| 02 | [Cái gì đã lỗi thời](docs/vi/02-what-is-outdated.md) | Phương pháp phổ biến nào là lãng phí thời gian | Ngay sau 01, để bỏ đi những thứ đã học sai |
| 03 | [Học với AI](docs/vi/03-learning-with-ai.md) | Agent giúp thế nào và âm thầm làm bạn tệ đi thế nào | Trước khi bạn xây thói quen học bằng AI |
| 04 | [Thiết kế thẻ Anki](docs/vi/04-anki-card-design.md) | Điều gì làm một thẻ tốt và một thẻ vô dụng | Trước deck thật đầu tiên |
| 05 | [Lịch ôn Anki](docs/vi/05-anki-scheduling.md) | FSRS, các cài đặt, và cái gì thật sự chỉ là nhiễu | Khi bạn đã có 200+ thẻ |
| 06 | [Pipeline deck bằng AI](docs/vi/06-ai-deck-pipeline.md) | Agent nên sinh và audit deck thế nào | Khi bạn tự động hóa việc làm thẻ |
| 07 | [Lộ trình CS](docs/vi/07-cs-roadmap.md) | Học gì, theo thứ tự nào, trong thời đại AI | Khi lập kế hoạch một học kỳ |
| 08 | [Tiếng Anh cho developer](docs/vi/08-english-for-developers.md) | Làm sao để thật sự giỏi tiếng Anh lên | Liên tục, cường độ thấp |
| 09 | [Vòng lặp hằng tuần](docs/vi/09-weekly-loop.md) | Một hệ thống tối giản vừa với một tuần thật | Nếu chỉ đọc một tài liệu, đọc cái này |
| 10 | [Nguồn](docs/10-sources.md) | Mọi trích dẫn, kèm link | Khi bạn muốn kiểm tra một khẳng định |

Trang nguồn (10) chỉ có tiếng Anh vì nó chỉ gồm link và DOI.

Tài liệu hỗ trợ:

- [`templates/concept-note.md`](templates/concept-note.md) — định dạng note, đồng thời là input để sinh thẻ.
- [`templates/card-quality-checklist.md`](templates/card-quality-checklist.md) — 15 mục kiểm tra đạt/không đạt cho một thẻ.
- [`data/deck-schema.md`](data/deck-schema.md) — định dạng TSV + manifest, kèm định nghĩa chính xác của `front_hash`.
- [`data/validate_deck.py`](data/validate_deck.py) — validator cấu trúc. Chạy trước khi commit một deck; nó bắt những lỗi làm hỏng lúc import.
- [`AGENTS.md`](AGENTS.md) — hợp đồng cho các AI agent đọc repo này.

---

## Các quy tắc repo này theo (KISS)

1. **Một ý mỗi file.** Nếu một tài liệu cần mục lục, nó nên là hai tài liệu.
2. **Mọi khẳng định đều có tag.** `[strong]` = meta-analysis hoặc đã được lặp lại. `[moderate]` = một nghiên cứu tốt. `[practice]` = ý kiến. Không có tag nghĩa là ý kiến.
3. **Không phương pháp nào được khuyên mà không kèm failure mode.** "Dùng spaced repetition" là thiếu; "spaced repetition hỏng khi thẻ không atomic" mới là phiên bản hữu ích.
4. **Tiếng Anh là bản chuẩn.** Các bản tiếng Việt nằm trong `docs/vi/` và `README.vi.md`. Chúng tồn tại để đọc thoải mái, không phải nguồn sự thật thứ hai.
5. **Agent chỉ đọc bản tiếng Anh.** Xem ghi chú về token bên dưới.
6. **Ở đây không có gì là một hệ thống năng suất.** Nếu một quy tắc không sống nổi qua một tuần tồi tệ, nó không có trong đây.
7. **Deck là data, không phải văn xuôi.** Thẻ nằm trong TSV + manifest để có thể audit, sinh lại, và diff.

---

## Dùng Anki với repo này (bắt đầu nhanh)

1. Đọc `docs/04-anki-card-design.md` một lần. Đó là phần duy nhất bạn không được đọc lướt.
2. Cài Anki, bật FSRS, đặt desired retention khoảng ~0.90. Bỏ qua mọi cài đặt khác trong lúc này (`docs/05-anki-scheduling.md`).
3. Viết thẻ bằng tay trong tháng đầu. Thẻ viết tay dạy bạn một thẻ tốt có cảm giác thế nào; thẻ do AI sinh thì không.
4. Khi bạn đã biết hình dạng của một thẻ tốt, dùng `docs/06-ai-deck-pipeline.md` để tự động hóa nửa nhàm chán.
5. Ôn hằng ngày, khoảng ~15–25 phút. Nếu một buổi kéo dài, bạn có quá nhiều thẻ mới, chứ không phải thiếu kỷ luật.

---

## Dành cho AI agent

Đọc [`AGENTS.md`](AGENTS.md) trước — nó ngắn và sẽ tiết kiệm token cho bạn.

Một điều đáng nhắc lại ở đây: **this repo is English-first. Do not read `README.vi.md` or anything under `docs/vi/`.** Đây là bản tiếng Việt để người đọc là chủ repo đọc cho thoải mái. Chúng không chứa thông tin nào mà bản tiếng Anh thiếu, nên đọc chúng chỉ làm chi phí token tăng gấp đôi mà không được gì. Nếu bạn là agent và bạn đã mở một file trong `vi/`, hãy đóng nó lại và mở file tiếng Anh tương ứng.

---

## Cái này không phải là gì

- Không phải lời khuyên y tế hay lâm sàng. Phần về giấc ngủ và vận động nói về hiệu suất học tập, không phải điều trị.
- Không khẳng định những phương pháp này hiệu quả y hệt nhau với mọi người. Effect size là số trung bình; phương sai của bạn là của riêng bạn.
- Không phải bản hoàn chỉnh. Các tag bằng chứng và những khẳng định về công cụ có phiên bản sẽ được kiểm tra lại; phần còn lại đủ ổn định để yên.

## Trạng thái

Bắt đầu 2026-11. Nội dung là sự tổng hợp của nghiên cứu đã công bố cộng với thực hành. Chỗ nào hai bên mâu thuẫn, tài liệu nói rõ. Nếu bạn thấy một khẳng định sai hoặc lỗi thời, cách sửa là một dòng sửa và một nguồn trong `docs/10-sources.md`.

## Tiếng Việt

Bản tiếng Việt: [`README.vi.md`](README.vi.md) và thư mục [`docs/vi/`](docs/vi/).
Bản tiếng Anh là bản gốc và đầy đủ nhất.

## License

MIT. Dùng đi, fork đi, đưa cho agent của bạn.
