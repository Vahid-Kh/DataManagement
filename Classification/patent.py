#Read-in script for Number of figures and sheets

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
import numpy as np

# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir(r"C:\Users\U375297\Documents\PycharmProjects\Data management\PatentsView\ZipFiles")
year = [
        # "2000",
        # "2001",
        # "2002",
        # "2003",
        # "2004",
        # "2005",
        # "2006",
        # "2007",
        # "2008",
        # "2009",
        # "2010",
        # "2011",
        # "2012",
        # "2013",
        # "2014",
        # "2015",
        # "2016",
        # "2017",
        # "2018",
        # "2019",
        "2020",
        ]
file_name = "claims_" + str(year[0]) + ".tsv.zip"
f_name = "claims_" + str(year[0]) + ".tsv"
# Selecting the zip file.
zf = zip.ZipFile(file_name)
# Reading the selected file in the zip.
df = pd.read_csv(zf.open(f_name), delimiter="\t", quoting = csv.QUOTE_NONNUMERIC,low_memory=False)

chunksize = 15*(10 ** 5)
count = 1
n_obs = 0
dtype={'sequence': int}
for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize,low_memory=False):
    print('processing chunk: ' + str(count))
    n_obs += len(df)
    count += 1
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)
print(df.describe(exclude=[np.number]))
