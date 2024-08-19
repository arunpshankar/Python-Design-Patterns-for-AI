from src.config.logging import logger 
from abc import ABC, abstractmethod
from typing import Optional
from typing import Any


class InferenceStrategy(ABC):
    """
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
    Context class that dynamically selects an inference strategy based on runtime conditions.
    """
    
    def __init__(self) -> None:
        """
        Initializes the context without a predefined strategy.
        """
        self._strategy: Optional[InferenceStrategy] = None

    def select_strategy(self, data: Any, network_latency: int) -> None:
        """
        Selects an inference strategy based on the data size and network latency.

        Args:
            data (Any): The input data for inference.
            network_latency (int): The current network latency in milliseconds.
        """
        logger.info("Selecting strategy based on data size and network latency.")
        
        # Example condition to choose the strategy
        if len(data) > 100 and network_latency < 100:
            logger.info("Selected BatchInference strategy.")
            self._strategy = BatchInference()
        else:
            logger.info("Selected StreamInference strategy.")
            self._strategy = StreamInference()

    def execute_inference(self, model: Any, data: Any, network_latency: int) -> Any:
        """
        Executes inference by selecting the appropriate strategy and performing inference.

        Args:
            model (Any): The model to be used for inference.
            data (Any): The input data for inference.
            network_latency (int): The current network latency in milliseconds.
        
        Returns:
            Any: The inference result.
        """
        self.select_strategy(data, network_latency)
        if self._strategy:
            logger.info("Executing inference using the selected strategy.")
            return self._strategy.infer(model, data)
        else:
            logger.error("No strategy selected.")
            raise RuntimeError("Inference strategy could not be selected.")


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
        return f"Batch prediction for: {data}"

    def predict_stream(self, data: Any) -> str:
        """
        Simulates stream prediction.

        Args:
            data (Any): The input data for stream prediction.
        
        Returns:
            str: The stream prediction result.
        """
        return f"Stream prediction for: {data}"


if __name__ == "__main__":
    model = Model()

    # Context dynamically selects strategy based on runtime conditions
    context = InferenceContext()

    # Simulate inference with varying data size and network latency
    data_small = "small data"
    data_large = "large data " * 120  # Simulate large data by repeating the string
    network_latency_low = 50
    network_latency_high = 150

    # Execute inference
    logger.info("Executing inference with small data and high network latency.")
    logger.info(context.execute_inference(model, data_small, network_latency_high))  # Likely Stream prediction
    
    logger.info("Executing inference with large data and low network latency.")
    logger.info(context.execute_inference(model, data_large, network_latency_low))   # Likely Batch prediction
