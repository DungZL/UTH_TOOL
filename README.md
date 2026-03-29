UTH_TOOL
Giới thiệu

UTH_TOOL là phần mềm hỗ trợ theo dõi trạng thái học phần của sinh viên.
Công cụ giúp tự động kiểm tra tình trạng đăng ký học phần, đăng nhập hệ thống và thông báo khi có thay đổi.

UTH_TOOL is a tool for tracking course registration status.
It helps automatically log in, check course status, and notify when changes occur.

Chức năng chính
Đăng nhập hệ thống sinh viên
Kiểm tra tình trạng học phần
Theo dõi thay đổi học phần
Phát âm thanh thông báo khi có cập nhật
Menu điều khiển đơn giản

Main features:

Student system login
Check course status
Track course changes
Sound notification when updates occur
Simple menu interface
Cấu trúc thư mục
UTH_TOOL/
│
├── Cau_Hinh.py              # File cấu hình
├── Dang_Ky.py               # Xử lý đăng ký học phần
├── Dang_Nhap.py             # Xử lý đăng nhập
├── Menu.py                  # Menu chương trình
├── Playwright_Manager.py    # Điều khiển trình duyệt Playwright
├── tingting.wav             # Âm thanh thông báo
├── README.md
└── .gitignore
Cài đặt
1. Cài Python

Tải Python tại:
https://www.python.org/

2. Cài thư viện cần thiết
pip install playwright
pip install asyncio
3. Cài Playwright browser
playwright install
Cách chạy chương trình
python Menu.py
Lưu ý
Cập nhật tài khoản trong file Cau_Hinh.py
Không chia sẻ tài khoản sinh viên
Nên chạy tool trước thời gian đăng ký học phần
Tác giả

DungZL
