class DataIngestionAgent:
    def __init__(self):
        pass
    
    def run(self, data):
        
        print("[DataIngestionAgent] Received data:", data)
        
        if not isinstance(data, dict):
            raise ValueError("Input data must be a dictionary.")
        
        cleaned_data = {}
        
        for key, value in data.items():
            if value is None:
                cleaned_data[key] = 0
            else:
                cleaned_data[key] = value
                
        print("[DataIngestionAgent] Cleaned data:", cleaned_data)
        
        return cleaned_data