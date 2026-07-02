import matplotlib.pyplot as plt
import numpy as np


class RadarVisualizationAgent:

    def run(self, report):

        print("[RadarVisualizationAgent] Generating radar chart...")

        parameters = list(report.keys())

        values = [report[p]["value"] for p in parameters]

        # Normalize values (important for radar)
        max_values = {
            "ph": 14,
            "tds": 1000,
            "hardness": 500,
            "fluoride": 3,
            "iron": 2,
            "nitrate": 100,
            "chlorine": 5,
            "conductivity": 2000,
            "turbidity": 100,
            "calcium": 200,
            "magnesium": 100,
            "potassium": 50,
            "sodium": 100
        }

        normalized = [
            values[i] / max_values.get(parameters[i], 1)
            for i in range(len(parameters))
        ]

        angles = np.linspace(0, 2 * np.pi, len(parameters), endpoint=False).tolist()
        normalized += normalized[:1]
        angles += angles[:1]

        plt.figure(figsize=(6, 6))
        ax = plt.subplot(111, polar=True)

        ax.plot(angles, normalized, linewidth=2)
        ax.fill(angles, normalized, alpha=0.3)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(parameters, fontsize=8)

        plt.title("Water Quality Radar Analysis")

        plt.savefig("radar_chart.png")
        plt.close()

        print("[RadarVisualizationAgent] Saved radar_chart.png")