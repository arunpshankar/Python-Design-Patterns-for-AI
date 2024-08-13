from abc import ABC, abstractmethod

class TrainingState(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class DataLoadingState(TrainingState):
    def handle(self, context):
        context.load_data()
        context.state = TrainingState()

class TrainingState(TrainingState):
    def handle(self, context):
        context.train_model()
        context.state = ValidationState()

class ValidationState(TrainingState):
    def handle(self, context):
        context.validate_model()
        context.state = DeploymentState()

class DeploymentState(TrainingState):
    def handle(self, context):
        context.deploy_model()
        print("Model deployed successfully")

class Context:
    def __init__(self, state: TrainingState):
        self.state = state

    def load_data(self):
        print("Loading data...")

    def train_model(self):
        print("Training model...")

    def validate_model(self):
        print("Validating model...")

    def deploy_model(self):
        print("Deploying model...")

    def request(self):
        self.state.handle(self)

# Usage
context = Context(DataLoadingState())
context.request()  # Transitions to TrainingState
context.request()  # Transitions to ValidationState
context.request()  # Transitions to DeploymentState
context.request()  # Output: Model deployed successfully
