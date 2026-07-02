class ScoreAgent:

    def run(self, report):

        print("[ScoreAgent] Calculating score...")

        total_score = 0
        count = 0

        for param, details in report.items():

            status = details.get("status", "Poor")

            if status == "Ideal":
                score = 100

            elif status == "Moderate":
                score = 70

            else:
                score = 0

            total_score += score
            count += 1

        if count == 0:
            return {
                "score": 0.0,
                "grade": "N/A"
            }

        final_score = total_score / count

        # Grade
        if final_score >= 90:
            grade = "A"

        elif final_score >= 70:
            grade = "B"

        else:
            grade = "D"

        print("[ScoreAgent] Final Score:", final_score)
        print("[ScoreAgent] Grade:", grade)

        return {
            "score": round(final_score, 2),
            "grade": grade
        }