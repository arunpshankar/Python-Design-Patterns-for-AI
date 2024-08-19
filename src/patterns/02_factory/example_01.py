from src.config.logging import logger 
from abc import ABC, abstractmethod
from typing import Any 


class BaseModel(ABC):
    def __init__(self, model_name: str = 'base_model', pretrained: bool = False) -> None:
        """
        Initialize the base model.

        Args:
            model_name (str): The name of the model.
            pretrained (bool): Flag to indicate if pre-trained weights should be loaded.
        """
        self.model_name = model_name
        self.pretrained = pretrained
        
        self._initialize_model()

    def _initialize_model(self) -> None:
        """
        Initializes the model, either by loading pre-trained weights or initializing from scratch.
        """
        if self.pretrained:
            logger.info(f"Loading pre-trained weights for {self.model_name}")
            # Here, you would load the actual model weights.
        else:
            logger.info(f"Initializing {self.model_name} from scratch")
            # Here, you would initialize the model's parameters.

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


class TextClassificationModel(BaseModel):
    """
    Model for text classification tasks.
    """
    def predict(self, text: str) -> str:
        """
        Predicts the class of the input text.

        Args:
            text (str): The input text for classification.
        
        Returns:
            str: The classification result.
        """
        # Replace with actual classification logic.
        return f"Classifying text with {self.model_name}: {text}"


class SummarizationModel(BaseModel):
    """
    Model for text summarization tasks.
    """
    def predict(self, text: str) -> str:
        """
        Summarizes the input text.

        Args:
            text (str): The input text to be summarized.
        
        Returns:
            str: The summarization result.
        """
        # Replace with actual summarization logic.
        return f"Summarizing text with {self.model_name}: {text}"


class TranslationModel(BaseModel):
    """
    Model for text translation tasks.
    """
    def predict(self, text: str) -> str:
        """
        Translates the input text.

        Args:
            text (str): The input text to be translated.
        
        Returns:
            str: The translation result.
        """
        # Replace with actual translation logic.
        return f"Translating text with {self.model_name}: {text}"


class ModelFactory:
    """
    Factory class to create models based on the task type.
    """
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
        
        task_map: dict[str, Type[BaseModel]] = {
            'classification': TextClassificationModel,
            'summarization': SummarizationModel,
            'translation': TranslationModel
        }
        
        model_class = task_map.get(task_type)
        
        if model_class is None:
            logger.error(f"Unknown task type: {task_type}")
            raise ValueError(f"Unknown task type: {task_type}")
        
        return model_class(**kwargs)


if __name__ == "__main__":
    try:
        classification_model = ModelFactory.create_model('classification', model_name='bert_classifier', pretrained=True)
        logger.info(classification_model.predict("This is an example text."))

        summarization_model = ModelFactory.create_model('summarization', model_name='gpt_summarizer', pretrained=False)
        logger.info(summarization_model.predict("This is a long article that needs summarization."))
    except ValueError as e:
        logger.error(f"Error occurred: {e}")
