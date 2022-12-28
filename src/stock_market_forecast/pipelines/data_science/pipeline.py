"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from stock_market_forecast.pipelines.data_science.nodes import split_data, train_model, evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs=["model_input_table", "parameters"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node",
        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train", "X_test", "y_test"],
            outputs="tensorflow_model",
            name="train_model_node",
        ),
        # node(
        #     func=evaluate_model,
        #     inputs=["tensorflow_model", "X_test", "y_test"],
        #     outputs=None,
        #     name="evaluate_model_node",
        # ),
    ])
