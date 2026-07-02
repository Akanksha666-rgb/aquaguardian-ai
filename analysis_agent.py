from config import WATER_LIMITS


class AnalysisAgent:

    def __init__(self):
        pass

    def check_status(self, value, parameter):

        ideal_min, ideal_max = WATER_LIMITS[parameter]["ideal"]
        acceptable_min, acceptable_max = WATER_LIMITS[parameter]["acceptable"]

        if ideal_min <= value <= ideal_max:
            return "Ideal"

        elif acceptable_min <= value <= acceptable_max:
            return "Moderate"

        else:
            return "Poor"

    def run(self, data):

        print("[AnalysisAgent] Analysing water quality...\n")

        report = {}

        for parameter in WATER_LIMITS.keys():

            value = data.get(parameter, 0)

            try:
                value = float(value)
            except:
                value = 0.0

            report[parameter] = {
                "value": value,
                "status": self.check_status(value, parameter)
            }

        print("\n===== ANALYSIS REPORT =====")
        for key, value in report.items():
            print(f"{key} : {value}")
        print("===========================\n")

        return report