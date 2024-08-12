def validate_data(func):
    """
    Decorator that validates the input data before processing.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: The wrapped function with additional validation logic.
    """
    def wrapper(data):
        # Check if the data is a non-empty string
        if not isinstance(data, str) or not data.strip():
            raise ValueError("Invalid data: Input must be a non-empty string.")
        
        # If validation passes, call the original function
        return func(data)
    
    return wrapper

def augment_data(func):
    """
    Decorator that augments the output of a data processing function.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: The wrapped function with additional augmentation logic.
    """
    def wrapper(data):
        # Call the original function to process the data
        processed_data = func(data)
        
        # Augment the processed data with additional information
        augmented_data = f"{processed_data} + augmented"
        
        # Return the augmented data
        return augmented_data
    
    return wrapper

@validate_data
@augment_data
def preprocess_data(data):
    """
    Function to preprocess the given data by cleaning it.

    Parameters:
    data (str): The raw input data to be cleaned.

    Returns:
    str: The cleaned data.
    """
    cleaned_data = f"cleaned {data}"
    return cleaned_data

# Example usage
if __name__ == "__main__":
    try:
        raw_data = " raw_data "
        
        # Process the raw data using the decorated preprocess_data function
        processed_data = preprocess_data(raw_data)
        
        # Output the processed and augmented data
        print(processed_data)  # Output: cleaned raw_data + augmented
        
        # Uncommenting the following line will raise a ValueError due to invalid data
        # invalid_data = ""
        # preprocess_data(invalid_data)

    except ValueError as e:
        print(f"Error: {e}")
