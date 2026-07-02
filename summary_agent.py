class SummaryAgent:

    def run(self, score):

        if isinstance(score, dict):
            value = score.get("score", 0)
            grade = score.get("grade", "N/A")
        else:
            value = float(score)
            grade = "N/A"

        if value >= 90:
            summary_text = "Excellent"
        elif value >= 70:
            summary_text = "Good"
        else:
            summary_text = "Poor"

        return {
            "summary": summary_text,
            "score": value,
            "grade": grade
        }