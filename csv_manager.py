import csv, codecs


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, stream, encoding):
        self.reader = codecs.getreader(encoding)(stream)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode('utf-8')
    
        
class CsvUnicodeReader(object):
    """
    Unicode Csv File Reader.
    Expects a filename and returns each row of csv file as a dictionary in a iteration
    """
    
    def __init__(self, filename, encoding='utf-8', **kwargs):
        stream = UTF8Recoder(open(filename, 'rb'), encoding)
        self.reader = csv.DictReader(stream, **kwargs)
        self.counter = 0
    
    def next(self):
        row = self.reader.next()
        self.counter += 1
        return dict([(key, unicode(value, 'utf-8')) for (key, value) in row.iteritems()])
    
    def __iter__(self):
        return self


