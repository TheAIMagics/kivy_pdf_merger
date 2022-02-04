import os
from PyPDF2 import PdfFileMerger


class FileOperations:
    def __init__(self, path):
        self.path = path

    def authenticate_path(self, path):
        print(os.path.exists(path))
        try:
            if os.path.exists(path):
                return True
            else:
                False
        except Exception as e:
            error = str(e)
            return error

    def available_file(self):
        try:
            list_dir = os.walk(self.path)
            available_files = []
            for root, dirs, files in list_dir:
                for file in files:
                    available_files.append(file)
            return available_files
        except Exception as e:
            error = str(e)
            return error

    def isPdf(self,file):
        try:
            if file.endswith('.pdf'):
                return True
            else:
                return False
        except Exception as e:
            error = str(e)
            return error

    def count_pdfs(self, list_of_files):
        try:
            if len(list_of_files) == 0:
                return 0
            else:
                count = 0
                for file in list_of_files:
                    if self.isPdf(file):
                        count +=1
                return count
        except Exception as e:
            error = str(e)
            return error

    def filter_pdfs(self, list_of_files, path):
        try:
            pdf_list = []
            for file in list_of_files:
                if file:
                    filename = os.path.join(path,file)
                    if self.authenticate_path(filename) and self.isPdf(file):
                        pdf_list.append(file)
            return pdf_list
        except Exception as e:
            error = str(e)
            return error

    def merge_pdf(self, list_of_files, path):
        try:
            count = self.count_pdfs(list_of_files)
            pdf_list = self.filter_pdfs(list_of_files, path)
            if count == 0:
                return f"NO PDF FOUND in PATH:{path}"
            if count == 1:
                return f"ONE PDF - {pdf_list[0]} FOUND"
            if count >=2:
                file_name = 'merged.pdf'
                merged_pdf = os.path.join(path, file_name)
                merger = PdfFileMerger()
                for file in pdf_list:
                    filename = os.path.join(path, file)
                    merger.append(filename)
                merger.write(f'{merged_pdf}')
                merger.close()
                return f'PDF MERGED - {merged_pdf}'
        except Exception as e:
            error = str(e)
            return error
