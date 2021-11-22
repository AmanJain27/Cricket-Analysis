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
    print('converted to csv')

# clean the data
def cleaning(dataframe):
    
    
    df = dataframe
    # debut year and final year
    df['Debut Year'] = df['Span'].apply(lambda x: x.split('-')[0])
    df['Last Year'] = df['Span'].apply(lambda x: x.split('-')[1])
    # number of years active
    df["Total Years"] = pd.to_numeric(df['Last Year']) - pd.to_numeric(df['Debut Year'])
    # innings per matches
    df['Innings per Matches'] = df['Inns']/df['Mat']
    
    # not outs per innings
    df['Not outs per innings'] = df['NO']/df['Inns']
    # average runs per innings (literal arithmatic average)
    # Average in Cricket is calculated as (Total Runs) / (Inns played - Not out)
    # Here average is (Total Runs) / (Inns played)
    df['Arithmatic Average of Total Runs by Inns Played'] = df['Runs']/df['Inns']
    # sort by number of not outs in desc order
    df = df.sort_values("Not outs per innings", ascending=False)
    return df



def driver_code():
    converting_path = '../Data Collection/scores.csv'
    df = convert_csv(filepath=converting_path)
    df = cleaning(df)
    to_convert_path = 'scores_reference.csv'
    tocsv(to_convert_path, df)

driver_code()
