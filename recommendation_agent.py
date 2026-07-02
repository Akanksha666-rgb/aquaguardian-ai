class RecommendationAgent:

    def run(self, decision):

        recommendations = []

        poor = decision.get("poor_parameters", [])
        moderate = decision.get("moderate_parameters", [])

        # Critical fixes
        for param in poor:
            recommendations.append(f"⚠️ Treat or filter {param} immediately before consumption.")

        # Monitoring advice
        for param in moderate:
            recommendations.append(f"🔍 Monitor {param} regularly to maintain water quality.")

        if not recommendations:
            recommendations.append("✅ Water quality is excellent. No action required.")

        return {
            "recommendations": recommendations
        }