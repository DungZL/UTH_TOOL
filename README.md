# UTH_TOOL
> Tool theo dõi trạng thái đăng ký học phần – UTH **(ĐHGTVT-TPHCM)**

---
## 📌 Giới thiệu | Introduction
UTH_TOOL là phần mềm hỗ trợ theo dõi trạng thái đăng ký môn học phần cho sinh viên.  
Công cụ giúp tự động đăng nhập, kiểm tra tình trạng đăng ký học phần và thông báo khi có thay đổi.

---
## ⚙️ Chức năng | Features
- Đăng nhập hệ thống sinh viên
- Kiểm tra tình trạng học phần
- Theo dõi thay đổi học phần
- Phát âm thanh khi có cập nhật
- Menu điều khiển


---

## 📂 Cấu trúc thư mục | Project Structure
```bash
UTH_TOOL/
│
├── Cau_Hinh.py              # File cấu hình
├── Dang_Ky.py               # Xử lý đăng ký học phần
├── Dang_Nhap.py             # Xử lý đăng nhập
├── Menu.py                  # Menu chương trình
├── Playwright_Manager.py    # Điều khiển Playwright
├── tingting.wav             # Âm thanh thông báo
├── README.md
├── .gitignore
└── ...

```

## 📦 Requirements

Project này chỉ cần cài Playwright 
>Trường hợp đơn giản bạn có thể tải file .exe ở đường dẫn phía bên dưới

### Cài Playwright

```bash
pip install playwright
```

### Cài Browser cho Playwright (bắt buộc)

```bash
playwright install
```

Hoặc:

```bash
python -m playwright install
```

Nếu không chạy bước này chương trình sẽ lỗi khi mở trình duyệt.

---
## 🧠 Hướng dẫn sử dụng | Guide
Bạn có thể tải xuống bản .exe của tool qua đường dẫn **<text>**, chỉ cần click vào là khởi chạy
>Hoặc cài thủ công yêu cầu cài đặt playwright nếu bạn chưa cài đặt hãy xem hướng dẫn phía trên

Khởi chạy tệp Menu.py 
1. Đầu tiên bạn chọn đăng nhâ




