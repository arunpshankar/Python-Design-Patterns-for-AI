class ModelPerformanceObserver:
    def update(self, accuracy, loss):
        if accuracy < 0.7:
            print("Alert: Model accuracy dropped below threshold!")
        print(f"Pushed Data - Accuracy: {accuracy}, Loss: {loss}")

class ModelMonitor:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, accuracy, loss):
        for observer in self._observers:
            observer.update(accuracy, loss)

# Usage
monitor = ModelMonitor()
observer = ModelPerformanceObserver()

monitor.attach(observer)

# Simulate model training
accuracy = 0.65
loss = 0.4
monitor.notify(accuracy, loss)  # Output: Alert: Model accuracy dropped below threshold!
