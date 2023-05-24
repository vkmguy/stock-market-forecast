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
    percentage_change = stockData['adjusted_close'].shift(1) / stockData['adjusted_close'] - 1
    return stockData.assign(percentage_change=percentage_change,
                            direction=percentage_change.apply(lambda x: 1 if x > 0 else 0).shift(1))


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
    # stratified shuffled split
    stockData['date'] = pd.to_datetime(stockData['date'])
    stockData.set_index('date', inplace=True)
    twitterData['date'] = pd.to_datetime(twitterData['date'])
    twitterData.set_index('date', inplace=True)
    merged_data = pd.merge(stockData, twitterData, how='inner', on='date')
    model_input_table = merged_data.dropna()
    # use logging to find out the dropped rows - IMPORTANT
    # Try using data from friday stock prices to fill in sat, sun - manage data first in the orignal data
    return model_input_table
