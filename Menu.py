import os
import sys
from Dang_Nhap import dang_nhap_va_luu_session
from Dang_Ky import mo_trang_dang_ky, kiem_tra_con_cho
from Cau_Hinh import SESSION_FILE
from Playwright_Manager import reset_browser

import Dang_Ky
if getattr(sys, 'frozen', False):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(
        sys._MEIPASS, "ms-playwright"
    )

def don_sach_he_thong(xoa_session=False):
    Dang_Ky.dk_page = None
    Dang_Ky.dk_context = None

    reset_browser()

    if xoa_session and os.path.exists(SESSION_FILE):
        try:
            os.remove(SESSION_FILE)
        except:
            pass

    print("🧹 Đã dọn sạch hệ thống")

def status_login():
    return "🟢 ĐÃ ĐĂNG NHẬP" if os.path.exists(SESSION_FILE) else "⚪ CHƯA ĐĂNG NHẬP"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def cho_quay_lai_menu():
    input("\n⏎ Nhấn Enter để quay lại menu...")

def status_login():
    return "🟢 ĐÃ ĐĂNG NHẬP" if os.path.exists(SESSION_FILE) else "⚪ CHƯA ĐĂNG NHẬP"


def menu_chinh():
    while True:
        clear()

        print(f"""
╔════════════════════════════════════════╗
║           🎓  UTH TOOL  🎓             ║
╠════════════════════════════════════════╣
║ Trạng thái: {status_login():<20}      ║
╠════════════════════════════════════════╣
║ 1  Đăng nhập hệ thống                  ║
║ 2  Mở trang đăng ký học phần           ║
║ 3  Theo dõi lớp học                    ║
║ 4  Dọn sạch (reset khẩn cấp)           ║
║ 0  Thoát                               ║
╚════════════════════════════════════════╝
""")

        chon = input("👉 Chọn chức năng: ").strip()

        if chon == "1":
            dang_nhap_va_luu_session()
            cho_quay_lai_menu()

        elif chon == "2":
            mo_trang_dang_ky()
            cho_quay_lai_menu()

        elif chon == "3":
            kiem_tra_con_cho()
            cho_quay_lai_menu()
        elif chon == "4":
            print("\n⚠️ DỌN SẠCH HỆ THỐNG")
            print("1️⃣  Chỉ reset tab & browser")
            print("2️⃣  Reset + xoá session (đăng nhập lại)")
            lua_chon = input("👉 Chọn: ").strip()

            if lua_chon == "2":
                don_sach_he_thong(xoa_session=True)
            else:
                don_sach_he_thong(xoa_session=False)

            cho_quay_lai_menu()

        elif chon == "0":
            print("👋 Thoát chương trình")
            break

        else:
            print("❌ Lựa chọn không hợp lệ")
            cho_quay_lai_menu()
            
if __name__ == "__main__":
    menu_chinh()
