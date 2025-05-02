

title = [
    "Data center cooling",

    # "",
]

abstarct = title
claim = title

CPC_single =  [
    "H05K7/2071",
    "H05K7/2075",
    # "H05K7/2076",
    # "H05K7/20",
    # "H05K7/2083",
    # "H01L23/42",
    # "H05K7/2080",
    # "H05K7/2081",
    # "H05K7/2030",
    # "H01L23/367",
    # "H01L23/4",
    # "H05K7/2032",
    # "F25B27/0",
    # "",
]

IPC_single =  [
    "F28D15/0",
    "F28F3/0",
    # "H01L23/42",
    # "H01L23/4",
    # "H05K7/2",
    # "F25B27/0",
    # "F04B43/0",
    # "",
]

owner_single =  [
    "Zutacore",
    "JetCool",
    "NeoGene",
    "Seguente",
    "Nexalus",
    "Vertiv",
    "Nvidia",
    # "",
]

CPC_double =  [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
IPC_double =  [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


Owner_double =  [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


query = ""
single = [title,
          abstarct,
          claim,
          # CPC_single,
          # IPC_single,
          # owner_single
          ]
text_single = ["title:",
               "abstract:",
               "claim:",
               # "class_cpc.symbol:",
               # "class_ipcr.symbol:",
               # "owner_all.name:"
               ]
for s, t_s in zip(single,text_single) :

    for i in s:
        query += t_s + " "
        query +=  "(" + i + ")" + " OR "
    query = query[:-4]
    query +=") OR "
query = query[:-4]
print("\n Your requested query is:  \n")

print(query)

query = ""
query +="  ( ( "
double = [CPC_single, IPC_single, owner_single]
text_double = ["class_cpc.symbol:", "class_ipcr.symbol:",  "owner_all.name:"]
for s, t_s in zip(double,text_double) :
    for i in s:
        query += t_s + " "
        query +=  "(" + i + ")" + " OR "
    query = query[:-3]
    if t_s=="class_ipcr.symbol:":
        query += ") ) AND ("
    else:
        query +=") OR ("

query = query[:-4]
query +=" ) "
print("\n Your requested query is:  \n")
print(query)



    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",