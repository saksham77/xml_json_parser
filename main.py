from xml_json_parser import XmlJsonParser
from input_arguments import input_agr
import time


def start():
    """

    :return:
    """
    start_time = time.time()
    input_file, output_file, element = input_agr()
    XmlJsonParser(input_file, output_file, element).start()
    print("\n Time taken to complete: %s seconds." % (time.time() - start_time))


if __name__ == '__main__':
    start()