import streamlit as st
from snowflake.snowpark.context import get_active_session
from datetime import datetime
import base64
from io import BytesIO
from PIL import Image

# Snowflake session
session = get_active_session()

# Page setup
st.set_page_config(
    page_title="LIVSAFE AI - Home Inspection", 
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "LIVSAFE AI - AI-Powered Home Safety Inspection"
    }
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #2E7D32;
        --secondary-color: #66BB6A;
        --accent-color: #FFA726;
        --danger-color: #EF5350;
        --bg-color: #F5F7FA;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        margin: 0;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.95);
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Card styling */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 4px solid var(--primary-color);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .metric-card h3 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .metric-card p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    
    /* Image container */
    .image-container {
        border: 3px dashed var(--primary-color);
        border-radius: 10px;
        padding: 1rem;
        background: rgba(46, 125, 50, 0.05);
    }
    
    /* Alert boxes */
    .alert-success {
        background: linear-gradient(135deg, #66BB6A 0%, #81C784 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .alert-warning {
        background: linear-gradient(135deg, #FFA726 0%, #FFB74D 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .alert-danger {
        background: linear-gradient(135deg, #EF5350 0%, #E57373 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Section headers */
    .section-header {
        color: var(--primary-color);
        font-size: 1.8rem;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid var(--secondary-color);
    }
    
    /* Feature boxes */
    .feature-box {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .feature-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);
        color: white;
        border-radius: 10px;
        margin-top: 3rem;
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Progress indicator */
    .progress-step {
        display: inline-block;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: var(--primary-color);
        color: white;
        text-align: center;
        line-height: 30px;
        margin-right: 0.5rem;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="main-header">
    <h1>🏠 LIVSAFE AI</h1>
    <p>AI-Powered Home Inspection Using Advanced Image Analysis</p>
</div>
""", unsafe_allow_html=True)

# ---------------- FEATURE HIGHLIGHTS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🔍</div>
        <h4>Smart Analysis</h4>
        <p style="color: gray; font-size: 0.9rem;">AI-powered inspection</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">⚡</div>
        <h4>Instant Results</h4>
        <p style="color: gray; font-size: 0.9rem;">Real-time detection</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🛡️</div>
        <h4>Safety First</h4>
        <p style="color: gray; font-size: 0.9rem;">Comprehensive checks</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">📊</div>
        <h4>Detailed Reports</h4>
        <p style="color: gray; font-size: 0.9rem;">Actionable insights</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- HERO IMAGE ----------------
st.markdown('<div class="image-container">', unsafe_allow_html=True)
st.image(
    "https://images.unsplash.com/photo-1580587771525-78b9dba3b914",
    caption="🏡 Professional home inspection powered by AI technology",
    use_container_width=True
)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PROPERTY SELECTION ----------------
st.markdown('<p class="section-header">🏢 Property Details</p>', unsafe_allow_html=True)

st.markdown('<div class="info-card">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    property_name = st.text_input(
        "Property Name",
        placeholder="e.g. GreenView Apartment",
        help="Enter the name or address of the property"
    )
with col2:
    room_name = st.selectbox(
        "Room Type",
        ["Bedroom", "Kitchen", "Bathroom", "Living Room", "Balcony", "Staircase"],
        help="Select the type of room being inspected"
    )
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- IMAGE UPLOAD ----------------
st.markdown('<p class="section-header">📸 Upload Home Image</p>', unsafe_allow_html=True)

st.markdown('<div class="info-card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Choose an image of the room for AI analysis",
    type=["jpg", "png", "jpeg"],
    help="Supported formats: JPG, PNG, JPEG (Max 200MB)"
)

if uploaded_file:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(uploaded_file, caption="✅ Uploaded Image Ready for Analysis", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Display image info
    image = Image.open(uploaded_file)
    st.markdown(f"""
    <div style="background: #F0F4F8; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
        <strong>📋 Image Details:</strong><br>
        • Format: {image.format}<br>
        • Dimensions: {image.size[0]} x {image.size[1]} pixels<br>
        • File Size: {uploaded_file.size / 1024:.2f} KB
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- OBSERVED ISSUES (HUMAN-IN-THE-LOOP) ----------------
st.markdown('<p class="section-header">👁️ Observed Issues</p>', unsafe_allow_html=True)

observed_issues = st.multiselect(
    "Select issues you can visibly observe in the image",
    [
        "Wall dampness / moisture",
        "Cracks in wall or ceiling",
        "Exposed electrical wiring",
        "Water leakage",
        "Unsafe staircase or railing",
        "Poor ventilation",
        "No visible issues"
    ],
    help="AI will reason based on these observed issues"
)

# ---------------- RUN AI BUTTON ----------------
st.markdown("<br>", unsafe_allow_html=True)
run_ai = st.button("🧠 Run AI Inspection", use_container_width=True)

if not run_ai:
    st.markdown("""
    <div class="info-card" style="text-align: center; background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%); border-left: 4px solid #2196F3;">
        <h4 style="color: #1976D2; margin: 0;">📌 Ready to Start</h4>
        <p style="color: #424242; margin: 0.5rem 0 0 0;">
            Upload an image and click <strong>Run AI Inspection</strong> to begin analysis
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Validation
if not property_name:
    st.error("⚠️ Please enter a property name before running the inspection.")
    st.stop()

if not uploaded_file:
    st.error("⚠️ Please upload an image before running the inspection.")
    st.stop()

# ---------------- VALIDATION FOR OBSERVED ISSUES ----------------
if not observed_issues:
    st.error("⚠️ Please select at least one observed issue before running AI inspection.")
    st.stop()

# ---------------- AI IMAGE ANALYSIS ----------------
st.markdown('<p class="section-header">🔍 AI Image Analysis</p>', unsafe_allow_html=True)

with st.spinner("🤖 AI is analyzing the image... Please wait"):
    # Prepare the AI prompt with proper escaping
    ai_image_prompt = f"""
You are a certified home inspection AI assisting a human inspector.

Room Type: {room_name}

The inspector uploaded an image and observed the following issues:
{', '.join(observed_issues)}

Your tasks:
1. Assess safety, health, and fire risks
2. Explain why these issues matter
3. Classify overall risk level (Low / Medium / High)
4. Suggest immediate corrective actions

Be realistic, safety-focused, and easy to understand.
"""
    
    # Try multiple models in order of availability
    models_to_try = ['snowflake-arctic', 'mistral-7b', 'llama3.1-8b', 'mixtral-8x7b', 'mistral-large']
    
    ai_result = None
    last_error = None
    image_description = None
    
    for model in models_to_try:
        try:
            # Properly escape single quotes for SQL
            escaped_prompt = ai_image_prompt.replace("'", "''")
            
            ai_query = f"""
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    '{model}',
    '{escaped_prompt}'
) AS description
"""
            ai_result = session.sql(ai_query).to_pandas()
            image_description = ai_result.iloc[0]["DESCRIPTION"]
            st.success(f"✅ Using model: {model}")
            break
        except Exception as e:
            last_error = e
            continue
    
    if image_description:
        st.markdown('<div class="alert-success">', unsafe_allow_html=True)
        st.markdown("### ✅ AI Analysis Completed Successfully")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(f"**Analysis Result:**\n\n{image_description}")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error(f"❌ Error during AI analysis: {str(last_error)}")
        st.stop()

# ---------------- STORE AI RESULT ----------------
try:
    # Properly escape single quotes for SQL INSERT
    escaped_property = property_name.replace("'", "''")
    escaped_room = room_name.replace("'", "''")
    escaped_description = image_description.replace("'", "''")
    escaped_issues = ', '.join(observed_issues).replace("'", "''")
    
    session.sql(f"""
INSERT INTO uploaded_images (property_name, room_name, image_description)
VALUES (
    '{escaped_property}',
    '{escaped_room}',
    '{escaped_description}'
)
""").collect()
    st.success("💾 Results saved to database successfully!")
    debug_df = session.sql("""
    SELECT * FROM uploaded_images ORDER BY uploaded_at DESC LIMIT 5 """).to_pandas()
    st.subheader("🧪 Debug: Recently Saved Inspections")
    st.dataframe(debug_df, use_container_width=True)

except Exception as e:
    st.warning(f"⚠️ Could not save to database: {str(e)}")

# ---------------- PROPERTY REPORT ----------------
st.markdown('<p class="section-header">📊 Overall Property Safety Report</p>', unsafe_allow_html=True)

try:
    report_df = session.sql("""
SELECT * FROM final_report ORDER BY inspection_date DESC
""").to_pandas()
    
    if not report_df.empty:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.dataframe(
            report_df, 
            use_container_width=True,
            hide_index=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Summary metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{len(report_df)}</h3>
                <p>Total Inspections</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                <h3>{report_df['PROPERTY_NAME'].nunique()}</h3>
                <p>Properties Analyzed</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
                <h3>{report_df['ROOM_NAME'].nunique()}</h3>
                <p>Room Types Checked</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("📝 No previous inspection reports found.")
except Exception as e:
    st.warning(f"⚠️ Could not load property report: {str(e)}")

# ---------------- AI EXPLANATION ----------------
st.markdown('<p class="section-header">🧠 AI Safety Recommendations</p>', unsafe_allow_html=True)

with st.spinner("🤖 Generating detailed safety recommendations..."):
    explain_prompt = f"""
Based on this inspection result:
{image_description}

Explain:
1. What risk this indicates
2. Why it matters to families
3. What should be fixed first
"""
    
    # Properly escape single quotes for SQL
    escaped_explain_prompt = explain_prompt.replace("'", "''")
    
    explain_query = f"""
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'llama3.1-8b',
    '{escaped_explain_prompt}'
) AS explanation
"""
    
    try:
        explain_result = session.sql(explain_query).to_pandas()
        explanation = explain_result.iloc[0]["EXPLANATION"]
        
        st.markdown('<div class="alert-warning">', unsafe_allow_html=True)
        st.markdown("### 💡 Expert Recommendations")
        st.markdown(explanation)
        st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"⚠️ Could not generate detailed recommendations: {str(e)}")

def generate_inspection_report(property_name, room_name, observed_issues, ai_result):
    report = f"""
LIVSAFE AI – HOME SAFETY INSPECTION REPORT
========================================

Property Name : {property_name}
Room Inspected: {room_name}
Inspection Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

----------------------------------------
OBSERVED ISSUES
----------------------------------------
"""
    for issue in observed_issues:
        report += f"- {issue}\n"

    report += f"""
----------------------------------------
AI SAFETY ANALYSIS
----------------------------------------
{ai_result}

----------------------------------------
DISCLAIMER
----------------------------------------
This report is generated using AI-assisted inspection.
It does not replace a certified structural audit.

Generated by LIVSAFE AI
"""
    return report



# ---------------- ACTION ITEMS ----------------
st.markdown('<p class="section-header">✅ Next Steps</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h4>🔧 Immediate Actions</h4>
        <ul style="color: #424242;">
            <li>Review all identified safety issues</li>
            <li>Prioritize critical repairs</li>
            <li>Document current conditions</li>
            <li>Get professional quotes if needed</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h4>📅 Follow-up</h4>
        <ul style="color: #424242;">
            <li>Schedule repairs with contractors</li>
            <li>Re-inspect after fixes</li>
            <li>Maintain regular inspection schedule</li>
            <li>Keep records for compliance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DOWNLOAD REPORT ----------------
st.markdown('<p class="section-header">📥 Export Options</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📄 Download Inspection Report", use_container_width=True):
        report_text = generate_inspection_report(
            property_name,
            room_name,
            observed_issues,
            image_description
        )

        st.download_button(
            label="⬇️ Click to Download",
            data=report_text,
            file_name="LIVSAFE_Inspection_Report.txt",
            mime="text/plain"
        )


with col2:
    if st.button("📧 Email Report", use_container_width=True):
        email_body = f"""
LIVSAFE AI – Home Inspection Report

Property: {property_name}
Room: {room_name}

AI Findings:
{image_description}

Thank you,
LIVSAFE AI
"""

        st.text_area(
            "📧 Email Preview (Copy & Send)",
            email_body,
            height=250
        )


with col3:
    if st.button("🔄 New Inspection", use_container_width=True):
        st.rerun()


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <h3 style="margin: 0;">🌍 LIVSAFE AI</h3>
    <p style="margin: 0.5rem 0; opacity: 0.9;">
        AI for Good • Image-based Inspection • Built on Snowflake Cortex
    </p>
    <p style="margin: 0.5rem 0; font-size: 0.9rem; opacity: 0.8;">
        Powered by Advanced Machine Learning • Protecting Families Worldwide
    </p>
    <p style="margin: 1rem 0 0 0; font-size: 0.85rem; opacity: 0.7;">
        © 2026 LIVSAFE AI • All Rights Reserved
    </p>
</div>
""", unsafe_allow_html=True)