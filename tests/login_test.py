from playwright.sync_api import sync_playwright
from pathlib import Path


def test_login_with_waits():
    """Deterministic login test using local HTML fixtures and Playwright waits.

    This test demonstrates proper waits, try/finally cleanup and headless mode.
    """
    login_file = Path(__file__).parent.parent / "testdata" / "login.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(login_file.as_uri())

            # Fill and submit the form
            page.fill("#username", "user1")
            page.fill("#password", "pass1")
            page.click("button[type=submit]")

            # Wait for navigation to the dashboard and for the welcome message
            page.wait_for_url("**/dashboard.html", timeout=5000)
            page.locator(".welcome-message").wait_for(timeout=5000)

            text = page.locator(".welcome-message").inner_text()
            assert "Welcome" in text
        finally:
            context.close()
            browser.close()
