# Pull Variant
class ModelPerformanceObserver:
    def __init__(self, subject):
        self._subject = subject

    def update(self):
        accuracy = self._subject.get_accuracy()
        loss = self._subject.get_loss()
        if accuracy < 0.7:
            print("Alert: Model accuracy dropped below threshold!")
        print(f"Pulled Data - Accuracy: {accuracy}, Loss: {loss}")

class ModelMonitor:
    def __init__(self):
        self._observers = []
        self._accuracy = 0
        self._loss = 0

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def set_state(self, accuracy, loss):
        self._accuracy = accuracy
        self._loss = loss
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update()

    def get_accuracy(self):
        return self._accuracy

    def get_loss(self):
        return self._loss

# Usage
monitor = ModelMonitor()
observer = ModelPerformanceObserver(monitor)

monitor.attach(observer)

# Simulate model training
monitor.set_state(0.65, 0.4)  # Output: Alert: Model accuracy dropped below threshold!
                                   #         Pulled Data - Accuracy: 0.65, Loss: 0.4

# push feels more elegant

"""

Both patterns are useful in different scenarios. 
The push variant is simpler when the subject knows exactly what data the observers need. 
The pull variant is more flexible, allowing observers to decide what data they want to pull from the subject.
"""