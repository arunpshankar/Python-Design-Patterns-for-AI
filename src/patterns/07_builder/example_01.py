from src.config.logging import logger 
from typing import Dict
from typing import Any


class PipelineBuilder:
    """
    A builder class for creating a machine learning pipeline with various components.
    """
    def __init__(self):
        self.pipeline: Dict[str, Any] = {}

    def add_data_loader(self, data_loader: Any) -> 'PipelineBuilder':
        """
        Adds a data loader component to the pipeline.

        :param data_loader: An instance responsible for loading data.
        :return: The current instance of PipelineBuilder for method chaining.
        """
        logger.info("Adding data loader to pipeline.")
        self.pipeline['data_loader'] = data_loader
        return self

    def add_preprocessor(self, preprocessor: Any) -> 'PipelineBuilder':
        """
        Adds a preprocessor component to the pipeline.

        :param preprocessor: An instance responsible for preprocessing data.
        :return: The current instance of PipelineBuilder for method chaining.
        """
        logger.info("Adding preprocessor to pipeline.")
        self.pipeline['preprocessor'] = preprocessor
        return self

    def add_model_trainer(self, trainer: Any) -> 'PipelineBuilder':
        """
        Adds a model trainer component to the pipeline.

        :param trainer: An instance responsible for training the model.
        :return: The current instance of PipelineBuilder for method chaining.
        """
        logger.info("Adding model trainer to pipeline.")
        self.pipeline['trainer'] = trainer
        return self

    def add_evaluator(self, evaluator: Any) -> 'PipelineBuilder':
        """
        Adds an evaluator component to the pipeline.

        :param evaluator: An instance responsible for evaluating the model.
        :return: The current instance of PipelineBuilder for method chaining.
        """
        logger.info("Adding evaluator to pipeline.")
        self.pipeline['evaluator'] = evaluator
        return self

    def build(self) -> Dict[str, Any]:
        """
        Finalizes and returns the constructed pipeline.

        :return: A dictionary representing the pipeline with all added components.
        """
        logger.info("Building the pipeline.")
        return self.pipeline

class DataLoader:
    """
    Component responsible for loading data.
    """
    def load_data(self) -> str:
        logger.info("Loading data.")
        return "data loaded"


class Preprocessor:
    """
    Component responsible for preprocessing data.
    """
    def preprocess(self, data: str) -> str:
        logger.info(f"Preprocessing data: {data}")
        return f"preprocessed {data}"


class ModelTrainer:
    """
    Component responsible for training the model on preprocessed data.
    """
    def train(self, data: str) -> str:
        logger.info(f"Training model on data: {data}")
        return f"trained model on {data}"


class Evaluator:
    """
    Component responsible for evaluating the trained model.
    """
    def evaluate(self, model: str) -> str:
        logger.info(f"Evaluating model: {model}")
        return f"evaluated {model}"


if __name__ == "__main__":
    builder = PipelineBuilder()
    pipeline = (builder
                .add_data_loader(DataLoader())
                .add_preprocessor(Preprocessor())
                .add_model_trainer(ModelTrainer())
                .add_evaluator(Evaluator())
                .build())

    # Execute Pipeline
    data = pipeline['data_loader'].load_data()
    processed_data = pipeline['preprocessor'].preprocess(data)
    trained_model = pipeline['trainer'].train(processed_data)
    evaluation = pipeline['evaluator'].evaluate(trained_model)
    logger.info(evaluation)  # Output: evaluated trained model on preprocessed data loaded
