from src.config.logging import logger 
from typing import Callable


def validate_data(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator that validates the input data before processing.

    Args:
        func (Callable[[str], str]): The function to be decorated.

    Returns:
        Callable[[str], str]: The wrapped function with additional validation logic.
    """
    def wrapper(data: str) -> str:
        logger.info("Validating data...")
        
        # Check if the data is a non-empty string
        if not isinstance(data, str) or not data.strip():
            logger.error("Invalid data: Input must be a non-empty string.")
            raise ValueError("Invalid data: Input must be a non-empty string.")
        
        # If validation passes, call the original function
        logger.info("Data validation passed.")
        return func(data)
    
    return wrapper

def augment_data(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator that augments the output of a data processing function.

    Args:
        func (Callable[[str], str]): The function to be decorated.

    Returns:
        Callable[[str], str]: The wrapped function with additional augmentation logic.
    """
    def wrapper(data: str) -> str:
        logger.info("Processing data...")
        
        # Call the original function to process the data
        processed_data = func(data)
        
        # Augment the processed data with additional information
        augmented_data = f"{processed_data} + augmented"
        logger.info("Data processed and augmented.")
        
        # Return the augmented data
        return augmented_data
    
    return wrapper


@validate_data
@augment_data
def preprocess_data(data: str) -> str:
    """
    Function to preprocess the given data by cleaning it.

    Args:
        data (str): The raw input data to be cleaned.

    Returns:
        str: The cleaned data.
    """
    cleaned_data = f"cleaned {data.strip()}"
    logger.info(f"Data cleaned: {cleaned_data}")
    return cleaned_data


if __name__ == "__main__":
    try:
        raw_data = " raw_data "
        
        # Process the raw data using the decorated preprocess_data function
        processed_data = preprocess_data(raw_data)
        
        # Output the processed and augmented data
        logger.info(f"Final Output: {processed_data}")  # Output: cleaned raw_data + augmented
        
        # Uncommenting the following line will raise a ValueError due to invalid data
        # invalid_data = ""
        # preprocess_data(invalid_data)

    except ValueError as e:
        logger.error(f"Error: {e}")
