import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/microsoft/vscode/issues")
    page.get_by_role("button", name="Author").click()
    page.get_by_role("textbox", name="Filter users").fill("bpasero")
    page.get_by_role("menuitem", name="author:bpasero Filter by this").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run_2(playwright)
