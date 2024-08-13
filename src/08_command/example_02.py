from abc import ABC, abstractmethod

# Abstract Command class defines the interface for all concrete commands.
class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

# Concrete Command for training a model.
class Train(Command):
    def __init__(self, model, data):
        """
        Initialize the command with a model and data.

        :param model: The model to be trained.
        :param data: The data on which the model will be trained.
        """
        self.model = model
        self.data = data

    def execute(self):
        """Execute the training command."""
        return self.model.train(self.data)

# Concrete Command for deploying a model.
class Deploy(Command):
    def __init__(self, model):
        """
        Initialize the command with a model.

        :param model: The model to be deployed.
        """
        self.model = model

    def execute(self):
        """Execute the deployment command."""
        return self.model.deploy()

# The Workflow class holds and executes a sequence of commands.
class Workflow:
    def __init__(self):
        """Initialize an empty list of commands."""
        self._commands = []

    def add(self, command):
        """
        Add a command to the workflow.

        :param command: The command to be added.
        """
        self._commands.append(command)

    def execute(self):
        """
        Execute all commands in the workflow in sequence.

        :return: A list of results from each command's execution.
        """
        results = []
        for command in self._commands:
            results.append(command.execute())
        return results

# Example model class that supports training and deploying.
class Model:
    def train(self, data):
        """
        Train the model on the provided data.

        :param data: The data to train on.
        :return: A string indicating training status.
        """
        return f'Training model on data: {data}'

    def deploy(self):
        """
        Deploy the model.

        :return: A string indicating deployment status.
        """
        return 'Deploying model...'

# Entry point of the script to demonstrate the command pattern.
if __name__ == '__main__':
    # Setup mock data and a model instance
    name = 'BERT'
    data = 'mock data'

    model = Model()
    
    # Create commands for training and deploying the model
    train = Train(model, data)
    deploy = Deploy(model)

    # Setup a workflow and add commands to it
    workflow = Workflow()
    workflow.add(train)
    workflow.add(deploy)

    # Execute the workflow and print the results
    results = workflow.execute()
    for result in results:
        print(result)
