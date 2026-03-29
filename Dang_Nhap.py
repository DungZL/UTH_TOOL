from playwright.sync_api import sync_playwright
from Cau_Hinh import PORTAL, SESSION_FILE

def dang_nhap_va_luu_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(PORTAL)
        print("👉 Vui lòng đăng nhập tại trang Portal")

        print("⏳ Đang chờ đăng nhập thành công...")
        page.wait_for_url("**/dashboard**", timeout=0)

        context.storage_state(path=SESSION_FILE)
        print("✅ Đăng nhập thành công, đã lưu session")

        browser.close()
