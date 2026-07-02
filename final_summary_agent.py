class FinalSummaryAgent:

    def run(self, score, decision, risk):

        print("[FinalSummaryAgent] Generating final human-friendly summary...")

        score_value = score.get("score", 0)
        grade = score.get("grade", "N/A")

        if score_value >= 90:
            status = "Excellent 💧 (Very Safe)"
        elif score_value >= 75:
            status = "Good 👍 (Safe)"
        elif score_value >= 50:
            status = "Average ⚠️ (Use Caution)"
        else:
            status = "Poor ❌ (Not Safe)"

        if decision.get("status") == "Unsafe to Drink":
            status += " - Not Recommended for Drinking"

        summary = {
            "health_status": status,
            "score": score_value,
            "grade": grade,
            "risk_level": risk.get("risk_level", "Unknown")
        }

        print("[FinalSummaryAgent] Summary:", summary)

        return summary