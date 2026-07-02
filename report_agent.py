class ReportAgent:

    def run(self, result):

        print("\n===== WATER QUALITY REPORT =====\n")

        # 🔴 SAFE SCORE EXTRACTION
        score_value = result.get("score", 0)

        # handle case where score is accidentally dict
        if isinstance(score_value, dict):
            score_value = score_value.get("score", 0)

        # force numeric safety
        try:
            score_value = float(score_value)
        except:
            score_value = 0.0

        # 🔴 SAFE GRADE EXTRACTION
        grade = result.get("grade", "N/A")

        # handle nested dict case
        if isinstance(grade, dict):
            grade = grade.get("grade", "N/A")

        print(f"Water Quality Score : {score_value}")
        print(f"Grade : {grade}")

        # OPTIONAL: unsafe parameters if exist
        poor_params = result.get("poor_parameters", [])
        moderate_params = result.get("moderate_parameters", [])

        print("\nPoor Parameters:", poor_params)
        print("Moderate Parameters:", moderate_params)

        print("\n=================================\n")

        # 🔴 NORMALIZE OUTPUT (IMPORTANT)
        result["score"] = score_value
        result["grade"] = grade

        return result