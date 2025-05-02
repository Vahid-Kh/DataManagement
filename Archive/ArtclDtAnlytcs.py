
import pandas as pd                 # Dataframe library
from funcPlt import plt

"""________________________________________________________________________________"""
PDM = [
    "CO2_refrigeration_articles.csv",

]
"""________________________________________________________________________________"""
"""CONSTANTS"""
label = [0]*100
step = 1
n_ave= 240
"""________________________________________________________________________________"""


def logic(index):
    if index % step == 0:
        return False
    return True


"""________________________________________________________________________________"""

for pdm in range(len(PDM)):
    """     Random colors    """
    # col = (
    #         rd.random(),
    #         rd.random(),
    #         rd.random()
    #         )

    """     Danfoss colors   """
    # if pdm == 0:
    #     col = (1, 0, 0)
    # if pdm == 1:
    #     col = (0, 0, 0)
    # if pdm == 2:
    #     col = (0.5, 0.5, 0.5)
    # if pdm == 3:
    #     col = (0.8, 0.8, 0.8)
    # if pdm == 4:
    #     col = (0.6, 0.1, 0.1)
    # if pdm == 5:
    #     col = (0.2, 0.2, 0.2)
    # if pdm == 6:
    #     col = (1, 0.5, 0.5)
    # if pdm == 7:
    #     col = (1, 0.9, 0.9)

    """     Visible colors   """
    if pdm == 0:
        col = (1, 0, 0)
    if pdm == 1:
        col = (0, 0.9, 1)
    if pdm == 2:
        col = (0.6, 0.2, 0.8)
    if pdm == 3:
        col = (1, 1, 0)
    if pdm == 4:
        col = (0.4, 1, 0)
    if pdm == 5:
        col = (0, 0.2, 1)
    if pdm == 6:
        col = (1, 0, 1)
    if pdm == 7:
        col = (0, 0, 0)


    df = pd.read_csv('Data/' + PDM[pdm], skiprows=lambda x: logic(x), low_memory=False, sep=',')

    print(df.columns)
    dfcol = ['Lens ID', 'Title', 'Date Published', 'Publication Year',
       'Publication Type', 'Source Title', 'ISSNs', 'Publisher',
       'Source Country', 'Author/s', 'Abstract', 'Volume', 'Issue Number',
       'Start Page', 'End Page', 'Fields of Study', 'Keywords', 'MeSH Terms',
       'Chemicals', 'Funding', 'Source URLs', 'External URL', 'PMID', 'DOI',
       'Microsoft Academic ID', 'PMCID', 'Patent Citation Count', 'References',
       'Scholarly Citation Count']

    # Sort by time can be ascending or not
    df['Lens ID'] = pd.to_datetime(df['Date Published'])
    df.sort_values(by=['Lens ID'], inplace=True, ascending=True)
    print(df.head())
    # Print settings limit on Row and Column
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    # Head of df
    print(df.head())

    # The count of certain scaler in a column
    print(df['Publisher'].value_counts())

    # The normalized count of certain scaler in a column
    print(df['Publisher'].value_counts(normalize=True))

    # The description of a certain column
    print(df['Publication Year'].describe())
    print(df['Publication Year'].value_counts(bins=50))

    # ######Only patents with 'Publisher' of 'DK'
    # print(df.loc[df['Publisher'] == 'Elsevier BV'])

    # # Drops the patents with certain value in certain column
    # df.drop(df.loc[df['Type'] == 'Granted Patent'].index, inplace=True)

    # #####Patents with 'Publisher' of 'DK' 'NO'
    # print(df.loc[df['Publisher'].isin(['DK', 'NO'])])

    """ Filtered dataframe with 'type' and 'Publisher'
    To get 'Granted Patent' and in 'DK', 'NO','IT' containing following info 'Title', 'URL','Publication Number'"""
    # df_g_J = df.loc[df['Type'].isin(['Granted Patent'])].loc[df['Publisher'].isin(['DK', 'NO','IT'])][['Title', 'URL','Publication Number']]

    # ###Translate title to english
    # translator = Translator()
    # df_g_J['Title'] = [translator.translate(tit).text for tit in df_g_J['Title']]
    # print(df_g_J)

    """___________________________________________________________________________________________________________
    ____________________________________________________PLOTS_____________________________________________________
    ___________________________________________________________________________________________________________"""
    """
    First plots the lines and then 'ro' spesifies red dots  __ r ::  for red and o :: for circle
        Color               Shape                  shape
        b : blue            "8"	: octagon          "," : pixel
        g : green           "s"	: square           "o" : circle
        r : red             "p"	: pentagon         "v" : triangle_down
        c : cyan            "P"	: plus (filled)    "x" : x
        m : magenta         "*"	: star             "X" : x (filled)
        y : yellow          "h"	: hexagon1         "D" : diamond
        k : black           "H"	: hexagon2         "d" : thin_diamond
        w : white           "+"	: plus
    """

    """___________________________________________________________________________________________________________
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PERFORMANCE PLOTS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ___________________________________________________________________________________________________________"""
    """________________________________________________________________________________"""

    # """______________________________________ X _________________________________________"""
    # v1, label[1] = df['time'], 'Time [sec] '
    # v1, label[1] = df[],
    # """______________________________________ Y _________________________________________"""
    # v2, label[2] = df['2nd law efficiency Exergy based'], '2nd law efficiency Exergy based'
    # v2, label[2] = df[],
    # """_________________________________ var1, var2 ______________________________________"""
    # time = df['time'].tolist()
    # l = len(time)
    #
    # var1 = v1.tolist()
    # var2 = v2.tolist()
    #
    #
    # """Time vs. Var1, Var2 plot"""
    # plot_2(time, var1, var2, ["Time [s]", label[1], label[2]], PDM[pdm][0:2])
    # plt.scatter(mov_ave(var1, n_ave), mov_ave(var2, n_ave), s=0.2)
    #
    #
    # """To fix the legend"""
    # pdml = len(PDM) + 1
    # leg = PDM[:pdml] * 2
    # wt = " "
    # for i in range(len(leg)):
    #
    #     if len(leg)-1> i >=len(leg)/2:
    #         leg[i] += " scatter data"
    #
    #     elif i <len(leg)/2:
    #         wt += leg[i][:3] + ", "
    #         leg[i] += " polynomial regression order " + str(po)
    #     else:
    #         wt = wt[:-2]
    #         wt += " & " + leg[i][:3]
    #         leg[i] += " scatter data"
    #
    # for i in range(len(leg)):
    #
    #     if len(leg)-1> i >=len(leg)/2:
    #         leg[i] += " scatter data"
    #
    #     elif i <len(leg)/2:
    #         wt += leg[i][:3] + ", "
    #         leg[i] += " polynomial regression order " + str(po)
    #     else:
    #         wt = wt[:-2]
    #         wt += " & " + leg[i][:3]
    #         leg[i] += " scatter data"
    #
    # plt.legend(leg)



plt.show()
