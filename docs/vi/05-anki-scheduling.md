> Bản dịch tiếng Việt. Bản gốc là file tiếng Anh cùng tên — đó là bản đầy đủ và mới nhất.

# 05 — Lịch ôn Anki

Thiết kế thẻ là phần quan trọng. Lên lịch là phần dễ làm sai theo những cách khiến bạn mất hàng tháng.

Hai quy tắc trước mọi thứ khác:

1. **Bật FSRS.** Nó không phải mặc định, và đây là cải tiến lớn nhất so với scheduler cũ.
2. **Gần như không đổi gì khác.** Hầu hết mọi hướng dẫn cài đặt Anki bạn tìm được đều mô tả một scheduler bạn không chạy.

Ghi chú phiên bản: các chi tiết bên dưới phản ánh Anki 26.x (cuối 2026). Những khẳng định phụ thuộc phiên bản đều được gắn tag; hãy kiểm tra lại khi nâng cấp, vì đây là phần duy nhất trong repo này bị mục theo thời gian.

## FSRS vs SM-2

**SM-2** là scheduler cũ: một ease factor cho mỗi thẻ, nhân vào interval trước đó. Thất bại mang tính cấu trúc của nó là **ease hell** — trượt lặp đi lặp lại làm ease factor của một thẻ bị hạ vĩnh viễn, nên interval của nó mãi mãi ngắn, và bạn phản ứng bằng cách thêm learning steps, làm mọi thứ tệ hơn. `[strong]` cho phần mô tả cơ chế; khác biệt về kết quả được ghi nhận rõ trong chính manual của Anki.

**FSRS** là một mô hình quên được fit, với ba biến cho mỗi thẻ:

| Biến | Ý nghĩa |
| --- | --- |
| **D** — difficulty | Mục này khó với bạn đến mức nào |
| **S** — stability | Interval mà tại đó retrievability giảm còn 90% |
| **R** — retrievability | Xác suất bạn nhớ được nó ngay lúc này, tính từ thời gian đã trôi qua và S |

Một lần ôn cập nhật (D, S) từ điểm bạn chấm và độ trễ; interval tiếp theo là lúc R được dự đoán chạm desired retention của bạn. "Optimize" chạy gradient descent trên chính review log của bạn, nên các tham số mang tính cá nhân ngay từ cách dựng.

Nguồn gốc: Ye, Su & Cao, KDD '22 (`10.1145/3534678.3539081`), được hiện thực bằng Rust với tên `fsrs-rs`.

Hệ quả thực tế: **không có ease factor để mà mắc kẹt.** Đó là lý do những thang learning steps công phu người ta dựng để thoát ease hell giờ thành vô nghĩa — chúng vốn là giải pháp vòng cho một scheduler bạn không còn dùng.

## Nó có phải mặc định không?

Không. Tính đến Anki 26.x bạn vẫn phải bật nó một cách tường minh: *Deck options → FSRS → Enable FSRS*. Manual vẫn gọi nó là "an alternative to the legacy SM-2 algorithm", và issue theo dõi của maintainer "Make FSRS the default?" (#3616) vẫn còn mở tính đến cuối 2026.

Điều này quan trọng vì nhiều hướng dẫn hiện hành nói ngược lại. Nếu một hướng dẫn nói "FSRS đã là mặc định từ 23.10", nó sai, và phần còn lại của lời khuyên cài đặt trong đó cũng nhiều khả năng sai.

Dòng thời gian, để định hướng:

| Phiên bản | Thay đổi |
| --- | --- |
| 23.10 | FSRS được tích hợp (opt-in) |
| 25.07 | FSRS-6; "Compute minimum recommended retention" (CMRR) bị bỏ |
| 25.09 | Desired retention cấu hình được theo từng deck |
| 26.x | Cập nhật `fsrs-rs`, sửa lỗi cloze-inside-MathJax |

Việc bật là toàn cục — bạn không thể chạy FSRS trên một preset và SM-2 trên preset khác.

## Những cài đặt quan trọng

| Setting | Giá trị | Vì sao |
| --- | --- | --- |
| Desired retention | **0.90** | Cài đặt quan trọng nhất. Trên 90% khối lượng tăng dốc; trên 97% là không quản nổi |
| FSRS parameters | Optimize hằng tháng, không bao giờ sửa tay | Manual cấm chép tham số của người khác — chúng được fit cho trí nhớ của *bạn* |
| Learning steps | `10m` | Các step từ 1 ngày trở lên phản tác dụng dưới FSRS |
| Maximum interval | để mặc định | Hạ nó xuống chỉ làm tăng khối lượng |
| New cards/day | 10–20 | 20 thẻ mới/ngày hội tụ về ~200 lượt ôn/ngày. Đó là trần của một thói quen bền vững |
| Bury siblings | bật | Hai thẻ từ một note không bao giờ rơi vào cùng một ngày — bản sửa nhiễu rẻ nhất có sẵn |
| Easy days | một ngày nhẹ | Có sẵn từ 24.11, hoạt động với FSRS |
| Review order | ascending retrievability | Thay thế phù hợp với FSRS cho "relative overdueness" |
| Reschedule on change | tắt | Có thể xả ra một đống đến hạn khổng lồ cùng lúc |

Đó là toàn bộ cấu hình. Chín dòng.

## Phép tính đáng làm một lần

Interval tỉ lệ với `ln(desired retention)`. Vậy:

- 90% → 95% nhân interval với ≈0.49, tức là **gần như gấp đôi số lượt ôn**
- 90% → 85% nhân interval với ≈1.54, tức là **giảm khoảng một phần ba số lượt ôn**

Đường cong là lồi: vài điểm retention cuối cùng là những điểm đắt. Đó là lý do 0.90 là mặc định và lý do "tôi muốn 97%" là một quyết định sống cả đời trong màn hình ôn tập.

Quy tắc ngón tay cái: 0.90 bình thường; 0.85 nếu việc ôn đang chèn ép tài liệu mới; 0.93 chỉ cho deck gắn với một ngày thi.

## Cái gì là nhiễu

| Lời khuyên bạn sẽ gặp | Thực tế |
| --- | --- |
| "Use learning steps `1m 10m 1d 4d 10d`" | Một giải pháp vòng cho ease hell. Dưới FSRS, lặp lại một thẻ trong cùng một ngày gần như không đóng góp vào trí nhớ dài hạn |
| "Tune the maximum interval" | Không ai chạm tới trần đó. Chỉnh nó là sự trì hoãn |
| "Copy these FSRS parameters" | Manual cấm rõ ràng. Tham số là của riêng từng người |
| "Click Compute minimum recommended retention" | **Bị bỏ từ 25.07.** Hướng dẫn vẫn bảo bạn bấm |
| "You need 1,000 reviews before Optimize works" | Lỗi thời từ 24.06.3 |
| "Install FSRS Helper for X" | Phần lớn giờ đã có sẵn. Chính README của nó gọi nó là "an added bonus, not recommended for extensive use". Hai tính năng vẫn còn quan trọng: Disperse Siblings và Remedy Hard Misuse |
| "Tune easy bonus / interval modifier / hard interval" | Những thứ này **bị ẩn** dưới FSRS. Lời khuyên về chúng là lời khuyên về một scheduler bạn không chạy |

Nếu bạn đang dành thời gian cho bất kỳ dòng nào trong bảng đó, bạn không phải đang học.

## Một cấu hình cụ thể cho 30–60 phút/ngày

Một preset cho mỗi nhóm môn — `CS` và `English` — không phải mỗi chương. Preset theo chương là gánh nặng bảo trì mà không có lợi ích.

```
FSRS:              on, optimize monthly
Desired retention: 0.90
Learning steps:    10m
Max interval:      default
New cards/day:     15 (hard cap 20)
Review cap:        200
Bury siblings:     on
Easy days:         Sunday light
Reschedule:        off
Review order:      ascending retrievability
```

Hội tụ về khoảng 150 lượt ôn/ngày ≈ 15–20 phút với 6–8 giây mỗi thẻ, cộng 5–8 phút cho thẻ mới. Đó là ngân sách 30–60 phút trong
[`09-weekly-loop.md`](09-weekly-loop.md).

## Note types

| Loại | Dùng khi | Cái bẫy |
| --- | --- | --- |
| `Basic` | Một chiều là một nhiệm vụ truy xuất thật | — |
| `Basic (and reversed card)` | Cả hai chiều đều không mơ hồ (từ vựng L2↔L1) | Với sự kiện kỹ thuật, chiều đảo thường mơ hồ: "which algorithm is O(log n)?" có nhiều đáp án |
| `Basic (optional reversed card)` | Mặc định tốt nhất cho generator — việc đảo chiều là quyết định theo từng note | — |
| `Basic (type in the answer)` | Chuỗi chính xác quan trọng (flags, keywords) | Tốn thời gian gõ; dùng tiết kiệm |
| `Cloze` | Sự kiện sống trong một câu; các phép liệt kê | Không tạo được từ note type thường |
| `Image Occlusion` | Sơ đồ | Không liên quan với tài liệu dạng chữ |

## Những cái bẫy định dạng âm thầm làm hỏng thẻ

Những cái này đặc thù của Anki và tốn thời gian debug thật. Chúng thuộc về bước validation của bất kỳ generator nào (`06`).

| Cái bẫy | Triệu chứng | Cách sửa |
| --- | --- | --- |
| `<` thô trong field code | Chữ biến mất âm thầm — `<T>` bị parse như một HTML tag | Escape thành `&lt;T&gt;` |
| `}}` bên trong cloze | Cloze kết thúc sớm, render hỏng | Chèn khoảng trắng (`} }`) hoặc dùng `<!-- -->` |
| `::` bên trong chữ của cloze | Bị parse thành dấu phân cách cloze *hint* | `std:<!-- -->:variant` |
| `[$]...[/$]` | Cần cài LaTeX cục bộ, mặc định bị tắt, **hỏng âm thầm** | Dùng MathJax `\(...\)` |
| Tab bên trong một field TSV | Cột khi import bị lệch | Luôn dùng dấu cách để thụt lề |
| Dòng dài trong `<pre>` | Tràn ra ngoài màn hình | `white-space: pre-wrap` trong CSS của template |

MathJax và việc sinh ảnh LaTeX là hai cơ chế khác nhau và thường xuyên bị nhầm lẫn. MathJax (`\(...\)`) chạy phía client, không cần cài gì, và hoạt động trên mọi nền tảng. Sinh ảnh LaTeX (`[latex]...[/latex]`, `[$]...[/$]`) gọi ra một bản cài LaTeX cục bộ và ghi ra file PNG. Với mọi thứ tự động:
**chỉ xuất MathJax.**

## Cách biết lịch đang hoạt động

| Tín hiệu | Ý nghĩa |
| --- | --- |
| True retention 85–90% | Khỏe. Dưới 80%: quá nhiều thẻ mới, hoặc thẻ dở |
| Điểm chấm điển hình ~5–20% Again | Nếu bạn bấm Again thường xuyên hơn nhiều, thẻ sai, không phải kỷ luật của bạn |
| Thời gian ôn mỗi thẻ 6–8 s | Trung bình trên ~12 s là thẻ quá lớn |
| Leech < 5 trên 100 thẻ | Nhiều hơn nghĩa là vấn đề thiết kế thẻ |

Điều khiến người ta bất ngờ: dưới FSRS, tỉ lệ Again cao là một **chẩn đoán về thẻ**, không phải chẩn đoán về ý chí. Nếu bạn trượt một phần tư số lượt ôn, hãy sửa deck trước khi thêm kỷ luật.

→ Tiếp: [06 — Pipeline tạo deck bằng AI](06-ai-deck-pipeline.md)
