from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import os
from PyPDF2 import PdfFileMerger
from FileOperations import FileOperations

Builder.load_file('pdf.kv')
merger = PdfFileMerger()

class MyLayout(Widget):
    path = ObjectProperty(None)

    def list_files(self):
        try:
            path = self.input_path.text
            path = path.strip()
            list_dir = os.listdir(path)
            object_file = FileOperations(path)

            files_present = object_file.available_file()
            all_files = ''
            if object_file.authenticate_path(path):
                if len(files_present) > 0:
                    for file in files_present:
                        all_files = f'{all_files}\n{file}'
                else:
                    all_files = f"No file present in {path}"
            else:
                all_files = f"{path}- NOT VALID"

            pdf_files = ''
            for item in list_dir:
                if item.endswith('.pdf'):
                    pdf_files = f'{pdf_files}\n{item}'

            self.ids.pdf_view.text = f'{pdf_files}'
            self.ids.list_view.text = f'{all_files}'
        except Exception as e:
            print(e)

    def merge_pdfs(self):
        try:
            prior = self.ids.list_view.text
            file_list = prior.split()
            path = self.input_path.text
            object_file = FileOperations(path.strip())
            result = object_file.merge_pdf(file_list, path)
            self.ids.result.text = f"{result}"
        except Exception as e:
            print(e)

    def clear(self):
        self.input_path.text = ''
        self.ids.pdf_view.text = ''
        self.ids.list_view.text = ''
        self.ids.result.text = ''


class PdfMergerApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    PdfMergerApp().run()
