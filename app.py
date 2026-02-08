import sys
import streamlit as st
from crew import ContentCalendarCrew
from file_generator import generate_pdf


if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

st.set_page_config(
    page_title="Content Calendar",
    page_icon="📅",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
    }
    .section-header {
        color: #667eea;
        border-left: 4px solid #764ba2;
        padding-left: 1rem;
        margin: 2rem 0 1rem 0;
    }
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 5px;
        font-weight: 600;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    .tip-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

if 'processing' not in st.session_state:
    st.session_state.processing = False
if 'result' not in st.session_state:
    st.session_state.result = None

st.markdown('<div class="main-header"><h1>Content Calendar Generator</h1><p>generate 30 days of content in minutes</p></div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-header">Brand information</h2>', unsafe_allow_html=True)

with st.form("content_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        brand_name = st.text_input("brand name", placeholder="your brand name here")
        industry = st.text_input("industry", placeholder="e.g. fashion, tech, food")
        brand_voice = st.selectbox(
            "brand voice",
            ["professional", "casual", "humorous", "inspirational", "educational", "friendly"]
        )
        target_audience = st.text_area(
            "target audience",
            placeholder="describe your ideal audience: age, profession, interests, pain points",
            height=100
        )
        
    with col2:
        content_goals = st.text_area(
            "content goals",
            placeholder="what do you want to achieve? (More engagement, brand awareness, drive sales, etc.)",
            height=100
        )
        platforms = st.multiselect(
            "platforms",
            ["linkedin", "twitter", "instagram", "facebook", "tiktok"],
            default=["tiktok", "twitter", "instagram"]
        )
        posting_frequency = st.select_slider(
            "posts per week",
            options=[1,2,3,4,5],
            value=3
        )
        content_themes = st.text_area(
            "content themes/topics",
            placeholder="e.g. sustainability, behind the scenes, product tips, user stories",
            height=100
        )
    
    st.markdown("### additional details")
    
    col3, col4 = st.columns(2)
    
    with col3:
        brand_values = st.text_area(
            "brand values",
            placeholder="what does your brand stand for?",
            height=80
        )
        competitors = st.text_input("main competitors", placeholder="competitor1, competitor2")
        
    with col4:
        special_events = st.text_area(
            "upcoming events/launches",
            placeholder="product launches, events, promotions",
            height=80
        )
        avoid_topics = st.text_input("topics to avoid", placeholder="politics, religion")
    
    st.markdown('<div class="tip-box">💡 tip: the more details you provide, the better your content calendar will be</div>', unsafe_allow_html=True)
    
    submit = st.form_submit_button("Generate content calendar", use_container_width=True)

if submit and not st.session_state.processing:
    if brand_name and industry and target_audience and content_goals:
        st.session_state.processing = True
        
        brand_input = f"""
        brand name: {brand_name}
        industry: {industry}
        brand voice: {brand_voice}
        
        target audience: {target_audience}
        
        content goals: {content_goals}
        
        platforms: {', '.join(platforms)}
        posting frequency: {posting_frequency} posts per week
        
        content themes:
        {content_themes}
        
        brand values: {brand_values or 'not specified'}
        competitors: {competitors or 'not specified'}
        upcoming events: {special_events or 'none'}
        avoid topics: {avoid_topics or 'none'}
        """
        
        with st.spinner("🎨 working on it... this may take a minute"):
            try:
                crew = ContentCalendarCrew()
                result = crew.execute(brand_input)
                st.session_state.result = result
                st.success("Calender is ready")
                
            except Exception as e:
                st.error(f"❌ error: {str(e)}")
            
        st.session_state.processing = False
        st.rerun()
    else:
        st.error("please fill required fields: brand name, industry, target audience, content goals")

if st.session_state.result:
    st.markdown('<h2 class="section-header"> your content calendar</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Download calendar")
        col1_1, col1_2 = st.columns(2)
        
        with col1_1:
            if st.button(" generate pdf", use_container_width=True):
                try:
                    with st.spinner("generating pdf..."):
                        pdf_path = generate_pdf(st.session_state.result)
                        
                        with open(pdf_path, 'rb') as f:
                            pdf_content = f.read()
                        
                        st.session_state.pdf_content = pdf_content
                        st.success("✅ pdf generated")
                        
                except Exception as e:
                    st.error(f"❌ error: {str(e)}")
                    import traceback
                    st.code(traceback.format_exc())
        
        with col1_2:
            if 'pdf_content' in st.session_state:
                st.download_button(
                    label="⬇️ download",
                    data=st.session_state.pdf_content,
                    file_name=f"{brand_name.replace(' ', '_')}_content_calendar.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
    
    with col2:
        st.markdown("### 📋 next steps")
        st.markdown("""
        1.  review generated content
        2.  customize posts to your style
        3.  schedule using your preferred tool
        4.  track performance metrics
        5.  iterate based on engagement
        """)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Powered by AI Content Calendar | <a href="https://github.com/OmarrAymann" style="color: #667eea; text-decoration: none;">@OmarAymann</a></p>
</div>
""", unsafe_allow_html=True)
