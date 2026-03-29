# UTH_TOOL
Tool theo dõi trạng thái đăng ký học phần – UTH

UTH_TOOL is a tool for tracking course registration status. It helps automatically log in, check course status, and notify when changes occur.

---

## 📌 Giới thiệu | Introduction
**VI:**  
UTH_TOOL là phần mềm hỗ trợ theo dõi trạng thái học phần của sinh viên.  
Công cụ giúp tự động đăng nhập, kiểm tra tình trạng đăng ký học phần và thông báo khi có thay đổi.

**EN:**  
UTH_TOOL helps students monitor course registration status automatically by logging in, checking course availability, and sending notifications when changes occur.

---

## ⚙️ Chức năng | Features
- Đăng nhập hệ thống sinh viên
- Kiểm tra tình trạng học phần
- Theo dõi thay đổi học phần
- Phát âm thanh khi có cập nhật
- Menu điều khiển

**Main features:**
- Student system login
- Check course status
- Track course changes
- Sound notification when updates occur
- Simple menu interface

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
└── .gitignore
```
## 📦 Requirements

Project này chỉ cần cài Playwright.

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

## ⚙️ Quick Setup

```bash
git clone <repo_url>
cd UTH_TOOL
pip install -r requirements.txt
playwright install
python Menu.py
```

