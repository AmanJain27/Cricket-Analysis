# =============================================================================
# Created By  : Aman Jain
# Created Date: echo Mon Nov 22 12:28:56 IST 2021
# =============================================================================
# Imports
# =============================================================================

import pandas as pd

# convert the csv file from Data Collection folder to dataframe
def convert_csv(filepath):
    df = pd.read_csv(filepath, index_col=0)
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
    df = df.loc[df['Total Years'] >= 5].copy() 
    df = df.reset_index()
    # list of dataframes to convert to numeric
    conv_numeric = ['Mat', 'Inns', 'NO', 'Runs', 'Ave', 'BF', 'SR', '100', '50', '0']
    for i in conv_numeric:
        df[i] = pd.to_numeric(df[i], errors="coerce")

    df = df.loc[df['HS'] != '-'].copy()    
    # innings per matches
    
    df['Innings per Matches'] = df['Inns']/df['Mat']
    
    # not outs per innings
    df['Not outs per innings'] = df['NO']/df['Inns']
    # average runs per innings (literal arithmatic average)
    # Average in Cricket is calculated as (Total Runs) / (Inns played - Not out)
    # Here average is (Total Runs) / (Inns played)
    df['Arithmatic Average of Total Runs by Inns Played'] = df['Runs']/df['Inns']
    # sort by number of not outs in desc order
    # df = df.sort_values("Not outs per innings", ascending=False)
 
    # create a column to specify wheter the batsman was out or not out when he scored his highest
    df['Not Out when scored highest'] = df['HS'].apply(lambda x: 1 if '*' in x else 0)
    # Highest scores in numeric
    df['HS Numeric'] = df['HS'].apply(lambda x: int(x[:-1]) if '*' in x else int(x))
    # number of 100's, 50's, 0's per innings
    df['100\'s per innings'] = df['100']/df['Inns']
    df['50\'s per innings'] = df['50']/df['Inns']
    df['0\'s per innings'] = df['0']/df['Inns']
    # 4's and 6's numeric
  
    df["4s numeric"] = df['4s'].apply(lambda x : int(x) if '+' not in x else int(x[:-1]))
    df["6s numeric"] = df['6s'].apply(lambda x : int(x) if '+' not in x else int(x[:-1]))
    # total boundaries
    df['boundaries'] = df['4s numeric'] + df['6s numeric']
    # 4's and 6's per inns
    df["4s per Inns"] = df["4s numeric"]/df["Inns"]
    df["6s per Inns"] = df["6s numeric"]/df["Inns"]
    # runs scored by boundaries per inns
    df['Boundary Ave per Inns'] = df['4s per Inns']*4 + df['6s per Inns']*6
    # boundaries per innings
    df['boundaries per innings'] = df['boundaries']/df['Inns']
    # total runs scored by boundaries
    df['runs scored by boundaries'] = df['4s numeric'].apply(lambda x : x*4) + df['6s numeric'].apply(lambda x : x*6)
    # ratio of runs scored by boundaries
    df['boundaries to runs ratio'] = df['runs scored by boundaries']/df['Runs']

    # runs without boundaries
    df['runs without boundaries'] = df['Runs'] - df['runs scored by boundaries']
    # balls faced that weren't boundaries
    df['BF without boundaries'] = df['BF']-df['boundaries']

    # strike rate without boundaries
    # Here we can subtract total number of boundaries from BF (Balls Faced) and subtract total runs
    # scored by boundaries from total runs. We can then calculate the ratio to check the strike
    # rate of a batter without boundaries.
    df['Strike Rate without boundaries'] = (df['runs without boundaries']/df['BF without boundaries']) * 100 
    
    # Average runs per year
    df['Avg runs per year'] = df['Runs'] / df['Total Years']
    
    return df



def driver_code():
    converting_path = '../Data Collection/merged.csv'
    df = convert_csv(filepath=converting_path)
    df = cleaning(df)
    to_convert_path = 'scores_reference.csv'
    tocsv(to_convert_path, df)

driver_code()
