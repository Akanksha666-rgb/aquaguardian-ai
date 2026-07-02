import matplotlib.pyplot as plt


class ParameterVisualizationAgent:

    def run(self, report):

        print("[ParameterVisualizationAgent] Generating parameter graph...")

        parameters = list(report.keys())

        actual = [report[p]["value"] for p in parameters]

        plt.figure(figsize=(10, 5))

        plt.bar(parameters, actual, label="Actual Value")

        plt.title("Water Quality Parameters")
        plt.ylabel("Value")
        plt.xticks(rotation=45)

        plt.legend()
        plt.tight_layout()

        plt.savefig("water_parameter_comparison.png")
        plt.close()

        print("[ParameterVisualizationAgent] Graph saved successfully.")