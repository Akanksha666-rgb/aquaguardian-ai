import streamlit as st
import os
import pandas as pd
import datetime
import plotly.graph_objects as go

from workflow import AquaGuardianWorkflow
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AquaGuardian AI Dashboard",
    page_icon="🚰",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.markdown("""
<div style="
    text-align:center;
    padding:15px;
    background:linear-gradient(90deg,#0D47A1,#42A5F5);
    border-radius:15px;
    color:white;
">
    <h1>🚰 AquaGuardian AI Dashboard</h1>
    <p>Multi-Agent Water Quality Intelligence System</p>
</div>
<br>
""", unsafe_allow_html=True)
# ---------------- SIDEBAR INPUT ---------------- #

st.sidebar.header("⚙️ Water Parameters")

ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0, 0.1)
tds = st.sidebar.slider("TDS", 0, 1000, 200)
hardness = st.sidebar.slider("Hardness", 0, 500, 150)
fluoride = st.sidebar.slider("Fluoride", 0.0, 3.0, 1.0, 0.1)
iron = st.sidebar.slider("Iron", 0.0, 2.0, 0.3, 0.1)
nitrate = st.sidebar.slider("Nitrate", 0, 100, 45)
chlorine = st.sidebar.slider("Chlorine", 0.0, 5.0, 0.5, 0.1)
conductivity = st.sidebar.slider("Conductivity", 0, 2000, 500)
turbidity = st.sidebar.slider("Turbidity", 0, 100, 2)
calcium = st.sidebar.slider("Calcium", 0, 200, 40)
magnesium = st.sidebar.slider("Magnesium", 0, 100, 20)
potassium = st.sidebar.slider("Potassium", 0, 50, 5)
sodium = st.sidebar.slider("Sodium", 0, 100, 10)


# ---------------- GAUGE METER ---------------- #

def show_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Water Quality Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#1E88E5"},
            "steps": [
                {"range": [0, 50], "color": "#ff4d4d"},
                {"range": [50, 75], "color": "#ffa500"},
                {"range": [75, 100], "color": "#2ecc71"},
            ],
        }
    ))

    fig.update_layout(height=300)
    return fig


# ---------------- PDF GENERATOR ---------------- #

def generate_pdf(result):

    file_name = "water_report.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)

    # ---------------- HEADER ---------------- #
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "AquaGuardian AI - Water Quality Report")

    c.setFont("Helvetica", 11)
    c.drawString(50, 730, f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # ---------------- BASIC INFO ---------------- #
    c.drawString(50, 700, f"Score: {result.get('score', 0):.2f}")
    c.drawString(50, 680, f"Grade: {result.get('grade', 'N/A')}")
    c.drawString(50, 660, f"Decision: {result.get('decision', {}).get('status', '')}")
    c.drawString(50, 640, f"Risk: {result.get('risk', {}).get('risk_level', '')}")

    # ---------------- MINERALS ---------------- #
    c.drawString(50, 610, "Water Parameters:")

    minerals = result.get("input_data", {})

    y = 590
    for key, value in minerals.items():
        c.drawString(60, y, f"{key.upper()}: {value}")
        y -= 15

        if y < 100:   # page break safety
            c.showPage()
            y = 750

    # ---------------- AI EXPLANATION ---------------- #
    c.drawString(50, y-20, "AI Explanation:")

    text = c.beginText(60, y-40)
    text.setFont("Helvetica", 10)

    explanation = result.get("explanation", "")

    for line in explanation.split("."):
        text.textLine(line.strip())

    c.drawText(text)

    c.save()

    return file_name

# ---------------- ANALYZE BUTTON ---------------- #

if st.sidebar.button("🔍 Analyze Water"):

    workflow = AquaGuardianWorkflow()

    input_data = {
        "ph": ph,
        "tds": tds,
        "hardness": hardness,
        "fluoride": fluoride,
        "iron": iron,
        "nitrate": nitrate,
        "chlorine": chlorine,
        "conductivity": conductivity,
        "turbidity": turbidity,
        "calcium": calcium,
        "magnesium": magnesium,
        "potassium": potassium,
        "sodium": sodium
    }

    with st.spinner("Running AI Water Analysis..."):
        result = workflow.run(input_data)
        result["input_data"] = input_data
    st.success("Analysis Completed Successfully 🚀")

    # ---------------- GAUGE ---------------- #

    st.subheader("📊 Water Quality Score")
    st.plotly_chart(show_gauge(result.get("score", 0)), use_container_width=True)


    # ---------------- METRICS ---------------- #

    col1, col2, col3 = st.columns(3)

    st.metric("🏆 Grade", result.get("grade", "N/A"))

    risk = result.get("risk", {}).get("risk_level", "Unknown")
    decision = result.get("decision", {}).get("status", "Unknown")

    with col1:
        st.metric("⚠️ Risk Level", risk)

    with col2:
        st.metric("💧 Status", decision)

    with col3:
        st.metric("📊 Score", f"{result.get('score', 0):.2f}")


    # ---------------- AI EXPLANATION ---------------- #

    st.subheader("🧠 AI Explanation")
    st.info(result.get("explanation", "No explanation available"))


    # ---------------- RECOMMENDATIONS ---------------- #

    st.subheader("📌 Recommendations")

    for rec in result.get("recommendation", {}).get("recommendations", []):
        st.write("✔", rec)


    # ---------------- PDF DOWNLOAD ---------------- #

    pdf_file = generate_pdf(result)

    with open(pdf_file, "rb") as f:
        st.download_button(
            label="📄 Download Water Report",
            data=f,
            file_name="AquaGuardian_Report.pdf",
            mime="application/pdf"
        )


# ---------------- HISTORY ---------------- #

st.markdown("---")
st.subheader("📊 Water Quality History")

if os.path.exists("water_history.csv"):
    history = pd.read_csv("water_history.csv")

    history.columns = history.columns.str.strip().str.lower()

    if "score" in history.columns:
        st.line_chart(history["score"])
    else:
        st.warning("Score column missing in history file")
        st.dataframe(history)

else:
    st.info("No history available yet. Run analysis to generate data.")


# ---------------- FOOTER ---------------- #

st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>AquaGuardian AI • Multi-Agent Water Intelligence System</p>",
    unsafe_allow_html=True
    
)
