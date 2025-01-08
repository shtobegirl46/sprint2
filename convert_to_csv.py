import typing
import numpy
import numpy as np
import pandas as pd
import csv


def result_to_csv(result: list[list[float, float, str, str]], output_name, DEBUD=False):
    """
    :param results: List[List[latitude: float, longitude: float, ammunition: str, certainly: str]]
    :return:
    """
    with open(output_name, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        header = ['latitude', 'longitude', 'ammunition', 'certainly']
        writer.writerow(header)
        for row in result:
            writer.writerow(row)
    if DEBUD:
        print("file saved successfuly!")

def test():
    result = [[1.0, 2.0, "aaa", "bbb"], [1.0, 2.0, "aaa", "bbb"]]
    result_to_csv(result, "test_output.csv", True)

if __name__ == "__main__":
    test()
