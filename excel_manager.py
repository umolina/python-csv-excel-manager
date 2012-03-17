import xlrd


class ExcelUnicodeReader(object):
    """
    Excel File Unicode Reader.
    Expects a filename and returns each row of csv file as a dictionary in a iteration
    """
    
    def __init__(self, filename):
        book = xlrd.open_workbook(filename)
        self.sheet = book.sheet_by_index(0)
        self.header = self.sheet.row_values(0)
        self.rows = self.sheet.nrows
        self.counter = 0
    
    def next(self):
        if self.counter == (self.rows - 1):
            raise StopIteration 
        row = self.sheet.row_values(self.counter + 1)
        self.counter += 1
        return self._attach_header(row)
    
    def __iter__(self):
        return self
    
    def _attach_header(self, raw_record):
        row = {}
        for index in range(self.sheet.ncols):
            row[str(self.header[index])] = raw_record[index]
        return row