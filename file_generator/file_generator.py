import os
from random import randint


class RowGenerator:

    def generate_row(self):
        #generates list of 4 values from 0 to 255 inclusive
        return [str(randint(0,255)) for p in range(0, 4)]
    
    
class RowAmountSetter:
    
    @property
    def row_amount(self):
        return randint(9000,11000)


class ListGenerator(RowGenerator, RowAmountSetter):        
    
    def generate_list(self,amount_of_rows):
        return map(lambda x:self.generate_row(), range(self.row_amount))

    
class FileSaver(ListGenerator):
    
    
    def __init__(self):
        
        self.file_name = 'file_test'
        self.file_suffix = 0
        
    @property
    def get_suffix(self):
        
        return self.file_suffix
    
    
    def save_file(self):
        
        file_name = 'test_files/' + self.file_name + '_' + str(self.file_suffix) + '.test'
        self.file_suffix += 1
        print(self.file_suffix)
        file = open(file_name, 'w+')
        
        for row in bot.generate_list(10):
            row = ','.join(row) +'\n'
            file.write(row)
        
        
class FileCreator(FileSaver):
    
    def __init__(self):
        super().__init__()
    
    def generate_files(self):
        
        for i in range(30):
            self.save_file()


if __name__ == '__main__':
    bot = FileCreator()
    bot.generate_files()
