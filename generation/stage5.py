from docx.shared import Pt, Inches


from generation import Project


class Stage5:

    def __init__(self):
        self.stage_number = 5

    def build(self, document):

        header = document.add_paragraph()
        header.add_run('5. Ograniczenia dziedzinowe').font.size = Pt(Project.HEADER_SIZE)
        document.add_page_break()

        print('Etap 5 wygenerowany')
