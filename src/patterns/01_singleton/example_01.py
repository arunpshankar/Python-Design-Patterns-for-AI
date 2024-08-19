from src.config.logging import logger
from typing import Optional


class ModelConfig:
    """
    Singleton class to manage model configuration. This class ensures that only one instance of the 
    configuration is created and shared across the application.
    """
    
    _instance: Optional['ModelConfig'] = None  # Class-level variable to hold the single instance

    def __new__(cls, *args, **kwargs) -> 'ModelConfig':
        """
        Overrides the __new__ method to control the creation of a new instance. 
        Ensures that only one instance of the class is created (Singleton pattern).

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        
        Returns:
            ModelConfig: The single instance of ModelConfig.
        """
        if cls._instance is None:
            logger.info("Creating a new instance of ModelConfig.")
            cls._instance = super(ModelConfig, cls).__new__(cls, *args, **kwargs)
            cls.model_name = "Gemini Pro 1.5"
            cls.model_path = "/models/gemini"
            cls.api_key = "xyz-abc-123"
        else:
            logger.info("Returning existing instance of ModelConfig.")
        
        return cls._instance


if __name__ == "__main__":
    # Creating the first instance of ModelConfig
    config1 = ModelConfig()
    logger.info(f"Config1 Instance: {config1}")
    logger.info(f"Model Name: {config1.model_name}")

    # Attempting to create a second instance, should return the same instance as config1
    config2 = ModelConfig()
    logger.info(f"Config2 Instance: {config2}")

    # Asserting that both variables point to the same instance
    assert config1 is config2
    logger.info("Config1 and Config2 are the same instance.")

    # Logging model name from the singleton instance
    logger.info(f"Model Name from Config1: {config1.model_name}")
