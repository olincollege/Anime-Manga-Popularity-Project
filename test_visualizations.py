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
]


@pytest.mark.parametrize("csv1, csv2, csv3", combine_data_sets_cases)
def test_combine_data_sets(csv1, csv2, csv3):
    """
    Test that a

    Args:

    """
    result = combine_data_sets(make_data_set(csv1), make_data_set(csv2))
    test = make_data_set(csv3)
    assert_frame_equal(result, test)


@pytest.mark.parametrize("csv1, test_list", clean_episodes_cases)
def test_clean_episodes(csv1, test_list):
    """
    Test that a

    Args:

    """
    result = clean_episodes(make_data_set(csv1))
    assert result == test_list
