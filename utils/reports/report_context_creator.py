from playwright.sync_api import Page

class ReportContextCreator:
    __test_name: str
    __instance = None
    __context: list = []

    def __new__(cls, test_name: str) -> object:
        if cls.__test_name != test_name:
            cls.__test_name = test_name
            return super().__new__(cls)
        return cls.__instance

    @classmethod
    def instance(cls):
        return cls.__instance

    def test_name(self):
        return self.__test_name

    def steps(self):
        return self.__context

    def step(self, title: str, page: Page) -> None:
        page.screenshot(path=f"reports/screenshots/{title}.png")
        self.__context.append({
            "title": title,
            "screenshot": f"screenshots/{title}.png"
        })
