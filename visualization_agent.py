import pandas as pd
import matplotlib.pyplot as plt
import os


class VisualizationAgent:

    def run(self):

        print("[VisualizationAgent] Generating graph...")

        if not os.path.exists("water_history.csv"):
            print("[VisualizationAgent] No history file found.")
            return

        data = pd.read_csv("water_history.csv")

        plt.figure(figsize=(8, 5))
        plt.plot(data["score"], marker="o")

        plt.title("Water Quality Score History")
        plt.xlabel("Analysis Number")
        plt.ylabel("Score")

        plt.grid(True)

        plt.savefig("water_score_graph.png")
        plt.close()

        print("[VisualizationAgent] Graph saved successfully.")
