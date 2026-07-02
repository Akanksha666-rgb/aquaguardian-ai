import pandas as pd
import os


from datetime import datetime
import pandas as pd
import os


class HistoryAgent:

    def run(self, result):

        score_value = result.get("score", 0)

        if isinstance(score_value, dict):
            score_value = score_value.get("score", 0)

        grade = result.get("grade", "N/A")

        decision = result.get("decision", {}).get("status", "")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # safe mineral extraction (no breaking if missing)
        minerals = result.get("input_data", {})

        row = {
            "timestamp": timestamp,
            "score": float(score_value),
            "grade": grade,
            "decision": decision,

            "ph": minerals.get("ph", 0),
            "tds": minerals.get("tds", 0),
            "hardness": minerals.get("hardness", 0),
            "fluoride": minerals.get("fluoride", 0),
            "iron": minerals.get("iron", 0),
            "nitrate": minerals.get("nitrate", 0),
            "chlorine": minerals.get("chlorine", 0),
            "conductivity": minerals.get("conductivity", 0),
            "turbidity": minerals.get("turbidity", 0),
            "calcium": minerals.get("calcium", 0),
            "magnesium": minerals.get("magnesium", 0),
            "potassium": minerals.get("potassium", 0),
            "sodium": minerals.get("sodium", 0),
        }

        df = pd.DataFrame([row])

        if os.path.exists("water_history.csv"):
            df.to_csv("water_history.csv", mode="a", header=False, index=False)
        else:
            df.to_csv("water_history.csv", index=False)

        return result