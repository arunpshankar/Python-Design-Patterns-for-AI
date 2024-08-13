from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        """Executes the command."""
        pass

# Concrete Command to Train a Model
class TrainModelCommand(Command):
    def __init__(self, model, data):
        """
        Initializes the TrainModelCommand with a model and training data.
        
        :param model: The model instance to be trained.
        :param data: The training data.
        """
        self.model = model
        self.data = data

    def execute(self):
        """
        Executes the training process on the model.
        
        :return: A message indicating the model has been trained.
        """
        return self.model.train(self.data)

# Concrete Command to Deploy a Model
class DeployModelCommand(Command):
    def __init__(self, model):
        """
        Initializes the DeployModelCommand with a model.
        
        :param model: The model instance to be deployed.
        """
        self.model = model

    def execute(self):
        """
        Executes the deployment process for the model.
        
        :return: A message indicating the model has been deployed.
        """
        return deploy_model(self.model)

# Invoker Class
class WorkflowInvoker:
    def __init__(self):
        """
        Initializes the WorkflowInvoker with an empty list of commands.
        """
        self._commands = []

    def add_command(self, command):
        """
        Adds a command to the list of commands to be executed.
        
        :param command: An instance of a Command.
        """
        self._commands.append(command)

    def execute_commands(self):
        """
        Executes all commands in the order they were added.
        
        :return: A list of results from each command's execution.
        """
        results = []
        for command in self._commands:
            results.append(command.execute())
        return results

# Example Model Class
class ExampleModel:
    def train(self, data):
        """
        Simulates training the model on the provided data.
        
        :param data: The data to train the model on.
        :return: A message indicating the training was successful.
        """
        return f"Model trained on {data}"

def deploy_model(model):
    """
    Simulates deploying the provided model.
    
    :param model: The model instance to deploy.
    :return: A message indicating the deployment was successful.
    """
    return f"Deployed {model}"

# Usage Example
if __name__ == "__main__":
    model = ExampleModel()
    train_command = TrainModelCommand(model, "training data")
    deploy_command = DeployModelCommand(model)

    invoker = WorkflowInvoker()
    invoker.add_command(train_command)
    invoker.add_command(deploy_command)

    results = invoker.execute_commands()
    for result in results:
        print(result)  # Output: ['Model trained on training data', 'Deployed <__main__.ExampleModel object at ...>']
