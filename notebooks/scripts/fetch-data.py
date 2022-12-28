import pandas as pd
from kedro.extras.datasets.api import APIDataSet

index_values = {'DJI.INDX': 'DJI.INDX',
                'DJI': 'DJI.US',
                'AAPL': 'AAPL.US'}


def get_tweet(stock, start_date, end_date, api_key, filepath, filename):
    dataset = APIDataSet(
        url="https://eodhistoricaldata.com/api/tweets-sentiments",
        params={
            'api_token': f'{api_key}',
            's': f'{stock}',
            'from': f'{start_date}',
            'to': f'{end_date}'
        }
    )
    dji_tweet_sentiment_data = dataset.load()
    dji_tweet_df = pd.DataFrame.from_dict(dji_tweet_sentiment_data[index_values[stock]])
    with open(f"{filepath}/{filename}.csv", "w", newline="", encoding='utf-8') as csvfile:
        dji_tweet_df.to_csv(csvfile)


def get_news(stock, start_date, end_date, api_key, filepath, filename):
    dataset = APIDataSet(
        url="https://eodhistoricaldata.com/api/sentiments",
        params={
            'api_token': f'{api_key}',
            's': f'{stock}',
            'from': f'{start_date}',
            'to': f'{end_date}'
        }
    )
    dji_tweet_sentiment_data = dataset.load()
    dji_tweet_df = pd.DataFrame.from_dict(dji_tweet_sentiment_data[stock])
    with open(f"{filepath}/{filename}.csv", "w", newline="", encoding='utf-8') as csvfile:
        dji_tweet_df.to_csv(csvfile)


def get_stock_data(stock, start_date, end_date, api_key, filepath, filename, offset=0):
    dataset = APIDataSet(
        url=f'https://eodhistoricaldata.com/api/eod/{stock}',
        params={
            'api_token': f'{api_key}',
            's': f'{stock}',
            'fmt': 'json',
            'period': 'd',
            'from': f'{start_date}',
            'to': f'{end_date}',
        }
    )
    stock_index_data = dataset.load()
    # Check the status code to make sure the request was successful
    if stock_index_data.status_code == 200:
        # Convert the response to a JSON object
        stock_index_data = stock_index_data.json()

        # Convert the JSON object to a DataFrame
        stock_indx_df = pd.DataFrame.from_dict(stock_index_data)

        # Display the DataFrame
        print(stock_indx_df.head())
    else:
        print('Request failed')
    with open(f"{filepath}/{filename}.csv", "w", newline="", encoding='utf-8') as csvfile:
        stock_indx_df.to_csv(csvfile)
