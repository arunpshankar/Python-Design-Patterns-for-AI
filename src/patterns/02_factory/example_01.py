from src.config.logging import logger 
from abc import ABC, abstractmethod
from typing import Any, Type

# Base model definition using abstract base class
class BaseModel(ABC):
    def __init__(self, model_name: str = 'base_model', pretrained: bool = False) -> None:
        """
        Initializes the base model.

        Args:
            model_name (str): The name of the model.
            pretrained (bool): Flag to indicate if pre-trained weights should be loaded.
        """
        self.model_name = model_name
        self.pretrained = pretrained
        
        if self.pretrained:
            logger.info(f"Loading pre-trained weights for {self.model_name}")
        else:
            logger.info(f"Initializing {self.model_name} from scratch")

    @abstractmethod
    def predict(self, text: str) -> Any:
        """
        Abstract method to be implemented by subclasses for text prediction.

        Args:
            text (str): The input text for prediction.
        
        Returns:
            Any: The prediction result.
        """
        raise NotImplementedError("Subclasses must implement the predict method")

# Subclass for text classification tasks
class TextClassificationModel(BaseModel):
    def predict(self, text: str) -> str:
        """
        Predicts the class of the input text.

        Args:
            text (str): The input text for classification.
        
        Returns:
            str: The classification result.
        """
        logger.info(f"Classifying text with {self.model_name}")
        return f"Classifying text with {self.model_name}: {text}"

# Subclass for text summarization tasks
class SummarizationModel(BaseModel):
    def predict(self, text: str) -> str:
        """
        Summarizes the input text.

        Args:
            text (str): The input text to be summarized.
        
        Returns:
            str: The summarization result.
        """
        logger.info(f"Summarizing text with {self.model_name}")
        return f"Summarizing text with {self.model_name}: {text}"

# Subclass for text translation tasks
class TranslationModel(BaseModel):
    def predict(self, text: str) -> str:
        """
        Translates the input text.

        Args:
            text (str): The input text to be translated.
        
        Returns:
            str: The translation result.
        """
        logger.info(f"Translating text with {self.model_name}")
        return f"Translating text with {self.model_name}: {text}"

# Factory class to create models based on task type
class ModelFactory:
    @staticmethod
    def create_model(task_type: str, **kwargs: Any) -> BaseModel:
        """
        Factory method to create models based on the task type.

        Args:
            task_type (str): The type of task ('classification', 'summarization', 'translation').
            **kwargs (Any): Additional arguments to pass to the model's constructor.
        
        Returns:
            BaseModel: An instance of a model subclass.
        
        Raises:
            ValueError: If the task type is unknown.
        """
        logger.info(f"Creating model for task type: {task_type}")
        
        if task_type == 'classification':
            return TextClassificationModel(**kwargs)
        elif task_type == 'summarization':
            return SummarizationModel(**kwargs)
        elif task_type == 'translation':
            return TranslationModel(**kwargs)
        else:
            logger.error(f"Unknown task type: {task_type}")
            raise ValueError("Unknown task type")

# Example usage
if __name__ == "__main__":
    classification_model = ModelFactory.create_model('classification', model_name='bert_classifier', pretrained=True)
    print(classification_model.predict("This is an example text."))  # Output: Classifying text with bert_classifier: This is an example text.

    summarization_model = ModelFactory.create_model('summarization', model_name='gpt_summarizer', pretrained=False)
    print(summarization_model.predict("This is a long article that needs summarization."))  # Output: Summarizing text with gpt_summarizer: This is a long article that needs summarization.
