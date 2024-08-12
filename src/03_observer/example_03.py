class ModelPerformanceObserver:
    def __init__(self, model_name):
        self.model_name = model_name

    def update(self, accuracy, loss):
        if accuracy < 0.7:
            print(f"Alert: {self.model_name} accuracy dropped below threshold!")
        print(f"Pushed Data for {self.model_name} - Accuracy: {accuracy}, Loss: {loss}")

class ModelMonitor:
    def __init__(self):
        self._observers = {}

    def attach(self, model_name, observer):
        if model_name not in self._observers:
            self._observers[model_name] = observer

    def detach(self, model_name):
        if model_name in self._observers:
            del self._observers[model_name]

    def notify(self, model_name, accuracy, loss):
        if model_name in self._observers:
            self._observers[model_name].update(accuracy, loss)

# Usage
monitor = ModelMonitor()

# Creating observers for Model A and Model B
observer_a = ModelPerformanceObserver("Model A")
observer_b = ModelPerformanceObserver("Model B")

# Attaching observers to the monitor
monitor.attach("Model A", observer_a)
monitor.attach("Model B", observer_b)

# Simulate model training for Model A
accuracy_a = 0.65
loss_a = 0.4
monitor.notify("Model A", accuracy_a, loss_a)  # Output: Alert: Model A accuracy dropped below threshold!

# Simulate model training for Model B
accuracy_b = 0.75
loss_b = 0.3
monitor.notify("Model B", accuracy_b, loss_b)  # Output: Pushed Data for Model B - Accuracy: 0.75, Loss: 0.3
