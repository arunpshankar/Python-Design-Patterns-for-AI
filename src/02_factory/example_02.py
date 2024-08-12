class ModelFactory:
    @staticmethod
    def create_model(task_type, **kwargs):
        if task_type == 'classification':
            return TextClassificationModel(**kwargs)
        elif task_type == 'summarization':
            return SummarizationModel(**kwargs)
        elif task_type == 'translation':
            return TranslationModel(**kwargs)
        else:
            raise ValueError("Unknown task type")

# Example Models
class TextClassificationModel:
    def __init__(self, model_name='default_classifier', pretrained=False):
        self.model_name = model_name
        self.pretrained = pretrained
        if self.pretrained:
            print(f"Loading pre-trained weights for {self.model_name}")
        else:
            print(f"Initializing {self.model_name} from scratch")

    def predict(self, text):
        return f"Classifying text with {self.model_name}: {text}"

class SummarizationModel:
    def __init__(self, model_name='default_summarizer', pretrained=False):
        self.model_name = model_name
        self.pretrained = pretrained
        if self.pretrained:
            print(f"Loading pre-trained weights for {self.model_name}")
        else:
            print(f"Initializing {self.model_name} from scratch")

    def predict(self, text):
        return f"Summarizing text with {self.model_name}: {text}"

class TranslationModel:
    def __init__(self, model_name='default_translator', pretrained=False):
        self.model_name = model_name
        self.pretrained = pretrained
        if self.pretrained:
            print(f"Loading pre-trained weights for {self.model_name}")
        else:
            print(f"Initializing {self.model_name} from scratch")

    def predict(self, text):
        return f"Translating text with {self.model_name}: {text}"

# Usage
model = ModelFactory.create_model('classification', model_name='bert_classifier', pretrained=True)
print(model.predict("This is an example text."))  # Output: Classifying text with bert_classifier: This is an example text.

model = ModelFactory.create_model('summarization', model_name='gpt_summarizer', pretrained=False)
print(model.predict("This is a long article that needs summarization."))  # Output: Summarizing text with gpt_summarizer: This is a long article that needs summarization.