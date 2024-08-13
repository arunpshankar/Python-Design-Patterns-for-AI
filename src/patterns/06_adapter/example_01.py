class ThirdPartyLLM1:
    """
    A mock representation of the first third-party Language Model (LLM).
    """
    def get_prediction(self, text: str) -> str:
        return f"Response from ThirdPartyLLM1: {text}"

class ThirdPartyLLM2:
    """
    A mock representation of the second third-party Language Model (LLM).
    """
    def get_prediction(self, text: str) -> str:
        return f"Response from ThirdPartyLLM2: {text}"

class LLMAdapter:
    """
    Adapter class to unify the interface of various third-party LLMs.
    """
    def __init__(self, llm):
        """
        Initializes the adapter with an instance of a third-party LLM.
        """
        self.llm = llm

    def predict(self, text: str) -> str:
        """
        Standardizes the method for getting predictions from the third-party LLM.
        """
        return self.llm.get_prediction(text)

# Usage
if __name__ == "__main__":
    # Initialize third-party models
    third_party_model1 = ThirdPartyLLM1()
    third_party_model2 = ThirdPartyLLM2()

    # Create adapters for each model
    adapter1 = LLMAdapter(third_party_model1)
    adapter2 = LLMAdapter(third_party_model2)

    # Use the adapters
    response1 = adapter1.predict("Input for model 1")
    response2 = adapter2.predict("Input for model 2")

    print(response1)  # Output: Response from ThirdPartyLLM1: Input for model 1
    print(response2)  # Output: Response from ThirdPartyLLM2: Input for model 2
