"""
This is a boilerplate pipeline 'data_fetching'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            lambda x: print(x.head()),
            inputs='dji_stock',
            outputs=None
        )
    ])
