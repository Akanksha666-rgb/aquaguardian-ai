class DecisionAgent:

    def run(self, report, score):

        poor = []
        moderate = []

        for param, details in report.items():

            if details["status"] == "Poor":
                poor.append(param)

            elif details["status"] == "Moderate":
                moderate.append(param)

        if score >= 90:
            decision = "Safe to Drink"

        elif score >= 70:
            decision = "Needs Treatment"

        else:
            decision = "Unsafe to Drink"

        return {
            "status": decision,
            "poor_parameters": poor,
            "moderate_parameters": moderate
        }