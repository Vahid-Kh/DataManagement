import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from funcTxtAnalytics import add_abstract, stringWord, addIPCdescription, stopwords, frequentWords, patent_abstract,df_patent_full,patent_fulltext,add_fulltext
import math
import nltk

# from patent_scraping import add_abstract

inPath = r"C:\Users\u375297\OneDrive - Danfoss\Documents - RAC Tech Center - Programming Projects\Python Projects\Data management\Data\Raw Data\\"
wrdCldPath = r"C:\Users\u375297\OneDrive - Danfoss\Documents - RAC Tech Center - Programming Projects\Python Projects\Data management\Data\Word Cloud\\"
outPath = r"C:\Users\u375297\OneDrive - Danfoss\Documents - RAC Tech Center - Programming Projects\Python Projects\Data management\Data\Search Result\\"

# fileName = r"PatentsAbstractBallValve20142020.csv"
# fileName = "ArticleWaterValveRefrigeration.csv"
# fileName = "ArticlePressureRegulator.csv"
# fileName = "PatentAbstractGrantedPressureRegulator20102020.csv"
# fileName= "PatentsF25WaterValve20102020.csv"
# fileName = "PatentIPCB60H1TeslaHeatPump20102021.csv"
# fileName = "ArticleExpansionValve19802021.csv"
# fileName = "PatentF25AbsClaimExpansionValve.csv"
# fileName = "ArticleCoolingRefrigerationChillerHeatPump20172021.csv"
# fileName = "ArticleHeatExchangerRefrigeration.csv"
# fileName ="ArticleSuperheatControlElectronicExpansionValve.csv"
# fileName ="PatentF25ANDHeatExchanger20052021.csv"
# fileName ="PatentSuperheatControlElectronicExpansionValve20052021.csv"
# fileName ="PatentHeatExchangerAlfaLaval.csv"
# fileName ="PatentAbstractCondensingUnitsF25_.csv"
# fileName ="PatentAbstractFrostHeatExchanger.csv"
# fileName ="ArticleActuatorTitleCitedByPatent20102021.csv"
# fileName ="ArticleActuatorTitle20102021.csv"
# fileName ="PatentActuatorsTitleGranted20102021.csv"
# fileName ="ArticleHightorqueActuatorAbstract.csv"
# fileName ="PatentHightorqueActuatorAbstract.csv"
# fileName ="PatentF16KANDF25BGranted20162021.csv"
# fileName ="PatentF16KANDF25BGranted20162021.csv"
# fileName ="ArticleAmmoniaCO2Refrigeration.csv"
# fileName ="PatentIndustrialF25B.csv"
# fileName ="PatentAmmoniaPropaneCO2F25B.csv"
# fileName ="PatentRefrigerantPipeConnectorLeakTightGasSealingPlastic.csv"
fileName ="PatentAbstractHighTensileStrengthMaterialIPCC21C23C22F.csv"
# fileName ="ScholarSustainableMaterial1975-2021.csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"


""" The column to read from """
# colName = "IPC Description"
colName = "Title"
# colName = "Abstract"
# colName = "Keywords"
# colName = "FullText"
"""Number of digits from IPC code"""
#N=3     #first level
#N=4     #second level
N=9      #complete IPC code

"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""

""" TO PRINT FULL DATAFRAME   """
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.max_colwidth = 100
""" Iterate through the csv file  """
df = pd.read_csv(inPath + fileName, encoding="latin-1", low_memory=False)

dftot = pd.DataFrame(columns=df.columns)
print("File name: ", fileName)
print("Column name: ", colName)

for i in range(math.ceil((len(df)/100))):

    print("I'm at row # ", i*100)
    try:
        dfi = df[i*100:(i+1)*100]
    except:
        dfi = df[i * 100:-1]

    if colName == "Abstract" and "Abstract" not in dfi.columns.tolist():
        """ Adds abstract to a data frame"""
        dfi = add_abstract(dfi)
    if colName == "IPC Description":
        """ add ipc descriptions """
        dfi = addIPCdescription(dfi, N)
    if colName == "FullText":
        """ add FullText"""
        dfi = add_fulltext(dfi)
    dftot = dftot.append(dfi, sort=False)

df = dftot
"""Creates an string from a column of a data frame"""
"""Used prior to wordcloud for preparing the string"""
string = stringWord(df, colName)

# # plot the WordCloud image
# print(string)

wordcloud = WordCloud(width=3600, height=5760, background_color='black', stopwords=stopwords,
                      prefer_horizontal=1, min_font_size=5).generate(string)

plt.figure('General wordcloud', figsize=(8, 16), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

if colName == "IPC Description":
    figName = str(wrdCldPath) +  "WordCloud_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".pdf"
else:
    figName = str(wrdCldPath) +  "WordCloud_" + fileName[0:-4] + "_" + colName + ".pdf"


plt.savefig(figName, dpi=500, format="pdf",)
# plt.savefig(figName, dpi=500, format="svg",)
plt.show()

"""Save the new df with IPC descriptions"""
if colName == "IPC Description":
    df.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")
if colName == "Abstract":
    df.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N) + colName + ".csv")
# df = df_patent_full(df)
most_occur = frequentWords(string)
#
"""Save the new df with frequency words"""
if colName == "IPC Description":
    most_occur.to_csv("FrequentWords_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")
else:
    most_occur.to_csv("FrequentWords_" + fileName[0:-4] + colName + ".csv")

