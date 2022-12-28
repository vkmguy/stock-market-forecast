"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.4
"""

import logging
from typing import Dict, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from keras.layers import Dense
from tensorflow.core.protobuf.saved_model_pb2 import SavedModel
from tensorflow.python.keras import Sequential


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters.yml.
    Returns:
        Split data.
    """
    X = data.loc[:, parameters['features']]
    y = data.loc[:, 'direction']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series,X_test: pd.DataFrame, y_test: pd.Series) -> Sequential:
    """Trains the linear regression model.

    Args:
        y_test:
        X_test:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    # Build the model
    model = Sequential()
    model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train)

    # Test the model
    scores = model.evaluate(X_test, y_test)
    logger = logging.getLogger(__name__)
    logger.info("Model has a accuracy of %.3f on test data.", scores[1])
    return model


def evaluate_model(
        model: SavedModel, X_test: pd.DataFrame, y_test: pd.Series
):
    """Calculates and logs the coefficient of determination.

    Args:
        model: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    # model = keras.models.load_model(model)
    # scores = model.predict(X_test, y_test)
    # logger = logging.getLogger(__name__)
    # logger.info("Model has a accuracy of %.3f on test data.", scores[1])
