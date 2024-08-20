from src.config.logging import logger 
from abc import abstractmethod
from typing import Type
from abc import ABC


class State(ABC):
    """
    Abstract base class for different states in the training process.
    Each state should implement the handle method to define its behavior.
    """
    
    @abstractmethod
    def handle(self, context: 'Context') -> None:
        """
        Handle the state-specific behavior.
        
        Args:
            context (Context): The context in which the state operates.
        """
        raise NotImplementedError("Must override handle method in the subclass")


class DataLoadingState(State):
    def handle(self, context: 'Context') -> None:
        logger.info("State: DataLoadingState - Loading data")
        context.load_data()
        context.state = TrainingState()


class TrainingState(State):
    def handle(self, context: 'Context') -> None:
        logger.info("State: TrainingState - Training model")
        context.train_model()
        context.state = ValidationState()


class ValidationState(State):
    def handle(self, context: 'Context') -> None:
        logger.info("State: ValidationState - Validating model")
        context.validate_model()
        context.state = DeploymentState()


class DeploymentState(State):
    def handle(self, context: 'Context') -> None:
        logger.info("State: DeploymentState - Deploying model")
        context.deploy_model()
        logger.info("Model deployed successfully")


class Context:
    """
    The Context class manages the current state and provides methods 
    to interact with the state.
    """
    
    def __init__(self, state: Type[State]) -> None:
        self.state: Type[State] = state

    def load_data(self) -> None:
        logger.info("Loading data...")

    def train_model(self) -> None:
        logger.info("Training model...")

    def validate_model(self) -> None:
        logger.info("Validating model...")

    def deploy_model(self) -> None:
        logger.info("Deploying model...")

    def request(self) -> None:
        """
        Request the current state to handle its behavior and transition to the next state.
        """
        self.state.handle(self)


if __name__ == "__main__":
    context = Context(DataLoadingState())
    context.request() 
    context.request()  
    context.request()  
    context.request()  
