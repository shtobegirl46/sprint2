import typing
import numpy
import numpy as np
import pandas as pd
import csv


def np_array_to_csv(np_array, output_name, DEBUD=False):
    """
    :param np_array: the np_array is many [latitude, longitude, ammunition, certainly]
    :return:
    """
    header = "latitude,longitude,ammunition,certainly"
    numpy.savetxt(output_name, np_array, delimiter=",", header=header, comments='')
    if DEBUD:
        print("file saved successfuly!")

def test():
    np_array = numpy.asarray([[1, 2, 3, 4], [4, 5, 6, 7]])
    np_array_to_csv(np_array, "test_output.csv", True)

if __name__ == "__main__":
    test()
