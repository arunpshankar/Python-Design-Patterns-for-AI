from src.config.logging import logger 
from abc import ABC, abstractmethod
from typing import Any


class InferenceStrategy(ABC):
    """
    Define the Strategy interface.

    Abstract base class for defining inference strategies.
    """
    
    @abstractmethod
    def infer(self, model: Any, data: Any) -> Any:
        """
        Abstract method for performing inference.

        Args:
            model (Any): The model to be used for inference.
            data (Any): The input data for inference.
        
        Returns:
            Any: The inference result.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement the infer method.")


class BatchInference(InferenceStrategy):
    """
    Concrete strategy for batch inference.
    """
    
    def infer(self, model: Any, data: Any) -> Any:
        """
        Performs batch inference using the model.

        Args:
            model (Any): The model to be used for batch inference.
            data (Any): The input data for batch inference.
        
        Returns:
            Any: The batch inference result.
        """
        logger.info("Performing batch inference.")
        return model.predict_batch(data)


class StreamInference(InferenceStrategy):
    """
    Concrete strategy for stream inference.
    """
    
    def infer(self, model: Any, data: Any) -> Any:
        """
        Performs stream inference using the model.

        Args:
            model (Any): The model to be used for stream inference.
            data (Any): The input data for stream inference.
        
        Returns:
            Any: The stream inference result.
        """
        logger.info("Performing stream inference.")
        return model.predict_stream(data)


class InferenceContext:
    """
    Context class that uses an inference strategy.
    """
    
    def __init__(self, strategy: InferenceStrategy) -> None:
        """
        Initializes the context with a specific inference strategy.

        Args:
            strategy (InferenceStrategy): The inference strategy to be used.
        """
        self._strategy = strategy
        logger.info(f"Strategy set to {type(strategy).__name__}")

    def set_strategy(self, strategy: InferenceStrategy) -> None:
        """
        Sets a new inference strategy.

        Args:
            strategy (InferenceStrategy): The new inference strategy to be used.
        """
        self._strategy = strategy
        logger.info(f"Strategy set to {type(strategy).__name__}")

    def execute_inference(self, model: Any, data: Any) -> Any:
        """
        Executes inference using the current strategy.

        Args:
            model (Any): The model to be used for inference.
            data (Any): The input data for inference.
        
        Returns:
            Any: The inference result.
        """
        logger.info("Executing inference using the current strategy.")
        return self._strategy.infer(model, data)


class Model:
    """
    Example model class with different prediction methods.
    """
    
    def predict_batch(self, data: Any) -> str:
        """
        Simulates batch prediction.

        Args:
            data (Any): The input data for batch prediction.
        
        Returns:
            str: The batch prediction result.
        """
        return f"Batch prediction for {data}"

    def predict_stream(self, data: Any) -> str:
        """
        Simulates stream prediction.

        Args:
            data (Any): The input data for stream prediction.
        
        Returns:
            str: The stream prediction result.
        """
        return f"Stream prediction for {data}"


if __name__ == "__main__":
    model = Model()
    context = InferenceContext(BatchInference())
    logger.info(context.execute_inference(model, "input data"))  # Output: Batch prediction for input data

    context.set_strategy(StreamInference())
    logger.info(context.execute_inference(model, "input data"))  # Output: Stream prediction for input data