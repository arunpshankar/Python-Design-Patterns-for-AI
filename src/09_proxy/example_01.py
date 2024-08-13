class LLMProxy:
    def __init__(self, model):
        self.model = model
        self.cache = {}

    def predict(self, input_text):
        if input_text in self.cache:
            return self.cache[input_text]

        response = self.model.predict(input_text)
        self.cache[input_text] = response
        return response

# Example Model
class ExampleModel:
    def predict(self, text):
        return f"Prediction for {text}"

# Usage
model = ExampleModel()
proxy = LLMProxy(model)

# First call (cache miss)
response1 = proxy.predict("Some input text")
print(response1)  # Output: Prediction for Some input text

# Second call (cache hit)
response2 = proxy.predict("Some input text")
print(response2)  # Output: Prediction for Some input text
