from src.config.logging import logger
from abc import abstractmethod
from typing import Optional 
from typing import Any
from abc import ABC


class EvaluationHandler(ABC):
    """
    Abstract base class for handling evaluation in a chain of responsibility pattern.
    """

    def __init__(self, successor: Optional['EvaluationHandler'] = None) -> None:
        self.successor = successor
        logger.info(f"{self.__class__.__name__} initialized with successor: {self.successor.__class__.__name__ if self.successor else 'None'}")

    @abstractmethod
    def evaluate(self, model: Any, data: Any) -> Optional[float]:
        if self.successor:
            logger.info(f"Passing control to successor: {self.successor.__class__.__name__}")
            return self.successor.evaluate(model, data)
        logger.info(f"No successor found. Ending evaluation in {self.__class__.__name__}")
        return None


class AccuracyHandler(EvaluationHandler):
    """
    Handler for evaluating the accuracy of the model.
    """

    def evaluate(self, model: Any, data: Any) -> Optional[float]:
        logger.info("Evaluating accuracy...")
        accuracy = self.calculate_accuracy(model, data)
        logger.info(f"Accuracy calculated: {accuracy:.2f}")
        if accuracy < 0.7:
            logger.warning(f"Accuracy {accuracy:.2f} is below threshold (0.7). Stopping evaluation.")
            return None
        logger.info(f"Accuracy {accuracy:.2f} is above threshold. Continuing evaluation.")
        return super().evaluate(model, data)

    def calculate_accuracy(self, model: Any, data: Any) -> float:
        logger.info("Calculating accuracy for model and data...")
        # Simulated accuracy calculation
        return 0.85  # try changing this value to 0.65


class F1ScoreHandler(EvaluationHandler):
    """
    Handler for evaluating the F1 score of the model.
    """

    def evaluate(self, model: Any, data: Any) -> Optional[float]:
        logger.info("Evaluating F1 score...")
        f1_score = self.calculate_f1_score(model, data)
        logger.info(f"F1 Score calculated: {f1_score:.2f}")
        return super().evaluate(model, data)

    def calculate_f1_score(self, model: Any, data: Any) -> float:
        logger.info("Calculating F1 score for model and data...")
        # Simulated F1 score calculation
        return 0.75


def run_evaluation_pipeline() -> None:
    """
    Runs the evaluation pipeline with accuracy and F1 score handlers.
    """
    logger.info("Starting evaluation pipeline...")
    f1_handler = F1ScoreHandler()
    accuracy_handler = AccuracyHandler(successor=f1_handler)

    model = "example_model"
    data = "example_data"

    logger.info("Running evaluation handlers...")
    accuracy_handler.evaluate(model, data)
    logger.info("Evaluation pipeline finished.")

if __name__ == "__main__":
    run_evaluation_pipeline()


# Note: To test the alternative scenario - Change the returned accuracy score to 0.6 by the AccuracyHandler class (which will be <0.7 as per the threshold conditional logic) 
# and re-run the evaluation pipeline. This should result in a warning message, and the pipeline will break without running the F1ScoreHandler.

