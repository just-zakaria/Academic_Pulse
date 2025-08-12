from pathlib import Path; import pandas as pd; from sqlalchemy import create_engine; from src.utils import load_csv, basic_clean
root=Path(__file__).resolve().parents[1]; data=root/'data'/'student_feedback.csv'; out=root/'outputs'; out.mkdir(exist_ok=True)
clean=out/'cleaned_feedback.csv'; db=out/'feedback.db'

def main():
 df=basic_clean(load_csv(data)); df.to_csv(clean, index=False); engine=create_engine(f'sqlite:///{db}'); df.to_sql('feedback', engine, if_exists='replace', index=False)

if __name__=='__main__': main()