from Cau_Hinh import DANG_KY_HP, SESSION_FILE
from Playwright_Manager import get_browser
import os
import time
import random
import winsound

dk_context = None
dk_page = None

def page_con_song(page):
    try:
        page.title()
        return True
    except:
        return False


# ================== MỞ TAB ĐĂNG KÝ ==================
def mo_trang_dang_ky():
    global dk_context, dk_page

    if not os.path.exists(SESSION_FILE):
        print("❌ Chưa đăng nhập")
        return

    # ✅ Nếu tab đã tồn tại và chưa bị đóng → dùng lại
    if dk_page and not dk_page.is_closed():
        print("⚠️ Tab đăng ký học phần đã mở sẵn, không mở thêm")
        dk_page.bring_to_front()
        return

    # ♻️ Nếu chưa có hoặc đã bị đóng → tạo lại
    browser = get_browser()
    dk_context = browser.new_context(storage_state=SESSION_FILE)
    dk_page = dk_context.new_page()
    dk_page.goto(DANG_KY_HP)

    print("🌐 Đã mở tab đăng ký học phần")



# ================== KIỂM TRA TỒN TẠI ==================
def hoc_phan_ton_tai(ma_hp):
    row = dk_page.locator(
        f'xpath=//tr[.//td[3]//p[text()="{ma_hp}"]]'
    )
    return row.count() > 0


def lop_ton_tai(ma_lop):
    rows = dk_page.locator("tr.MuiTableRow-root")
    for i in range(rows.count()):
        if ma_lop in rows.nth(i).inner_text():
            return True
    return False


# ================== THEO DÕI LỚP ==================
def kiem_tra_con_cho():
    global dk_page, dk_context

    # ✅ Check sống/chết THẬT
    if dk_page is None or not page_con_song(dk_page):
        dk_page = None
        dk_context = None
        print("❌ Chưa mở tab đăng ký để theo dõi")
        return

    try:
        dk_page.wait_for_selector(
            'text=Lớp học phần đang chờ đăng ký',
            timeout=15000
        )
    except:
        # ⚠️ Check lại lần nữa để phân biệt CHẾT hay CHƯA CHỌN MÔN
        if not page_con_song(dk_page):
            dk_page = None
            dk_context = None
            print("❌ Chưa mở tab đăng ký để theo dõi")
            return

        print("⚠️ Chưa thấy danh sách lớp. Hãy bấm chọn môn học trước.")
        return


    ma_hp_chinh = input("👉 Nhập MÃ HỌC PHẦN CHÍNH: ").strip()
    ma_hp_trao_doi = input("👉 Nhập MÃ HỌC PHẦN TRÁO ĐỔI: ").strip()
    ma_lop = input("👉 Nhập MÃ LỚP HỌC PHẦN: ").strip()

    if not hoc_phan_ton_tai(ma_hp_chinh):
        print(f"❌ Không tìm thấy học phần CHÍNH: {ma_hp_chinh}")
        return

    if not hoc_phan_ton_tai(ma_hp_trao_doi):
        print(f"❌ Không tìm thấy học phần TRÁO ĐỔI: {ma_hp_trao_doi}")
        return

    if not lop_ton_tai(ma_lop):
        print(f"❌ Không tìm thấy LỚP HỌC PHẦN: {ma_lop}")
        return


    def click_hoc_phan(ma_hp):
        dk_page.locator(
            f'xpath=//tr[.//td[3]//p[text()="{ma_hp}"]]'
        ).click()
        print(f"🔁 Click học phần {ma_hp}")


    def lay_percent(ma_lop):
        rows = dk_page.locator("tr.MuiTableRow-root")
        for i in range(rows.count()):
            r = rows.nth(i)
            if ma_lop in r.inner_text():
                try:
                    text = r.locator(".MuiTypography-caption").inner_text()
                    return int(text.replace("%", "").strip())
                except:
                    return None
        return None


    print("\n🚀 Bắt đầu theo dõi lớp học")
    print("⛔ Nhấn Ctrl + C để dừng\n")

    try:
        while True:
            click_hoc_phan(ma_hp_chinh)
            time.sleep(random.randint(2, 8))

            click_hoc_phan(ma_hp_trao_doi)
            time.sleep(random.randint(2, 8))

            click_hoc_phan(ma_hp_chinh)
            time.sleep(2)

            percent = lay_percent(ma_lop)
            if percent is not None:
                print(f"📊 {ma_lop}: {percent}%")
                if percent < 100:
                    print("🚨 CÓ CHỖ !!!")
                    winsound.PlaySound("tingting.wav", winsound.SND_FILENAME)

    except KeyboardInterrupt:
        print("\n🛑 Đã dừng theo dõi")
