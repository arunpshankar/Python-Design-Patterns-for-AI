from src.config.logging import logger 
from typing import Optional
from typing import Dict 


class ModelPerformanceObserver:
    """
    Observer class that monitors and logs model performance metrics such as accuracy and loss.
    Alerts when performance metrics fall below predefined thresholds.
    """
    
    def __init__(self, model_name: str) -> None:
        """
        Initializes the observer with the model name.

        Args:
            model_name (str): The name of the model being observed.
        """
        self.model_name = model_name

    def update(self, accuracy: float, loss: float) -> None:
        """
        Updates the observer with the latest accuracy and loss metrics.

        Args:
            accuracy (float): The accuracy of the model.
            loss (float): The loss value of the model.
        """
        if accuracy < 0.7:
            logger.warning(f"Alert: {self.model_name} accuracy dropped below threshold!")
        logger.info(f"Pushed Data for {self.model_name} - Accuracy: {accuracy}, Loss: {loss}")


class ModelMonitor:
    """
    Subject class that manages observers and notifies them of model performance updates.
    Implements the observer design pattern to monitor model performance.
    """
    
    def __init__(self) -> None:
        """
        Initializes the ModelMonitor with an empty dictionary of observers.
        """
        self._observers: Dict[str, ModelPerformanceObserver] = {}

    def attach(self, model_name: str, observer: ModelPerformanceObserver) -> None:
        """
        Attaches an observer to a specific model.

        Args:
            model_name (str): The name of the model to be observed.
            observer (ModelPerformanceObserver): The observer instance to attach.
        """
        if model_name not in self._observers:
            self._observers[model_name] = observer
            logger.info(f"Attached observer to {model_name}.")

    def detach(self, model_name: str) -> None:
        """
        Detaches an observer from a specific model.

        Args:
            model_name (str): The name of the model to stop observing.
        """
        if model_name in self._observers:
            del self._observers[model_name]
            logger.info(f"Detached observer from {model_name}.")

    def notify(self, model_name: str, accuracy: float, loss: float) -> None:
        """
        Notifies the observer of the specified model with the latest performance metrics.

        Args:
            model_name (str): The name of the model being observed.
            accuracy (float): The latest accuracy value.
            loss (float): The latest loss value.
        """
        observer: Optional[ModelPerformanceObserver] = self._observers.get(model_name)
        if observer:
            logger.info(f"Notifying observer for {model_name}.")
            observer.update(accuracy, loss)
        else:
            logger.warning(f"No observer found for {model_name}.")


if __name__ == "__main__":
    monitor = ModelMonitor()

    # Creating observers for Model A and Model B
    observer_a = ModelPerformanceObserver("Model A")
    observer_b = ModelPerformanceObserver("Model B")

    # Attaching observers to the monitor
    monitor.attach("Model A", observer_a)
    monitor.attach("Model B", observer_b)

    # Simulate model training for Model A
    accuracy_a = 0.65
    loss_a = 0.43
    monitor.notify("Model A", accuracy_a, loss_a)  # Output: Alert: Model A accuracy dropped below threshold!

    # Simulate model training for Model B
    accuracy_b = 0.75
    loss_b = 0.39
    monitor.notify("Model B", accuracy_b, loss_b)  # Output: Pushed Data for Model B - Accuracy: 0.75, Loss: 0.3

    # Deattach observer for Model A 
    monitor.detach("Model A")