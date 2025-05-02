# Python program to generate WordCloud

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from Archive import funcTxtAnlytcs as ff
from Archive.funcTxtAnlytcs import abstrctExtrct
""" SELECT FILE :::  """
"""----------------------------------------------"""
""" Can only take lower case """

# fileName = r"MineBeaPermanentMotorAssembly.csv"

fileName = r"MineBeaSteppingMotor.csv"

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

"""----------------------------------------------"""

searchOutpt = []
valList = []

comment_words = ''
stopwords = set(STOPWORDS)
lt = []

""" TO PRINT FULL DATAFRAME   """
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# pd.options.display.max_colwidth = 100

print('fileName   : ',fileName)

""" Iterate through the csv file  """
df = pd.read_csv("Data/Raw Data/"  + fileName , encoding="latin-1")
""" Empty dataframe for search"""


""" THIS EXTRACTS THE ABSTRACT FROM GOOGLE BY RECEIVING PUBLICATION NUMBER"""
print(df["Publication Number"])
abstract = [abstrctExtrct(num) for num in df["Publication Number"].tolist()]
df = df.assign(abstract=abstract)

# # plot the WordCloud image


print(df.columns)
# data = pd.DataFrame(dfsearch)
data = pd.DataFrame(df[['Publication Number','Title','Inventors', 'Owners (US)', 'URL', 'Publication Year']])
data['IP Abstract'] = abstract

for val in data['IP Abstract']:
    # typecaste each val to string
    val = str(val)
    # split the value
    tokens = val.split()
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        lt.append(tokens[i])
    comment_words += " ".join(tokens) + " "
wordcloud = WordCloud(width=5000, height=3000, background_color='white', stopwords=ff.stopwords,
                      prefer_horizontal=1, min_font_size=10).generate(comment_words)
plt.figure('General wordcloud', figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
""" Saves the figure as SVG format """
# figName = "Data/" + fileName[0:-4] + colName + ".svg"
# plt.savefig(figName, dpi=None, format="svg",)
figName = "Data/" + fileName[0:-4] + colName + ".pdf"
plt.savefig(figName, dpi=500, format="pdf",)
data.to_excel("Data/Search Result/" + fileName[0:-4]  + "Output.xlsx")

plt.show()
