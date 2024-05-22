import re
from playwright.sync_api import Playwright, sync_playwright, expect


class git_pars:
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.list_seller_name =[]

    def __page_down(self):
        self.page.evaluate()


    def __get_links(self):
        self.page.wait_for_selector(".Box-sc-g0xbh4-0 kXssRI")
        self.__page_down()
        self.page.wait_for_selector(f':text("Next")')

        search_result = self.page.query_selector(".Box-sc-g0xbh4-0 kXssRI")
        links = search_result.query_selector_all(".Box-sc-g0xbh4-0.Qaxme")
        print(len(links))

    def parse(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            self.context = browser.new_context()
            self.page = self.context.new_page()
            self.page.goto("https://github.com/search/advanced")
            self.get_by_label("Written in this language").select_option("Python")
            self.get_by_placeholder("200, >1000").click()
            self.get_by_placeholder("200, >1000").fill(">20000")
            self.get_by_placeholder("app.rb, footer.erb").click()
            self.get_by_placeholder("app.rb, footer.erb").fill("environment.yml")
            self.locator("#search_form div").filter(has_text="Advanced options From these").get_by_role(
                "button").click()
            self.__get_links()
    def run_3(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self = context.new_page()
        self.goto("https://github.com/search/advanced")
        self.get_by_label("Written in this language").select_option("Python")
        self.get_by_placeholder("200, >1000").click()
        self.get_by_placeholder("200, >1000").fill(">20000")
        self.get_by_placeholder("app.rb, footer.erb").click()
        self.get_by_placeholder("app.rb, footer.erb").fill("environment.yml")
        self.locator("#search_form div").filter(has_text="Advanced options From these").get_by_role("button").click()



        # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run_3(playwright)

    def get_by_label(self, param):
        pass
