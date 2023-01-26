import pandas as pd
import re

csv_files = ["export-data (1).csv", 
             "export-data (2).csv", 
             "export-data (3).csv", 
             "export-data (4).csv", 
             "export-data (5).csv"]

zotero = pd.DataFrame()

# appends all files together, zotero only allowed batch exports of size 100
for file in csv_files:
            df_temp = pd.read_csv(file)
            zotero = zotero.append(df_temp, ignore_index=True)

zotero.head()

# function to apply to column
def find_num(string):
    if type(string) != str:
        return string
    splitted = string.split() # split string into individual words
    result = [i for i in splitted if i.startswith("#")] # get only the string that starts with #
    return re.sub('\D', '', result[0])

zotero['Extra'] = zotero['Extra'].apply(find_num)

zotero.to_csv("updated_zotero.csv", sep=",", index=False)
