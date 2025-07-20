import streamlit as st

# Fancy page config
st.set_page_config(page_title="Diabetes Risk Checker", layout="centered")

# Custom CSS for background and text
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ef 100%);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    }
    .title {
        font-size: 2.6rem !important;
        font-weight: bold;
        color: #145da0;
    }
    .hint {
        color: #838383;
        font-size: 0.95em;
        margin-bottom: 0.7em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="title">🌱 Early Diabetes Risk Checker</div>', unsafe_allow_html=True)
    st.write("Answer the following questions to estimate your diabetes risk. [Information only. Not a medical diagnosis.]")

    # More questions with hints
    age = st.number_input('Age (years)', min_value=1, max_value=120, value=30)
    st.markdown('<span class="hint">Typically, risk increases after 45 years.</span>', unsafe_allow_html=True)

    bmi = st.number_input('Body Mass Index (BMI)', min_value=10.0, max_value=60.0, value=22.0, step=0.1, format="%.1f")
    st.markdown('<span class="hint">Normal: 18.5-24.9 | Overweight: 25-29.9 | Obese: 30+</span>', unsafe_allow_html=True)

    glucose = st.number_input('Fasting Glucose Level (mg/dL)', min_value=50, max_value=250, value=90)
    st.markdown('<span class="hint">Normal: 70–99 | Pre-diabetes: 100–125 | Diabetes: 126+</span>', unsafe_allow_html=True)

    blood_pressure = st.number_input('Systolic Blood Pressure (mm Hg)', min_value=50, max_value=220, value=120)
    st.markdown('<span class="hint">Normal: &lt;120 | High: 130+ (consult your doctor)</span>', unsafe_allow_html=True)

    family_history = st.radio('Family history of diabetes?', ('Yes', 'No'))
    st.markdown('<span class="hint">A parent or sibling with diabetes increases your risk.</span>', unsafe_allow_html=True)

    exercise = st.radio('Do you exercise regularly (150+ min/week)?', ('Yes', 'No'))
    st.markdown('<span class="hint">Regular exercise reduces diabetes risk.</span>', unsafe_allow_html=True)

    diet = st.radio('Do you often eat sugary or processed foods?', ('Yes', 'No'))
    st.markdown('<span class="hint">Frequent intake can raise risk. Balanced diet recommended.</span>', unsafe_allow_html=True)

    stress = st.radio('Do you experience high stress levels frequently?', ('Yes', 'No'))
    st.markdown('<span class="hint">Chronic stress can increase risk factors.</span>', unsafe_allow_html=True)

    # Assessment logic
    risk_points = 0
    if age >= 45:
        risk_points += 1
    if bmi >= 25:
        risk_points += 1
    if glucose >= 100:
        risk_points += 1
    if glucose >= 126:
        risk_points += 1  # add another for diabetic range
    if blood_pressure >= 130:
        risk_points += 1
    if family_history == 'Yes':
        risk_points += 1
    if exercise == 'No':
        risk_points += 1
    if diet == 'Yes':
        risk_points += 1
    if stress == 'Yes':
        risk_points += 1

    if st.button('Check My Diabetes Risk'):
        st.subheader("Your Diabetes Risk Result:")
        if risk_points >= 6:
            st.error('😟 **High Risk:** Please consult a healthcare professional soon. Early action matters.')
        elif risk_points >= 3:
            st.warning('⚠️ **Moderate Risk:** Consider lifestyle changes and periodic health checks.')
        else:
            st.success('😊 **Low Risk:** Keep up your healthy habits and stay active!')
        st.markdown("---")
        st.info("**Tips:** Eat a balanced diet, maintain healthy weight, exercise regularly, avoid excess sugar, and manage stress.")

    st.caption('Disclaimer: This tool is for informational purposes only and not a substitute for professional medical advice.')
    st.markdown('</div>', unsafe_allow_html=True)
