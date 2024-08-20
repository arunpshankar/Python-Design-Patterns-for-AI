from src.config.logging import logger
from abc import abstractmethod
from typing import Optional
from abc import ABC


class Mediator(ABC):
    """
    The Mediator abstract base class defines an interface for communication between components (agents). 
    Components use this interface to notify the mediator about various events and to send messages between components, functioning as a pull mechanism for communication.
    """

    @abstractmethod
    def notify(self, sender: 'BaseAgent', event: str, data: Optional[str] = None) -> None:
        """
        Notifies the mediator of an event from a component.

        :param sender: The component that triggered the event.
        :param event: A string representing the event type.
        :param data: Optional data related to the event.
        :raises NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError("The 'notify' method must be implemented by subclasses of Mediator.")

    @abstractmethod
    def send_message(self, sender: 'BaseAgent', receiver: 'BaseAgent', message: str) -> None:
        """
        Sends a message from one component to another.

        :param sender: The component sending the message.
        :param receiver: The component receiving the message.
        :param message: The message being sent.
        :raises NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError("The 'send_message' method must be implemented by subclasses of Mediator.")


class Workflow(Mediator):
    """
    The Workflow class acts as a concrete mediator, coordinating
    interactions between the DataAgent, InferenceAgent, and EvaluationAgent.
    """
    def __init__(self, data_agent: 'DataAgent', inference_agent: 'InferenceAgent', evaluation_agent: 'EvaluationAgent') -> None:
        self.data_agent = data_agent
        self.inference_agent = inference_agent
        self.evaluation_agent = evaluation_agent
        
        # Set this mediator for each agent
        self.data_agent.set_mediator(self)
        self.inference_agent.set_mediator(self)
        self.evaluation_agent.set_mediator(self)
        logger.info("Workflow initialized and agents registered.")

    def notify(self, sender: 'BaseAgent', event: str, data: Optional[str] = None) -> None:
        logger.info(f"Notification received from {sender.__class__.__name__} with event: {event}")
        
        if event == "data_ready":
            logger.info("Data ready event triggered. Passing data to InferenceAgent.")
            self.inference_agent.process_data(data or sender.get_data())
        
        elif event == "inference_done":
            logger.info("Inference done event triggered. Passing results to EvaluationAgent.")
            self.evaluation_agent.evaluate(data or sender.get_results())
    
    def send_message(self, sender: 'BaseAgent', receiver: 'BaseAgent', message: str) -> None:
        logger.info(f"{sender.__class__.__name__} is sending a message to {receiver.__class__.__name__}: {message}")
        receiver.receive_message(message)


class BaseAgent(ABC):
    """
    The BaseAgent class serves as an abstract base for all agents interacting
    with the mediator. It stores a reference to the mediator and provides a
    method to set it.
    """
    def __init__(self, mediator: Optional[Mediator] = None) -> None:
        self._mediator = mediator

    def set_mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator
        logger.info(f"{self.__class__.__name__} mediator set.")

    @abstractmethod
    def receive_message(self, message: str) -> None:
        """
        Handles receiving a message from another agent.

        :param message: The message content.
        :raises NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError("The 'receive_message' method must be implemented by subclasses of BaseAgent.")


class DataAgent(BaseAgent):
    def process(self) -> None:
        logger.info("DataAgent processing started.")
        data = self.load_data()
        logger.info("Data loaded successfully.")
        self._mediator.notify(self, "data_ready", data)

    def load_data(self) -> str:
        logger.info("Loading data...")
        return "processed_data"

    def get_data(self) -> str:
        return self.load_data()

    def receive_message(self, message: str) -> None:
        logger.info(f"DataAgent received message: {message}")


class InferenceAgent(BaseAgent):
    def process_data(self, data: str) -> None:
        logger.info(f"InferenceAgent processing data: {data}")
        results = self.run_inference(data)
        logger.info("Inference completed.")
        self._mediator.notify(self, "inference_done", results)

    def run_inference(self, data: str) -> str:
        logger.info("Running inference...")
        return f"inference_results for {data}"

    def get_results(self) -> str:
        return self.run_inference("processed_data")

    def receive_message(self, message: str) -> None:
        logger.info(f"InferenceAgent received message: {message}")
        # Optionally, trigger a specific action based on the message
        if message == "request_data":
            self._mediator.send_message(self, self._mediator.data_agent, "data_requested")


class EvaluationAgent(BaseAgent):
    """
    The EvaluationAgent evaluates the results produced by InferenceAgent.
    """
    def evaluate(self, results: str) -> None:
        logger.info(f"EvaluationAgent evaluating results: {results}")
        print(f"Evaluating: {results}")
        # Example of sending a message to another agent
        self._mediator.send_message(self, self._mediator.inference_agent, "request_data")

    def receive_message(self, message: str) -> None:
        logger.info(f"EvaluationAgent received message: {message}")


# Usage
data_agent = DataAgent()
inference_agent = InferenceAgent()
evaluation_agent = EvaluationAgent()

mediator = Workflow(data_agent, inference_agent, evaluation_agent)
data_agent.process()  # Triggers the entire workflow
