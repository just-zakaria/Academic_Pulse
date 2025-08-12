import pandas as pd

def load_csv(p): return pd.read_csv(p)

def basic_clean(df):
 df=df.copy().dropna(how='all')
 return df