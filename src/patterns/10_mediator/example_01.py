from src.config.logging import logger
from abc import abstractmethod
from typing import Optional
from abc import ABC


class Mediator(ABC):
    """
    The Mediator abstract base class defines an interface for communication between components (agents). 
    Components use this interface to notify the mediator about various events, which serves as a push mechanism for communication. 
    The mediator can then coordinate actions between the components.
    """

    @abstractmethod
    def notify(self, sender: 'BaseAgent', event: str) -> None:
        """
        Notifies the mediator of an event from a component.

        :param sender: The component that triggered the event.
        :param event: A string representing the event type.
        :raises NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError("The 'notify' method must be implemented by subclasses of Mediator.")


class Workflow(Mediator):
    """
    The Workflow class acts as a concrete mediator, coordinating the interactions
    between the DataAgent, InferenceAgent, and EvaluationAgent.
    """
    def __init__(self, data_agent: 'DataAgent', inference_agent: 'InferenceAgent', evaluation_agent: 'EvaluationAgent') -> None:
        self.data_agent = data_agent
        self.inference_agent = inference_agent
        self.evaluation_agent = evaluation_agent
        
        # Register each agent with the mediator
        self.data_agent.set_mediator(self)
        self.inference_agent.set_mediator(self)
        self.evaluation_agent.set_mediator(self)
        logger.info("Workflow initialized and agents registered.")

    def notify(self, sender: 'BaseAgent', event: str) -> None:
        logger.info(f"Notification received from {sender.__class__.__name__} with event: {event}")
        
        if event == "data_ready":
            logger.info("Data ready event triggered. Passing data to InferenceAgent.")
            self.inference_agent.process_data(sender.get_data())
        
        elif event == "inference_done":
            logger.info("Inference done event triggered. Passing results to EvaluationAgent.")
            self.evaluation_agent.evaluate(sender.get_results())


class BaseAgent:
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


class DataAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self._data = None

    def process(self) -> None:
        logger.info("DataAgent processing started.")
        self._data = self.load_data()
        logger.info(f"Data loaded successfully: {self._data}")
        self._mediator.notify(self, "data_ready")

    def load_data(self) -> str:
        logger.info("Loading data...")
        return "processed_data"

    def get_data(self) -> str:
        return self._data


class InferenceAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self._results = None

    def process_data(self, data: str) -> None:
        logger.info(f"InferenceAgent processing data: {data}")
        self._results = self.run_inference(data)
        logger.info(f"Inference completed with results: {self._results}")
        self._mediator.notify(self, "inference_done")

    def run_inference(self, data: str) -> str:
        logger.info("Running inference...")
        return f"inference_results for {data}"

    def get_results(self) -> str:
        return self._results


class EvaluationAgent(BaseAgent):
    """
    The EvaluationAgent evaluates the results produced by InferenceAgent.
    """
    def evaluate(self, results: str) -> None:
        logger.info(f"EvaluationAgent evaluating results: {results}")
        logger.info(f"Evaluation complete: {results}")


# Usage
data_agent = DataAgent()
inference_agent = InferenceAgent()
evaluation_agent = EvaluationAgent()

mediator = Workflow(data_agent, inference_agent, evaluation_agent)
data_agent.process()  # Triggers the entire workflow
