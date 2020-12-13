import os
from file_generator import FileCreator

class FileChecker:
    
    @property
    def file_list(self):
        return os.listdir('test_files/')
    

class Upload(FileChecker):
    
    def upload_file(self,file):
        
        data = {
            'file_name':file.split('.')[0],
        }
        
        url = "http://127.0.0.1:8000/upload/"
        files = {'file':('test_file', open(f'test_files/{file}', 'rb'))}
        r = requests.put(url, files=files,data=data)  

class FilesUploader(Upload):
    
    def upload_files(self):
        
        for file in self.file_list:
            self.upload_file(file)


if __name__ == '__main__':
 
    agent = FilesUploader()
    agent.upload_files()