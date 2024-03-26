import csv
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def make_data_set(path):
    """
    Reads the CSV file and creates readable data

    Args:
        path: A path to the CSV file that will be read

    Return:
        A data set of the entered CSV file written with the columns
        "Rank,Title,Rating,Image_URL,Episodes,Dates"
    """
    data_set = pd.read_csv(path)

    return data_set


def combine_data_sets(data1, data2):
    """
    Combines two data sets from CSV files into one

    Args:
        data1: The first data set
        data2: The second data set

    Return:
        A single data set that has the data from the two entered in

    """
    data_combined = pd.concat([data1, data2], ignore_index=True)
    data_combined = data_combined.sort_values(by=["Rank", "Rating"])
    return data_combined

    # data_set = pd.read_csv(path)


# def find_rank(data_fav, data_pop):
#    """ """
#    count = 0
#    while count < len(data_fav["Rank"]):


# def sort_data_set(data_fav, data_pop):
#    """ """
#    ranking_fav = {}
#    ranking_pop = {}
#    for i in data_fav["Title"]:
#        if i in data_fav["Title"] and i in data_pop["Title"]:
#            ranking_fav[i] = data_fav[i]


def make_scatter_plot(data_set):
    """
    Creates a scatter plot given a data set

    Arg:
        A data set of "Rank,Title,Rating,Image_URL,Episodes,Dates" of which
        is being graphed

    Return:
        A visualized scatter plot of the rank on the x-axis and the rating
        on the y-axis
    """
    rank = data_set["Rank"]
    rating = data_set["Rating"]

    plt.plot(rank, rating, ".")

    plt.xlabel("Rank")
    plt.ylabel("Rating")
    plt.title("Scatter Plot :3")
    plt.show()


def analyze_scatter_plot(data):
    """
    Given the data set used to plot the scatter plot, create findings to help
    answer the reasearch question

    Args:
        data: The same data set used to crate the scatter plot

    Return:
        A string that has the title of the "anime/manga"
    """
    max_rating = max(data["Rating"])
    csv.DictReader(data)
    counter = 0
    for row in data["Rating"]:
        if row == max_rating:
            break
        else:
            counter += 1
    print(data.iloc[counter])


def make_wordcloud(data):
    """
    Creates a visualized wordcloud given a data set

    Args:
        A data set of "Rank,Title,Rating,Image_URL,Episodes,Dates" of which
        is being graphed

    Returns:
        A visualized wordcloud of the most common words that appear
    """
    text = " ".join(data["Title"])

    wordcloud = WordCloud(
        collocations=False, background_color="white"
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("WordCloud :3")
    plt.show()


def make_bar_graph(data):
    """
    Creates a visualized bar graph from the given data set

    Args:
        A data set of "Rank,Title,Rating,Image_URL,Episodes,Dates" of which
        is being graphed

    Returns:
        A visualized bar graph of each anime/manga and their respective episode
        counts
    """
    num_episodes = []
    for row in data["Episodes"]:
        if row[0] == "T":
            temp = row.replace("TV (", "")
            temp = temp.replace(" eps)", "")
            num_episodes += [temp]
        else:
            temp = row.replace("Movie (", "")
            temp = temp.replace(" eps)", "")
            num_episodes += [temp]
    for i, row in enumerate(num_episodes):
        if row == "?":
            num_episodes[i] = "1000"
    num_episodes = [eval(i) for i in num_episodes]

    plt.figure(figsize=(10, 7))
    plt.barh(data["Title"], num_episodes)
    plt.xlabel("Number of Episodes")
    plt.ylabel("Titles")
    plt.title("Bar Graph :3")
    plt.show()
