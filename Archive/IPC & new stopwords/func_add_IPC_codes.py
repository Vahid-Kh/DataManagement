import pandas as pd
import numpy as np


N = 4

IPC_codes = pd.read_csv(r'IPC_table.xlsx').drop(columns=['Unnamed: 0'], axis=1)



def add_IPC_description(df, N):


    columnIPC = pd.DataFrame(df["IPCR Classifications"])


    columnIPC = columnIPC["IPCR Classifications"].str.split(';;', expand=True).add_prefix('code_')

    for i in columnIPC.columns:
        columnIPC[i] = columnIPC[i].astype(str).str[:N]


    for i in columnIPC.index:
        columnIPC.loc[i,:] = columnIPC.loc[i,:].drop_duplicates(keep='first')

    s = IPC_codes.set_index('code')['description']
    columnIPC = columnIPC.replace(s)

    columnIPC = columnIPC.fillna(value='')

    columnIPC['IPC Description'] = columnIPC[columnIPC.columns[0:]].apply(
        lambda x: ';'.join(x.dropna().astype(str)),
        axis=1
    )

    df['IPC Description'] = columnIPC['IPC Description']

    print('Descriptions added!')

    return df