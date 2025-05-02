import pandas as pd

IPC_codes = pd.read_csv(r'IPC_table.csv').drop(columns=['Unnamed: 0'], axis=1)



for i in IPC_codes.index:

    k = IPC_codes.iloc[i,0]

    if len(k) == 14:

        k = k[:-4]
        k = k[:-6] + k[6:]
        k = str(k[:-2]) + '/' + str(k[6:])



    if len(k) == 9:
        if k[4] == "0":
            k = k[:4] + k[5:]

    IPC_codes.iloc[i,0] = k

IPC_codes.to_csv(r'IPC_table_new.csv')





