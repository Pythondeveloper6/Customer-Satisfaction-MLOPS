import logging
import pandas as pd
from zenml import step


@step
def evaluate_model(df:pd.DataFrame) -> None:
    """
    evaluates the model on the ingest data 
    Args:
        df : the ingested df 
    """
    pass