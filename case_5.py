import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run_5(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/microsoft/vscode/graphs/commit-activity")
    page.locator("g:nth-child(26) > rect").click()
    expect(page.locator("#commit-activity-master")).to_contain_text("11/12")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run_5(playwright)
