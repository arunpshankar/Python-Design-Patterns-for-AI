import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Mediator:
    def notify(self, sender, event):
        pass

class Workflow(Mediator):
    def __init__(self, data_agent, inference_agent, evaluation_agent):
        self.data_agent = data_agent
        self.inference_agent = inference_agent
        self.evaluation_agent = evaluation_agent
        
        # Set this mediator for each agent
        self.data_agent.set_mediator(self)
        self.inference_agent.set_mediator(self)
        self.evaluation_agent.set_mediator(self)
        logger.info("Workflow initialized and agents registered.")

    def notify(self, sender, event):
        logger.info(f"Notification received from {sender.__class__.__name__} with event: {event}")
        
        if event == "data_ready":
            logger.info("Data ready event triggered. Passing data to InferenceAgent.")
            self.inference_agent.process_data(sender.get_data())
        
        elif event == "inference_done":
            logger.info("Inference done event triggered. Passing results to EvaluationAgent.")
            self.evaluation_agent.evaluate(sender.get_results())

class BaseAgent:
    def __init__(self, mediator=None):
        self._mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator
        logger.info(f"{self.__class__.__name__} mediator set.")

class DataAgent(BaseAgent):
    def process(self):
        logger.info("DataAgent processing started.")
        data = self.load_data()
        logger.info("Data loaded successfully.")
        self._mediator.notify(self, "data_ready")

    def load_data(self):
        logger.info("Loading data...")
        return "processed_data"

    def get_data(self):
        return self.load_data()

class InferenceAgent(BaseAgent):
    def process_data(self, data):
        logger.info(f"InferenceAgent processing data: {data}")
        results = self.run_inference(data)
        logger.info("Inference completed.")
        self._mediator.notify(self, "inference_done")

    def run_inference(self, data):
        logger.info("Running inference...")
        return f"inference_results for {data}"

    def get_results(self):
        return self.run_inference("processed_data")

class EvaluationAgent(BaseAgent):
    def evaluate(self, results):
        logger.info(f"EvaluationAgent evaluating results: {results}")
        print(f"Evaluating: {results}")

# Usage
data_agent = DataAgent()
inference_agent = InferenceAgent()
evaluation_agent = EvaluationAgent()

mediator = Workflow(data_agent, inference_agent, evaluation_agent)
data_agent.process()  # Triggers the entire workflow
