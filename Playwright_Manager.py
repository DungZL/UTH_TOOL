from playwright.sync_api import sync_playwright

_playwright = None
_browser = None

def get_browser():
    global _playwright, _browser

    if _browser:
        try:
            _browser.contexts
        except:
            reset_browser()

    if _playwright is None:
        _playwright = sync_playwright().start()

    if _browser is None:
        _browser = _playwright.chromium.launch(headless=False)

    return _browser


def reset_browser():
    global _playwright, _browser

    try:
        if _browser:
            _browser.close()
    except:
        pass

    try:
        if _playwright:
            _playwright.stop()
    except:
        pass

    _browser = None
    _playwright = None
