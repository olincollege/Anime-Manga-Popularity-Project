from collections import Counter
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
import matplotlib.pyplot as plt
import csv


from Visualizations import (
    make_bar_graph,
    make_data_set,
    make_scatter_plot,
    make_wordcloud,
    combine_data_sets,
    analyze_scatter_plot_min,
    analyze_scatter_plot_max,
    clean_episodes,
)

combine_data_sets_cases = [
    # Test that two 2x2 integer and float csv files will combine to create a
    # 2x4 csv with the correct values in each row/column
    ("Test/mock_csv1.csv", "Test/mock_csv2.csv", "Test/test_mock_csv1.csv"),
    # Test that two 3x2 integer, float, and string csv files will combine to
    # create a 3x4 csv file with the correct values in each row/column
    ("Test/mock_csv3.csv", "Test/mock_csv4.csv", "Test/test_mock_csv2.csv"),
    # Test that two 5x6 integer, float, and string in the orignal format of
    # myanimelist csv files will combine to create a 10x6 csv file with the
    # correct values in each row/column
    ("Test/mock_csv5.csv", "Test/mock_csv6.csv", "Test/test_mock_csv3.csv"),
]

clean_episodes_cases = [
    # Test a csv with a column titled Episodes that has 4 items in it that
    # are in the same TV format as the myanimelist dataframe
    ("Test/clean_mock_csv1.csv", [24, 64, 12, 36]),
    # Test a csv with a column titled Epsiodes that has 0 items in it
    # will return an empty list
    ("Test/clean_mock_csv2.csv", []),
    # Test a csv with a column titled Episodes that has 4 items in it that
    # are in the same Movie format as the myanimelist dataframe
    ("Test/clean_mock_csv3.csv", [64, 36, 24, 12]),
    # Test a csv with a column titled Episodes that has 4 items in it that
    # are in the same TV and Movie format as the myanimelist dataframe
    ("Test/clean_mock_csv4.csv", [64, 12, 24, 36]),
    # Test a csv with a column titled Episodes that has 4 items in it that
    # are in the same TV and Movie format as the myanimelist dataframe and
    # tests that a ? will automatically change to 1000
    ("Test/clean_mock_csv5.csv", [24, 1000, 12, 36]),
    # Test a csv with a column titled Episodes that has 5 items in it that
    # are in the same TV and Movie format as the myanimelist dataframe and
    # tests that a ? will automatically change to 1000
    ("Test/clean_mock_csv6.csv", [24, 1000, 12, 36, 1]),
    # Test a csv with a column s other than just episodes will return
    # the correct cleaned data
    ("Test/clean_mock_csv7.csv", [12, 1000, 36, 64, 1]),
]


@pytest.mark.parametrize("csv1, csv2, csv3", combine_data_sets_cases)
def test_combine_data_sets(csv1, csv2, csv3):
    """
    Test that two pandas dataframes can be combined into a single pandas
    dataframe with the correct values and order.

    Check that given two pandas dataframes the combine_data_set() function
    can return a single pandas dataframes no matter what is in the two
    entered pandas dataframes

    Args:
        csv1: A csv file that will be converted into a pandas dataframe that
            will be the first dataframe in the combination
        csv2: A csv file that will be converted into a pandas dataframe that
            will be the second dataframe in the combination
        csv3: A csv file that will be converted into a pandas dataframe that
            holds the correct combined data from the two pandas dataframes being
            combined


    """
    result = combine_data_sets(make_data_set(csv1), make_data_set(csv2))
    test = make_data_set(csv3)
    assert_frame_equal(result, test)


@pytest.mark.parametrize("csv1, test_list", clean_episodes_cases)
def test_clean_episodes(csv1, test_list):
    """
    Test that inside a pandas dataframes, a single column can be altered
    and manipulated and cleaned to make the data easier to manipulate

    Check that given a pandas dataframe the clean_episodes function will
    be able to access the correct column and correctly alter the strings
    in each row to return a list of integers

    Args:
        csv1: A csv file that will be converted into a pandas dataframe that
            will contain atleast one column of "Episodes" that will be cleaned
        test_list: A list that contains the correct cleaned output of the
            clean_episodes() function

    """
    result = clean_episodes(make_data_set(csv1))
    assert result == test_list
