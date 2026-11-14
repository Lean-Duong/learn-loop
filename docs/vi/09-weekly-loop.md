> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# 09 — Vòng lặp hằng tuần

Nếu chỉ đọc một tài liệu trong repo này, hãy đọc tài liệu này. Phần còn lại là lý lẽ biện minh.

Ràng buộc thiết kế là đời thật: lịch học, một việc làm bán thời gian, gia đình, và sự thật rằng động lực không phải một đầu vào ổn định. Một hệ thống cần một tuần tốt đẹp thì không phải một hệ thống.

Nên: **một vòng lặp, một deck, một dự án, một cuốn sách.** Mọi thứ khác là tùy chọn.

## Vòng lặp

```
   read / watch  ──►  attempt by hand  ──►  card the gaps  ──►  review daily
        ▲                                                        │
        └────────────────────────────────────────────────────────┘
```

Bốn bước. Bước người ta bỏ qua là bước hai, và đó là bước duy nhất nơi việc học xảy ra.

1. **Đọc** một thứ cho tử tế (không phải năm thứ hời hợt).
2. **Thử** — đóng nguồn lại, viết code, trả lời câu hỏi, vẽ sơ đồ. Dở cũng được. Đây là sự kiện sản sinh.
3. **Làm thẻ cho các lỗ hổng** — chỉ những thứ bạn trượt khi truy xuất, và chỉ khi chúng là những đơn vị truy xuất đơn lẻ (`04`).
4. **Ôn** — hằng ngày, chỉ thẻ đến hạn, 10–20 phút.

## Khối hằng ngày (45–75 phút)

| Phút | Hoạt động | Ghi chú |
| --- | --- | --- |
| 10–15 | Anki, chỉ thẻ đến hạn | Không bao giờ thêm thẻ mới ở đây; thẻ mới là quyết định hằng tuần |
| 30–45 | Deep work trên dự án hoặc chủ đề hiện tại | Một thứ. Không chuyển tab |
| 5–10 | Thử từ trí nhớ | Đóng mọi thứ và tái tạo lại thứ bạn vừa học |
| 5 | Anki tiếng Anh | Deck riêng, cloze trên collocation |

Thứ tự quan trọng hơn thời lượng: **ôn trước**, vì đó là thứ bạn sẽ bỏ nếu nó đến cuối, và vì nó mồi sẵn chủ đề bạn sắp làm.

## Khối hằng tuần (90–120 phút, một lần ngồi)

1. **Chọn một chủ đề cho tuần sau** (10 phút). Một. Không phải ba.
2. **Viết tay 10–20 thẻ mới** từ tài liệu của tuần này (30 phút). Viết tay, không sinh
   tự động — ít nhất trong những tháng đầu.
3. **Kiểm toán deck** (15 phút): xóa leech, tách thẻ nhiều sự kiện, sửa ngữ cảnh mồ
   côi. Chạy
   [`templates/card-quality-checklist.md`](../../templates/card-quality-checklist.md).
4. **Bộ luyện tập đan xen** (30 phút): 6–8 bài từ những chủ đề *khác nhau* trong quá
   khứ, chọn sao cho bạn không đoán được thể loại từ tiêu đề.
5. **Viết 5 dòng tiếng Anh** về thứ bạn đã học (10 phút). Một commit message, một ghi
   chú, bất cứ thứ gì thật.

Đó là toàn bộ hệ thống. Hai giờ mỗi tuần có cấu trúc có chủ đích cộng một giờ mỗi ngày.

## Khối hằng tháng (45 phút)

- Đọc lại ghi chú của chính bạn trong tháng. Thứ gì bạn không dựng lại được là một lỗ hổng — hoặc làm thẻ cho nó, hoặc xóa ghi chú đó.
- Kiểm tra sức khỏe deck: tỉ lệ retention, số leech, các thẻ có `lifecycle::ephemeral` đã hết hạn.
- Giết một thứ. Một chủ đề, một gói subscription, một side project. Chiều sâu đòi phải trừ bớt, và không có gì khác cưỡng chế được điều đó.

## Ngân sách thời gian

| Lớp | Mỗi tuần | Nó mua được gì |
| --- | --- | --- |
| Vòng lặp hằng ngày | ~7 h | Mức sàn. Không có nó thì mọi thứ khác vô nghĩa |
| Khối hằng tuần | ~2 h | Chất lượng deck và đan xen — hai thứ âm thầm xuống cấp |
| Khối hằng tháng | ~45 phút | Tỉa gọn |
| **Tổng** | **~10 h** | Một học kỳ tiến bộ thật song song với việc học trên trường |

Nếu bạn có dưới 7 giờ một tuần, hãy cắt khối hằng tuần xuống 45 phút trước khi cắt việc ôn hằng ngày. Ôn mới là phần tích lũy.

## Giao thức cho tuần tồi

Có những tuần bạn chỉ có tổng cộng 20 phút. Làm đúng thế này, theo đúng thứ tự này, và không làm gì khác:

1. **Thẻ đến hạn trên Anki.** 10 phút. Kể cả ngày tệ nhất.
2. **Một lần thử từ trí nhớ** về bất cứ thứ gì bạn học gần đây. 5 phút.
3. Dừng.

Đừng "đuổi kịp" sau đó. Đuổi kịp nghĩa là gấp đôi hàng đợi ôn, thứ sinh ra một ngày 200 thẻ, thứ sinh ra một tuần bị bỏ, thứ sinh ra việc bỏ hẳn. Hãy để tồn đọng là tồn đọng; FSRS sẽ dàn nó ra. Thất bại không thể cứu duy nhất là dừng việc ôn hoàn toàn.

## Cắt gì, theo thứ tự nào

Khi hệ thống quá nặng:

1. Cắt phần shadowing tiếng Anh (lợi nhuận biên thấp nhất).
2. Cắt bộ luyện tập đan xen hằng tuần xuống 4 bài.
3. Cắt thẻ mới về zero trong một tuần (vẫn ôn).
4. Cắt dự án về mức bảo trì.
5. **Không bao giờ** cắt việc ôn hằng ngày. Đó là thứ duy nhất tích lũy.

## Những chỉ số đáng theo dõi

| Chỉ số | Khỏe | Ý nghĩa khi nó lệch |
| --- | --- | --- |
| True retention (FSRS) | 85–90% | Dưới 80%: quá nhiều thẻ mới, hoặc thẻ dở |
| Leech trên 100 thẻ | < 5 | Cao: vấn đề thiết kế thẻ, không phải kỷ luật |
| Số thẻ thêm mỗi tuần | 10–25 | Cao hơn: bạn đang làm thẻ thay vì học |
| Số ngày có ôn | 6–7 / tuần | Dưới 5: vòng lặp đã gãy, sửa cái cò chứ đừng sửa ý chí |
| Số bài giải được mà không cần xem | tăng dần | Chỉ số duy nhất phản ánh kỹ năng thật |

Số lượng thẻ không phải chỉ số. Kích thước deck không phải thành tích. Một deck 5.000 thẻ ôn dở tệ còn tệ hơn một deck 400 thẻ bạn thực sự biết.

## Vì sao hình dạng này

Mỗi thành phần ánh xạ tới bằng chứng trong `01`:

- **Ôn hằng ngày** — spaced repetition, hiệu ứng lớn và đáng tin cậy duy nhất.
- **Thử từ trí nhớ** — retrieval practice, hiệu ứng còn lại.
- **Bộ đan xen hằng tuần** — kỹ thuật mà Anki không thể cho bạn.
- **Thẻ viết tay** — generation effect; bạn học tài liệu trong lúc viết thẻ.
- **Tỉa gọn hằng tháng** — giữ deck khỏi trở thành một nghĩa vụ bạn căm ghét.

Không có gì ở đây mới lạ. Đó chính là điểm. Một hệ thống bạn theo hai năm đánh bại một hệ thống tối ưu bạn theo ba tuần.

→ Tiếp: [10 — Nguồn tham khảo](../10-sources.md)
