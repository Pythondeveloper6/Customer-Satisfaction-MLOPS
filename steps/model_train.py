import logging
import pandas as pd
from zenml import step
from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin
from .config import ModelNameConfig

@step()
def train_model(
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    config: ModelNameConfig,
) -> RegressorMixin:
    """
    Args:
        x_train: pd.DataFrame
        x_test: pd.DataFrame
        y_train: pd.Series
        y_test: pd.Series
    Returns:
        model: RegressorMixin
    """
    try:
        model = None

        if config.model_name == "linear_regression":
            model = LinearRegressionModel()
            trained_model = model.train(x_train, y_train)
            return trained_model
        else:
            raise ValueError("Model name not supported")



    except Exception as e:
        logging.error(e)
        raise e