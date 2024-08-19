from src.config.logging import logger 
from abc import abstractmethod
from typing import List
from typing import Any
from abc import ABC


class Command(ABC):
    """
    Command Interface
    Defines the structure for command classes.
    """
    @abstractmethod
    def execute(self) -> Any:
        """Executes the command."""
        raise NotImplementedError("Subclasses must implement this method.")


class Train(Command):
    """
    Concrete Command to Train a Model.
    """
    def __init__(self, model: 'Model', data: Any) -> None:
        """
        Initializes the Train command with a model and training data.
        
        :param model: The model instance to be trained.
        :param data: The training data.
        """
        self.model = model
        self.data = data

    def execute(self) -> str:
        """
        Executes the training process on the model.
        
        :return: A message indicating the model has been trained.
        """
        logger.info(f"Training model with data: {self.data}")
        return self.model.train(self.data)


class Deploy(Command):
    """
    Concrete Command to Deploy a Model.
    """
    def __init__(self, model: 'Model') -> None:
        """
        Initializes the Deploy command with a model.
        
        :param model: The model instance to be deployed.
        """
        self.model = model

    def execute(self) -> str:
        """
        Executes the deployment process for the model.
        
        :return: A message indicating the model has been deployed.
        """
        logger.info("Deploying model...")
        return deploy_model(self.model)


class Workflow:
    """
    Invoker Class to kick off the workflow.
    Manages and executes a series of commands.
    """
    def __init__(self) -> None:
        """
        Initializes the Workflow with an empty list of commands.
        """
        self._commands: List[Command] = []

    def add_command(self, command: Command) -> None:
        """
        Adds a command to the list of commands to be executed.
        
        :param command: An instance of a Command.
        """
        self._commands.append(command)

    def execute_commands(self) -> List[str]:
        """
        Executes all commands in the order they were added.
        
        :return: A list of results from each command's execution.
        """
        logger.info("Executing workflow commands...")
        results: List[str] = []
        for command in self._commands:
            results.append(command.execute())
        return results


class Model:
    """
    Model Class
    Represents a machine learning model.
    """
    def train(self, data: Any) -> str:
        """
        Simulates training the model on the provided data.
        
        :param data: The data to train the model on.
        :return: A message indicating the training was successful.
        """
        logger.info(f"Training completed with data: {data}")
        return f"Model trained on {data}"


def deploy_model(model: Model) -> str:
    """
    Simulates deploying the provided model.
    
    :param model: The model instance to deploy.
    :return: A message indicating the deployment was successful.
    """
    logger.info(f"Deployment of model: {model}")
    return f"Deployed {model}"


# Usage Example
if __name__ == "__main__":
    model = Model()
    train_command = Train(model, "training data")
    deploy_command = Deploy(model)

    invoker = Workflow()
    invoker.add_command(train_command)
    invoker.add_command(deploy_command)

    results = invoker.execute_commands()
    for result in results:
        logger.info(result)  # Output: ['Model trained on training data', 'Deployed <__main__.Model object at ...>']
