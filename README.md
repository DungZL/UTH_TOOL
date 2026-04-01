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
Bạn có thể tải xuống bản .exe của tool qua đường dẫn **https://drive.google.com/file/d/1buJxUy6IqXbJrHJxVRgebYtZ-N8SSUKo/view?usp=drive_link**, chỉ cần click vào là khởi chạy
>Hoặc cài thủ công yêu cầu cài đặt playwright nếu bạn chưa cài đặt hãy xem hướng dẫn phía trên

Riêng nếu bạn cài thủ công thì khởi chạy tệp Menu.py 
1. Đầu tiên bạn chọn *đăng nhập hệ thống* điền thông tin tài khoản mật khẩu của bạn
2. Chọn mở trang *đăng ký học phần*
   > Hãy chọn học kỳ muốn theo dõi, và click chọn vào môn học muốn theo dõi nếu không hệ thống sẽ không tìm thấy lớp học phần
4. Chọn *theo dõi lớp học* chỉ khi nào bạn mở trang đăng ký học phần mới có thể chọn theo dõi lớp học
5. Điền thông tin học phần muốn theo dõi và học phần thay thế ( Học phần thay thế chỉ để hệ thông có thể auto chuyển đổi qua lại)
6. Chạy và chờ kết quả nếu hệ thống sẽ có thông báo nếu lớp học phần có chỗ trống

- Nếu xảy ra lỗi chỉ cần thoát ứng dụng hoặc chọn reset khẩn cấp, trong thời gian dài có thể chọn xoá sesion để tránh bị hết hạn đăng nhập

## 👨‍💻 Tác giả

**DUNGZL**

* 🚀 Project: UTH Tool
