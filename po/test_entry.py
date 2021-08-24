from optparse import OptionParser

class StringIndexer:
    def __init__(self, l_string, l_index):
        self.l_string = l_string
        self.l_index = l_index

def str_indicator(l_string, l_index):
    print("string_line:{} on index: {}".format(l_string, l_index))

def parse_args():
    parser = OptionParser()
    parser.add_option("-s", "--str", dest="string",
                    help="write report to FILE", metavar="FILE")
    parser.add_option("-i", "--index", type="int", dest="index", default=True)

    return parser.parse_args()

if __name__ == '__main__':

