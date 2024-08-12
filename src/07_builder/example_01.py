class TrainingPipelineBuilder:
    def __init__(self):
        self.pipeline = {}

    def add_data_loader(self, data_loader):
        self.pipeline['data_loader'] = data_loader
        return self

    def add_preprocessor(self, preprocessor):
        self.pipeline['preprocessor'] = preprocessor
        return self

    def add_model_trainer(self, trainer):
        self.pipeline['trainer'] = trainer
        return self

    def add_evaluator(self, evaluator):
        self.pipeline['evaluator'] = evaluator
        return self

    def build(self):
        return self.pipeline

# Example Pipeline Components
class DataLoader:
    def load_data(self):
        return "data loaded"

class Preprocessor:
    def preprocess(self, data):
        return f"preprocessed {data}"

class ModelTrainer:
    def train(self, data):
        return f"trained model on {data}"

class Evaluator:
    def evaluate(self, model):
        return f"evaluated {model}"

# Usage
builder = TrainingPipelineBuilder()
pipeline = builder.add_data_loader(DataLoader()).add_preprocessor(Preprocessor()).add_model_trainer(ModelTrainer()).add_evaluator(Evaluator()).build()

# Execute Pipeline
data = pipeline['data_loader'].load_data()
processed_data = pipeline['preprocessor'].preprocess(data)
trained_model = pipeline['trainer'].train(processed_data)
evaluation = pipeline['evaluator'].evaluate(trained_model)

print(evaluation)  # Output: evaluated trained model on preprocessed data loaded
