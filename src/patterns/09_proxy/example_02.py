from src.config.logging import logger
from typing import Callable
from functools import wraps
from typing import Tuple
from typing import Dict
from typing import Any


def cache_decorator(func: Callable) -> Callable:
    """
    A decorator to cache the results of a function based on its arguments.
    """
    cache: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function that checks the cache before executing the function.
        
        :param args: Positional arguments for the function.
        :param kwargs: Keyword arguments for the function.
        :return: The result from the cache or the function execution.
        """
        # Create a cache key based on function arguments
        key = args + tuple(sorted(kwargs.items()))
        logger.info(f"Cache decorator called with key: {key}")

        if key in cache:
            logger.info(f"Cache hit for key: {key}")
            return cache[key]
        
        logger.info(f"Cache miss for key: {key}. Calling the function.")
        # Call the function and store the result in cache
        result = func(*args, **kwargs)
        cache[key] = result
        logger.info(f"Result cached for key: {key}")
        return result
    
    return wrapper


class Model:
    """
    Example Model class that simulates a prediction based on input text.
    """
    def __init__(self) -> None:
        """
        Initializes the Model.
        """
        logger.info("Initializing Model.")

    @cache_decorator
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

    # Cache miss
    response1 = model.predict("Some input text")
    logger.info(f"First response: {response1}")  # Output: Prediction for Some input text

    # Cache hit
    response2 = model.predict("Some input text")
    logger.info(f"Second response: {response2}")  # Output: Prediction for Some input text
