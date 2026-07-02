from agents.data_ingestion_agent import DataIngestionAgent
from agents.analysis_agent import AnalysisAgent
from agents.score_agent import ScoreAgent
from agents.summary_agent import SummaryAgent
from agents.decision_agent import DecisionAgent
from agents.risk_agent import RiskAgent
from agents.recommendation_agent import RecommendationAgent
from agents.explanation_agent import ExplanationAgent
from agents.history_agent import HistoryAgent
from agents.report_agent import ReportAgent
from agents.visualization_agent import VisualizationAgent
from agents.parameter_visualization_agent import ParameterVisualizationAgent
from agents.final_summary_agent import FinalSummaryAgent

# NEW UPGRADES
from ml_dataset_agent import DatasetAgent
from agents.radar_visualization_agent import RadarVisualizationAgent

import pandas as pd
import os


class AquaGuardianWorkflow:

    def __init__(self):

        self.ingestion_agent = DataIngestionAgent()
        self.analysis_agent = AnalysisAgent()
        self.score_agent = ScoreAgent()
        self.summary_agent = SummaryAgent()
        self.decision_agent = DecisionAgent()
        self.risk_agent = RiskAgent()
        self.recommendation_agent = RecommendationAgent()
        self.explanation_agent = ExplanationAgent()
        self.history_agent = HistoryAgent()
        self.report_agent = ReportAgent()
        self.visualization_agent = VisualizationAgent()
        self.parameter_visualization_agent = ParameterVisualizationAgent()
        self.final_summary_agent = FinalSummaryAgent()

        # NEW
        self.dataset_agent = DatasetAgent()
        self.radar_agent = RadarVisualizationAgent()

    def run(self, input_data):

        print("\n🚰 Starting AquaGuardian Workflow\n")

        # 1. Clean input
        cleaned_data = self.ingestion_agent.run(input_data)

        # 2. Analysis
        report = self.analysis_agent.run(cleaned_data)

        # 3. Parameter visualization
        self.parameter_visualization_agent.run(report)

        # 4. Score
        score_output = self.score_agent.run(report)

        score_value = score_output.get("score", 0)
        grade = score_output.get("grade", "N/A")

        try:
            score_value = float(score_value)
        except:
            score_value = 0.0

        score = {
            "score": score_value,
            "grade": grade
        }

        # 5. Summary
        summary = self.summary_agent.run(score_value)

        # 6. Decision
        decision = self.decision_agent.run(report, score_value)

        # 7. Risk
        risk = self.risk_agent.run(decision)

        # 8. Recommendation
        recommendation = self.recommendation_agent.run(decision)

        # 9. Final summary
        final_summary = self.final_summary_agent.run(score, decision, risk)

        # 10. Explanation
        final_result = self.explanation_agent.run({
            "summary": final_summary,
            "score": score,
            "decision": decision,
            "risk": risk,
            "recommendation": recommendation
        })

        # 11. History logging
        final_result = self.history_agent.run(final_result)

        # ---------------- NEW FEATURES ---------------- #

        # 12. Save dataset (ML training data)
        row = self.dataset_agent.run(report)
        df = pd.DataFrame([row])

        if os.path.exists("water_dataset.csv"):
            df.to_csv("water_dataset.csv", mode="a", header=False, index=False)
        else:
            df.to_csv("water_dataset.csv", index=False)

        # 13. Radar chart (WHO-style analysis)
        self.radar_agent.run(report)

        # 14. Report generation
        final_result = self.report_agent.run(final_result)

        # 15. Final visualization
        self.visualization_agent.run()

        print("\n✅ Workflow Completed Successfully\n")

        return final_result