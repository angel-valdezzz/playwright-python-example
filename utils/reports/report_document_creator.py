class ReportDocumentCreator:
    def __init__(self, report):
        self.report = report
    
    def create(self, context):
        document = Document()
        document.add_heading(self.report.title, level=1)
        document.add_paragraph(self.report.content)
        document.save(self.report.path)