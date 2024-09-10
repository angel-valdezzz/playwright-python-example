import os

class ReportsDirContent:
    def __init__(self, filename: str) -> None:
        cd = os.path.dirname(__file__)
        data_dir = os.path.join(cd, "..", "output", "reports")
        self.__data_source = os.path.abspath(os.path.join(data_dir, filename))

    def get_content(self):
        return self.__data_source
