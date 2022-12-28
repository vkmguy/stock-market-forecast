"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
import pandas as pd


def preprocess_stock_data(stockData: pd.DataFrame) -> pd.DataFrame:
    """

    Args:
        stockData:

    Returns:

    """
    stockData["pct_change"] = stockData['adjusted_close'].shift(1) / stockData['adjusted_close'] - 1
    stockData['direction'] = stockData['pct_change'].apply(lambda x: 1 if x > 0 else 0)
    stockData['direction'] = stockData['direction'].shift(1)
    return stockData


def preprocess_twitter_data(twitterData: pd.DataFrame) -> pd.DataFrame:
    """

    Args:
        twitterData:

    Returns:

    """
    return twitterData


def create_model_input_table(
    stockData: pd.DataFrame, twitterData: pd.DataFrame
) -> pd.DataFrame:
    """Combines all data to create a model input table.

    Args:
        stockData: Preprocessed data for shuttles.
        twitterData: Preprocessed data for companies.
    Returns:
        model input table.

    """
    stockData['date'] = pd.to_datetime(stockData['date'])
    stockData.set_index('date', inplace=True)
    twitterData['date'] = pd.to_datetime(twitterData['date'])
    twitterData.set_index('date', inplace=True)
    merged_data = pd.merge(stockData, twitterData, how='inner', on='date')
    model_input_table = merged_data.dropna()
    return model_input_table
