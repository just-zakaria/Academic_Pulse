import pandas as pd, sqlite3, matplotlib.pyplot as plt, seaborn as sns; from pathlib import Path
root=Path(__file__).resolve().parents[1]; db=root/'outputs'/'feedback.db'; figs=root/'outputs'/'figures'; figs.mkdir(parents=True, exist_ok=True)

def load_feedback():
 conn=sqlite3.connect(db); df=pd.read_sql('SELECT * FROM feedback', conn); conn.close(); return df

def main():
 df=load_feedback(); df.mean().plot(kind='bar'); plt.savefig(figs/'chart.png')

if __name__=='__main__': main()