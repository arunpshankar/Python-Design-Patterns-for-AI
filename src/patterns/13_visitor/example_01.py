import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Model(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ClassificationModel(Model):
    def accept(self, visitor):
        logging.info(f'{self.__class__.__name__}: Accepting visitor {visitor.__class__.__name__}')
        visitor.visit_classification_model(self)

class Visitor(ABC):
    @abstractmethod
    def visit_classification_model(self, model):
        pass

class SHAPVisitor(Visitor):
    def visit_classification_model(self, model):
        logging.info(f'{self.__class__.__name__}: Visiting {model.__class__.__name__}')
        logging.info('Applying SHAP to explain model predictions')

class LIMEVisitor(Visitor):
    def visit_classification_model(self, model):
        logging.info(f'{self.__class__.__name__}: Visiting {model.__class__.__name__}')
        logging.info('Applying LIME to explain model predictions')

# Usage
if __name__ == "__main__":
    model = ClassificationModel()

    shap_visitor = SHAPVisitor()
    lime_visitor = LIMEVisitor()

    logging.info('Starting SHAP visitor process')
    model.accept(shap_visitor)  # Output: Applying SHAP to explain model predictions

    logging.info('Starting LIME visitor process')
    model.accept(lime_visitor)  # Output: Applying LIME to explain model predictions
