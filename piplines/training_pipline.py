from zenml import pipeline
from steps.clearn_data import clean_data
from steps.ingest_data import ingest_data
from steps.model_train import train_model 
from steps.evaluation import evaluate_model



@pipeline
def train_pipeline(data_path:str):
    df = ingest_data(data_path)
    clean_data(df)
    train_model(df)
    evaluate_model(df)