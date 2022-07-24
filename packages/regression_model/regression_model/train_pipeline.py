import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
import sys
sys.path.append('/tf/packages/regression_model/')
#print(sys.path)
from regression_model.processing.data_management import(
    load_dataset, save_pipeline)

from regression_model.config import config

import regression_model.pipeline as pipeline



_logger = logging.getLogger(__name__)


def run_training() -> None:
    """Train the model."""

    print('Training...')

    # read the training data

    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    x_train, x_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.1,
        random_state=0
    )
    
    y_train = np.log(y_train)
    y_test = np.log(y_test)

    pipeline.price_pipe.fit(x_train[config.FEATURES], y_train)

    save_pipeline(pipeline_to_persist=pipeline.price_pipe)




if __name__ == "__main__":
    run_training()
    print("model trained")
