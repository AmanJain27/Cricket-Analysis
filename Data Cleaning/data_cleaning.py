# =============================================================================
# Created By  : Aman Jain
# Created Date: echo Mon Nov 22 12:28:56 IST 2021
# =============================================================================
# Imports
# =============================================================================

import pandas as pd

# convert the csv file from Data Collection folder to dataframe
def convert_csv(filepath):
    df = pd.read_csv(filepath)
    return df

# to csv
def tocsv(filepath, df):
    df.to_csv(filepath)

# clean the data
def cleaning(dataframe):

    df = dataframe
    df['Debut Year'] = df['Span'].split("-")[0]
    df['Last Year'] = df['Span'].split("-")[1]
    return df 


def driver_code():
    converting_path = ''
