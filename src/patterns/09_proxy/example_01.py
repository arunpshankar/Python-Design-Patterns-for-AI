from src.config.logging import logger
from typing import Dict


class LLMProxy:
    """
    Proxy class for interacting with a language model.
    Caches results to optimize repeated predictions.
    """
    def __init__(self, model: 'Model') -> None:
        """
        Initializes the LLMProxy with a model and an empty cache.
        
        :param model: The model instance to interact with.
        """
        logger.info("Initializing LLMProxy.")
        self.model = model
        self.cache: Dict[str, str] = {}

    def predict(self, input_text: str) -> str:
        """
        Predicts the output for the given input text using the model.
        Caches the result to avoid redundant computations for repeated inputs.
        
        :param input_text: The input text for which the prediction is to be made.
        :return: The model's prediction.
        """
        logger.info(f"Received request for prediction with input: {input_text}")

        if input_text in self.cache:
            logger.info(f"Cache hit for input: {input_text}")
            return self.cache[input_text]
        
        logger.info(f"Cache miss for input: {input_text}. Predicting using model.")
        response = self.model.predict(input_text)
        logger.info(f"Caching prediction for input: {input_text}")
        self.cache[input_text] = response
        return response


class Model:
    """
    Example Model class representing a simple predictive model.
    """
    def predict(self, text: str) -> str:
        """
        Simulates making a prediction based on the input text.
        
        :param text: The input text for which the prediction is to be made.
        :return: A simulated prediction result.
        """
        logger.info(f"Model received input for prediction: {text}")
        return f"Prediction for {text}"


if __name__ == "__main__":
    model = Model()
    proxy = LLMProxy(model)

    # First call (cache miss)
    response1 = proxy.predict("Some input text")
    logger.info(f"First response: {response1}")  # Output: Prediction for Some input text

    # Second call (cache hit)
    response2 = proxy.predict("Some input text")
    logger.info(f"Second response: {response2}")  # Output: Prediction for Some input text
