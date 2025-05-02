import pandas as pd
from funcPatent import df_patent_ipc, df_patent_full
import time

# fileName ="PatentIPCB60H1TeslaHeatPump20102021.csv"
fileName ="PatentAbstractGrantedPressureRegulator20102020.csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"


"""Number of digits from IPC code"""
inPath = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Documents\Python Projects\Data management\Data\Raw Data\\"
wrdCldPath = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Documents\Python Projects\Data management\Data\Word Cloud\\"
outPath = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Documents\Python Projects\Data management\Data\Search Result\\"



N=9      #complete IPC code
""" TO PRINT FULL DATAFRAME   """
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.max_colwidth = 100
""" Iterate through the csv file  """
df = pd.read_csv(inPath + fileName, encoding="latin-1", low_memory=False)


"""  XXXXXXXXXXXXXXXXXX
Remember to remove later
xxxxxxxxxxxxxxxxxxxxxxxxx"""
df= df[:2]

dft = df

df1 = df[:1]
df1 = df_patent_ipc(df1, N)
df1 = df_patent_full(df1)

dftot = pd.DataFrame(columns=df1.columns)

start = time.time()

if len(df) >= 100:

    for i in range(round(len(df)/100)):

        print("Please be patient ... I'm at row # ", i*100)

        df = dft[i*100:(i+1)*100]
        df = df_patent_ipc(df, N)
        df = df_patent_full(df)

        dftot = dftot.append(df, sort=False)
        if i ==0:
            end = time.time()
            elapsed = end - start
        print("Estimated time remaining : ", round((round(len(dft) / 100) - i) * elapsed // 60), "minutes & " ,  round((round(len(dft) / 100) - i) * elapsed % 60), "seconds")

else:

    print("This won't take long...")
    df = df_patent_ipc(df, N)
    df = df_patent_full(df)
    dftot = dftot.append(df, sort=False)


dftot.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N)  + "Full Text" + ".csv")
