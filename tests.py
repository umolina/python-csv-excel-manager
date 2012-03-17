import unittest

from csv_manager import CsvUnicodeReader
from excel_manager import ExcelUnicodeReader

class CsvUnicodeReaderTestCase(unittest.TestCase):
    
    def setUp(self):
        self.iterator = CsvUnicodeReader('support/data.csv')
        
    def test_iterator(self):
        expected = {'first_name':u'person1\u16b8', 'email':u'person1@gmail.com', 'title':u'Mr\u0d8c'}
        expected_rows = 7
        
        first_row = self.iterator.next()
        self.assertEquals(first_row, expected)
        
        count = 1
        for row in self.iterator:
            count += 1
        
        self.assertEquals(self.iterator.counter, expected_rows)
        self.assertEquals(count, expected_rows)


class ExcelUnicodeReaderTestCase(unittest.TestCase):
    
    def setUp(self):
        self.iterator = ExcelUnicodeReader('support/data.xls')
        
    def test_iterator(self):
        expected = {'name':u'person1\u16b8', 'email':u'person1@gmail.com', 'mobile':u'0777777777\u0d8c'}
        expected_rows = 4
        
        first_row = self.iterator.next()
        self.assertEquals(first_row, expected)
        
        count = 1
        for row in self.iterator:
            count += 1
        
        self.assertEquals(self.iterator.counter, expected_rows)
        self.assertEquals(count, expected_rows)
        

        

if __name__ == '__main__':
    unittest.main()
