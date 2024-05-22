import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/microsoft/vscode/issues")
    page.get_by_role("button", name="Search or jump to...").click()
    page.get_by_label("Clear", exact=True).click()
    page.get_by_role("combobox", name="Search").fill("bug")
    page.get_by_role("combobox", name="Search").press("Enter")
    # expect("qbsearch-input").to_contain_text("bug")
    order = expect(page.locator("qbsearch-input")).to_contain_text(["bug"])
    # order = expect(page.locator("qbsearch-input")).to_contain_text("bug")
    print(order)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
