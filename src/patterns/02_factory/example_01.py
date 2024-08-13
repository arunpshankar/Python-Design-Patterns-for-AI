class ModelFactory:
    @staticmethod
    def create_model(task_type):
        if task_type == 'classification':
            return TextClassificationModel()
        elif task_type == 'summarization':
            return SummarizationModel()
        elif task_type == 'translation':
            return TranslationModel()
        else:
            raise ValueError("Unknown task type")

# Example Models
class TextClassificationModel:
    def predict(self, text):
        return f"Classifying text: {text}"

class SummarizationModel:
    def predict(self, text):
        return f"Summarizing text: {text}"

class TranslationModel:
    def predict(self, text):
        return f"Translating text: {text}"

# Usage
model = ModelFactory.create_model('classification')
print(model.predict("This is an example text."))  # Output: Classifying text: This is an example text.
