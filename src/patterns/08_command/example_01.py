from src.config.logging import logger
from abc import abstractmethod
from typing import List, Any
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
        logger.info(f"Initializing Train command with model: {model} and data: {data}")
        self.model = model
        self.data = data

    def execute(self) -> str:
        """
        Executes the training process on the model.
        
        :return: A message indicating the model has been trained.
        """
        logger.info(f"Executing Train command. Training model: {self.model} with data: {self.data}")
        result = self.model.train(self.data)
        logger.info(f"Train command execution completed. Result: {result}")
        return result


class Deploy(Command):
    """
    Concrete Command to Deploy a Model.
    """
    def __init__(self, model: 'Model') -> None:
        """
        Initializes the Deploy command with a model.
        
        :param model: The model instance to be deployed.
        """
        logger.info(f"Initializing Deploy command with model: {model}")
        self.model = model

    def execute(self) -> str:
        """
        Executes the deployment process for the model.
        
        :return: A message indicating the model has been deployed.
        """
        logger.info(f"Executing Deploy command. Deploying model: {self.model}")
        result = self.model.deploy()
        logger.info(f"Deploy command execution completed. Result: {result}")
        return result


class Workflow:
    """
    Invoker Class to kick off the workflow.
    Manages and executes a series of commands.
    """
    def __init__(self) -> None:
        """
        Initializes the Workflow with an empty list of commands.
        """
        logger.info("Initializing Workflow with an empty command list.")
        self._commands: List[Command] = []

    def add_command(self, command: Command) -> None:
        """
        Adds a command to the list of commands to be executed.
        
        :param command: An instance of a Command.
        """
        logger.info(f"Adding command to Workflow: {command}")
        self._commands.append(command)

    def execute_commands(self) -> List[str]:
        """
        Executes all commands in the order they were added.
        
        :return: A list of results from each command's execution.
        """
        logger.info("Executing all commands in the Workflow.")
        results: List[str] = []
        for command in self._commands:
            logger.info(f"Executing command: {command}")
            result = command.execute()
            results.append(result)
        logger.info("All commands in the Workflow have been executed.")
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
        logger.info(f"Training model with data: {data}")
        result = f'Training model on data: {data}'
        logger.info(f"Model training completed successfully. Result: {result}")
        return result

    def deploy(self) -> str:
        """
        Simulates deploying the model.
        
        :return: A message indicating the deployment was successful.
        """
        logger.info("Initiating model deployment.")
        result = 'Deploying model...'
        logger.info(f"Model deployment completed successfully. Result: {result}")
        return result


# Usage Example
if __name__ == "__main__":
    name = 'BERT'
    data = 'mock data'

    model = Model()
    
    # Create commands for training and deploying the model
    train_command = Train(model, data)
    deploy_command = Deploy(model)

    # Setup a workflow and add commands to it
    workflow = Workflow()
    workflow.add_command(train_command)
    workflow.add_command(deploy_command)

    # Execute the workflow and print the results
    workflow.execute_commands()