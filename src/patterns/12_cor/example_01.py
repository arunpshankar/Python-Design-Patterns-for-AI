import logging
from abc import ABC, abstractmethod

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EvaluationHandler(ABC):
    def __init__(self, successor=None):
        self.successor = successor
        logging.info(f"{self.__class__.__name__} initialized with successor: {self.successor.__class__.__name__ if self.successor else 'None'}")

    @abstractmethod
    def evaluate(self, model, data):
        logging.info(f"Starting evaluation with {self.__class__.__name__}")
        if self.successor:
            logging.info(f"Passing control to successor: {self.successor.__class__.__name__}")
            return self.successor.evaluate(model, data)
        logging.info(f"No successor found. Ending evaluation in {self.__class__.__name__}")
        return None

class AccuracyHandler(EvaluationHandler):
    def evaluate(self, model, data):
        logging.info("Evaluating accuracy...")
        accuracy = self.calculate_accuracy(model, data)
        logging.info(f"Accuracy calculated: {accuracy:.2f}")
        if accuracy < 0.7:
            logging.warning(f"Accuracy {accuracy:.2f} is below threshold (0.7). Stopping evaluation.")
            return None
        logging.info(f"Accuracy {accuracy:.2f} is above threshold. Continuing evaluation.")
        return super().evaluate(model, data)

    def calculate_accuracy(self, model, data):
        logging.debug("Calculating accuracy for model and data...")
        # Simulated accuracy calculation
        return 0.85
    

class F1ScoreHandler(EvaluationHandler):
    def evaluate(self, model, data):
        logging.info("Evaluating F1 score...")
        f1_score = self.calculate_f1_score(model, data)
        logging.info(f"F1 Score calculated: {f1_score:.2f}")
        return super().evaluate(model, data)

    def calculate_f1_score(self, model, data):
        logging.debug("Calculating F1 score for model and data...")
        # Simulated F1 score calculation
        return 0.75

# Usage example
def run_evaluation_pipeline():
    logging.info("Starting evaluation pipeline...")
    f1_handler = F1ScoreHandler()
    accuracy_handler = AccuracyHandler(successor=f1_handler)

    model = "example_model"
    data = "example_data"

    logging.info("Running evaluation handlers...")
    accuracy_handler.evaluate(model, data)
    logging.info("Evaluation pipeline finished.")

if __name__ == "__main__":
    run_evaluation_pipeline()



# change returned accuracy score to .85 and re-run to see the f1 successor in action 
# basically 
