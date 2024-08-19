from src.config.logging import logger 
from typing import Protocol


class LanguageModel(Protocol):
    """
    Protocol defining the interface for third-party Large Language Models (LLMs).
    """
    def get_prediction(self, text: str) -> str:
        ...


class CohereLLM:
    """
    A mock representation of the Cohere Language Model.
    """
    def get_prediction(self, text: str) -> str:
        return f"Response from CohereLLM for: {text}"


class AnthropicLLM:
    """
    A mock representation of the Anthropic Language Model.
    """
    def get_prediction(self, text: str) -> str:
        return f"Response from AnthropicLLM for: {text}"


class LLMAdapter:
    """
    Adapter class to unify the interface of various third-party LLMs.
    
    This adapter standardizes how predictions are fetched from different LLMs.
    """
    def __init__(self, llm: LanguageModel):
        """
        Initializes the adapter with an instance of a third-party LLM.
        
        :param llm: An instance of a third-party LLM implementing the LanguageModel interface.
        """
        self.llm = llm

    def predict(self, text: str) -> str:
        """
        Standardized method for getting predictions from the third-party LLM.
        
        :param text: The input text for which a prediction is required.
        :return: A standardized response from the LLM.
        """
        if not text:
            logger.error("Input text is empty.")
            return "Error: Input text cannot be empty."

        logger.info(f"Fetching prediction for input: '{text}'")
        response = self.llm.get_prediction(text)
        logger.info(f"Received response: '{response}'")
        return response


if __name__ == "__main__":
    # Initialize third-party models
    cohere_model = CohereLLM()
    anthropic_model = AnthropicLLM()

    # Create adapters for each model
    cohere_adapter = LLMAdapter(cohere_model)
    anthropic_adapter = LLMAdapter(anthropic_model)

    # Use the adapters
    cohere_adapter.predict("Input for Cohere model")
    anthropic_adapter.predict("Input for Anthropic model")
