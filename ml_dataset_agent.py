import pandas as pd

class DatasetAgent:
    def run(self, report):
        
        row = {}
        
        for param, details in report.items():
            row[param] = details["value"]
            row[param + "_status"] = details["status"]
            
        return row