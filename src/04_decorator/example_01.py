def augment_data(func):
    def wrapper(data):
        data = func(data)
        augmented_data = f"{data} + augmented"
        return augmented_data
    return wrapper

@augment_data
def preprocess_data(data):
    cleaned_data = f"cleaned {data}"
    return cleaned_data

# Usage
data = "raw_data"
processed_data = preprocess_data(data)
print(processed_data)  # Output: cleaned raw_data + augmented
