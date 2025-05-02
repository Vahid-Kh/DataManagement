# Python program to generate WordCloud

from wordcloud import WordCloud, STOPWORDS
import os
os.path.exists('/Users/paul/Library/Fonts/Verdana.ttf')
FONT_PATH = os.environ.get("FONT_PATH", "/Library/Fonts/Times 210106 Roman.ttf")
import matplotlib.pyplot as plt
import pandas as pd
from Archive import funcTxtAnlytcs as ff

""" SELECT FILE :::  """
"""----------------------------------------------"""
""" Can only take lower case """

fileNameList = [
    # r"ArticleAirConditioning20172020.csv",
    # r"ArticleCooling20172020.csv",
    # r"ArticleHeatPump20172020.csv",
    # r"ArticleRefrigeration20172020.csv",
    r"ArticleMoistureAcidDirtPurgerRetention.csv",
    ]
# fileName = r"PatentMoistureDirtAcidReclaimRecoveryPurger.csv"
# fileName = r"ArticleMoistureAcidDirtPurgerRetention.csv"
"""----------------------------------------------"""
""" SELECT COLUMN TO SEARCH :::  """
"""----------------------------------------------"""
""" The column to read from """
colName = "Title"
# colName = "Abstract"
# colName = "Keywords"
"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""

searchOutpt = []
valList = []

comment_words = ''
stopwords = set(STOPWORDS)
lt = []

""" TO PRINT FULL DATAFRAME   """
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# pd.options.display.max_colwidth = 100

for filename in fileNameList:
    comment_words = " "
    """ Iterate through the csv file  """
    # text = ""
    # with open('example.txt', encoding='utf-8') as f:
    #     text = ''.join(f.readlines())
    df = pd.read_csv("Data/Raw Data/" + filename, encoding="latin-1")
    for val in df[colName]:
        # typecaste each val to string
        val = str(val)
        # split the value
        tokens = val.split()
        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
            lt.append(tokens[i])
        comment_words += " ".join(tokens) + " "

    wordcloud = WordCloud(width=5000, height=3000,font_path=r'C:\Users\U375297\AppData\Local\Programs\Python\Python39\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\DejaVuSerif.ttf', background_color='white', stopwords=ff.stopwords,
                          prefer_horizontal=1, min_font_size=10).generate(comment_words)

    plt.figure(filename[0:-4], figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    """ Saves the figure as SVG format """
    figName = "Data/" + filename[0:-4] + colName + ".svg"
    plt.savefig(figName, dpi=None, format="svg",)

    figName = "Data/" + filename[0:-4] + colName + ".pdf"
    plt.savefig(figName, dpi=500, format="pdf",)

plt.show()


