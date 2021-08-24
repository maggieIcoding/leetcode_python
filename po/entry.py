

from optparse import OptionParser
# from sample import pprint

class Person:
    
    def __init__(self, name):
        print("__init__ EntryPrint class")
        self.name = name
    
    def introduce(self, skill):
        print("my name is {}, I can {}".format(self.name, skill))

# xiaoming = Person("xiaoming")
# print(xiaoming.name)
# xiaoming.introduce("play basketball")


class FileProcessor:

    def process(self, file_name, column):
        pass

def entry_print(word):
    print("{} printed in entry print function".format(word))

def convert_file(file_name, column):
    print("process file:{} on column: {}".format(file_name, column))


def parse_args():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
    parser.add_option("-c", "--column", type="int", dest="column", default=True)

    return parser.parse_args()

if __name__ == "__main__":
    #print("entry main")
    (option, args) = parse_args()
    print(option)
    convert_file(option.filename, option.column)