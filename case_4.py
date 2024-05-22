import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run_4(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://skillbox.ru/code/")
    page.locator("label").filter(has_text="Профессия").locator("span").click()
    page.get_by_label("Изменить диапозон").first.click()
    page.get_by_label("Изменить диапозон").first.press("ArrowRight")
    page.get_by_label("Изменить диапозон").nth(1).click()
    page.get_by_label("Изменить диапозон").nth(1).press("ArrowLeft")
    expect(page.get_by_role("main")).to_contain_text("От 6 до 12 мес")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run_4(playwright)
