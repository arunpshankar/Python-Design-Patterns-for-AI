from functools import wraps 

def cache_decorator(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key based on function arguments
        key = args + tuple(sorted(kwargs.items()))
        print(cache)
        
        if key in cache:
            return cache[key]
        
        # Call the function and store the result in cache
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper


class Model:
    @cache_decorator
    def predict(self, text):
        if 'happy' in text:
            return 1
        elif 'sad' in text:
            return -1
        else:
            return 0

# Usage
model = Model()

# cache miss
response = model.predict("happy face")
print(response) 

# cache miss
response = model.predict("sad face")
print(response)  

# cache miss
response = model.predict("cat face")
print(response)  

# cache hit 
response = model.predict("sad face")
print(response) 

# cache hit 
response = model.predict("cat face")
print(response)  
