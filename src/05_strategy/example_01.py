from abc import ABC, abstractmethod

# Define the Strategy interface
class InferenceStrategy(ABC):
    @abstractmethod
    def infer(self, model, data):
        pass

# Concrete strategy for batch inference
class BatchInference(InferenceStrategy):
    def infer(self, model, data):
        return model.predict_batch(data)

# Concrete strategy for stream inference
class StreamInference(InferenceStrategy):
    def infer(self, model, data):
        return model.predict_stream(data)

# Context class that uses a strategy
class InferenceContext:
    def __init__(self, strategy: InferenceStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: InferenceStrategy):
        self._strategy = strategy

    def execute_inference(self, model, data):
        return self._strategy.infer(model, data)

# Example model with different prediction methods
class Model:
    def predict_batch(self, data):
        return f"Batch prediction for {data}"

    def predict_stream(self, data):
        return f"Stream prediction for {data}"

# Usage
model = Model()
context = InferenceContext(BatchInference())
print(context.execute_inference(model, "input data"))  # Output: Batch prediction for input data

context.set_strategy(StreamInference())
print(context.execute_inference(model, "input data"))  # Output: Stream prediction for input data


"""
Imagine a payment processing system where you need to support multiple payment methods like credit card, PayPal, and cryptocurrency. 
Instead of handling all these payment methods in one large class with many conditional checks, you can use the Strategy pattern. 
Each payment method becomes a strategy, and the context (payment processor) can switch between them based on user choice.
"""