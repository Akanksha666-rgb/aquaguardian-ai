class RiskAgent:

    def run(self, decision):

        if decision["status"] == "Safe to Drink":
            risk_level = "Low"

        elif decision["status"] == "Needs Treatment":
            risk_level = "Medium"

        else:
            risk_level = "High"

        return {
            "risk_level": risk_level
        }