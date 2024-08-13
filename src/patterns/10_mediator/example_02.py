import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event, data=None):
        pass

    @abstractmethod
    def send_message(self, sender, receiver, message):
        pass

class AIWorkflowMediator(Mediator):
    def __init__(self, data_agent, inference_agent, evaluation_agent):
        self.data_agent = data_agent
        self.inference_agent = inference_agent
        self.evaluation_agent = evaluation_agent
        
        # Set this mediator for each agent
        self.data_agent.set_mediator(self)
        self.inference_agent.set_mediator(self)
        self.evaluation_agent.set_mediator(self)
        logger.info("AIWorkflowMediator initialized and agents registered.")

    def notify(self, sender, event, data=None):
        logger.info(f"Notification received from {sender.__class__.__name__} with event: {event}")
        
        if event == "data_ready":
            logger.info("Data ready event triggered. Passing data to InferenceAgent.")
            self.inference_agent.process_data(data or sender.get_data())
        
        elif event == "inference_done":
            logger.info("Inference done event triggered. Passing results to EvaluationAgent.")
            self.evaluation_agent.evaluate(data or sender.get_results())
    
    def send_message(self, sender, receiver, message):
        logger.info(f"{sender.__class__.__name__} is sending a message to {receiver.__class__.__name__}: {message}")
        receiver.receive_message(message)

class BaseAgent(ABC):
    def __init__(self, mediator=None):
        self._mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator
        logger.info(f"{self.__class__.__name__} mediator set.")

    @abstractmethod
    def receive_message(self, message):
        pass

class DataAgent(BaseAgent):
    def process(self):
        logger.info("DataAgent processing started.")
        data = self.load_data()
        logger.info("Data loaded successfully.")
        self._mediator.notify(self, "data_ready", data)

    def load_data(self):
        logger.info("Loading data...")
        return "processed_data"

    def get_data(self):
        return self.load_data()

    def receive_message(self, message):
        logger.info(f"DataAgent received message: {message}")

class InferenceAgent(BaseAgent):
    def process_data(self, data):
        logger.info(f"InferenceAgent processing data: {data}")
        results = self.run_inference(data)
        logger.info("Inference completed.")
        self._mediator.notify(self, "inference_done", results)

    def run_inference(self, data):
        logger.info("Running inference...")
        return f"inference_results for {data}"

    def get_results(self):
        return self.run_inference("processed_data")

    def receive_message(self, message):
        logger.info(f"InferenceAgent received message: {message}")
        # Optionally, trigger a specific action based on the message
        if message == "request_data":
            self._mediator.send_message(self, self._mediator.data_agent, "data_requested")

class EvaluationAgent(BaseAgent):
    def evaluate(self, results):
        logger.info(f"EvaluationAgent evaluating results: {results}")
        print(f"Evaluating: {results}")
        # Example of sending a message to another agent
        self._mediator.send_message(self, self._mediator.inference_agent, "request_data")

    def receive_message(self, message):
        logger.info(f"EvaluationAgent received message: {message}")

# Usage
data_agent = DataAgent()
inference_agent = InferenceAgent()
evaluation_agent = EvaluationAgent()

mediator = AIWorkflowMediator(data_agent, inference_agent, evaluation_agent)
data_agent.process()  # Triggers the entire workflow
