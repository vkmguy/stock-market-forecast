"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from stock_market_forecast.pipelines.data_processing.nodes import preprocess_stock_data, preprocess_twitter_data, \
    create_model_input_table


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=preprocess_stock_data,
             inputs="dji_stock",
             outputs="processed_stock_data",
             name="processed_stock_data_node"
             ),
        node(func=preprocess_twitter_data,
             inputs="dji_tweets",
             outputs="processed_twitter_data",
             name="processed_twitter_data_node"
             ),
        node(
            func=create_model_input_table,
            inputs=["processed_stock_data", "processed_twitter_data"],
            outputs="model_input_table",
            name="create_model_input_table_node",
        ),
    ])
