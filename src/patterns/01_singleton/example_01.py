class ModelConfig:
    _instance = None  # Class-level variable to hold the single instance of the class

    def __new__(cls, *args, **kwargs):
        """
        Overrides the __new__ method to control the creation of a new instance. This ensures that only one instance 
        of the class is created, implementing the Singleton pattern.
        """
        if not cls._instance:
            # If no instance exists, create one and assign it to the _instance variable
            cls._instance = super(ModelConfig, cls).__new__(cls, *args, **kwargs)
            cls.model_name = "Gemini 2.0"
            cls.model_path = "/models/gemini"
            cls.api_key = "xyz-abc"
        return cls._instance

if __name__ == '__main__':
    config1 = ModelConfig()
    print(config1)

    config2 = ModelConfig()
    print(config2)

    # Both variables point to the same instance
    assert config1 is config2

    print(config1.model_name)  # Output: LLM_Model_v1
