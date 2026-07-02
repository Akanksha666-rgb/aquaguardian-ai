import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class ExplanationAgent:

    def run(self, result):

        print("[ExplanationAgent] Generating explanation using Gemini...")

        prompt = f"""
The water quality analysis result is:

Summary:
{result.get("summary", "")}

Score:
{result.get("score", "")}

Grade:
{result.get("grade", "")}

Decision:
{result.get("decision", "")}

Risk:
{result.get("risk", "")}

Recommendation:
{result.get("recommendation", "")}

Explain in simple English whether the water is safe to drink and why.
Keep it within 3–4 sentences.
"""

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            explanation = response.text

        except Exception:
            explanation = (
                "AI explanation is temporarily unavailable due to API limits."
            )

        print("[ExplanationAgent] Explanation:", explanation)

        return {
            "summary": result.get("summary"),
            "score": result.get("score"),
            "grade": result.get("grade"),
            "decision": result.get("decision"),
            "risk": result.get("risk"),
            "recommendation": result.get("recommendation"),
            "explanation": explanation
        }