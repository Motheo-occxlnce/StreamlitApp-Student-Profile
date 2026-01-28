import streamlit as st
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Research Profile | Motheo Mahlatse Maoto Nkadimeng",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- LOAD CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

try:
    local_css("style.css")
except FileNotFoundError:
    st.warning("style.css not found.")

# --- DATA ---
profile_data = {
    "name": "Motheo Mahlatse Maoto Nkadimeng",
    "role": "Physics & Engineering Professional",
    "email": "HMkasi@csir.co.za",
    "phone": "071 192 7150",
    "institution": "North-West University / TUT",
    "location": "Pretoria, South Africa",
    "current_role": "Meng Industrial Engineering Data Science",
    "summary": "Detail-oriented physics and engineering professional with experience in precision measurement, optical systems, and calibration. Skilled in analyzing measurement datasets using Python and supporting engineering teams in research and manufacturing environments.",
}

skills_data = {
    "Optics & Laser Systems": 95,
    "Python & Linux (Data Analysis)": 90,
    "Metrology & Calibration": 75,
    "Scientific Reporting": 85,
}

competencies = ["Data Analysis", "Optics & Lasers", "Metrology", "Python/Coding", "Reporting"]
competency_values = [85, 90, 75, 88, 80]

research_focus = {"Physics": 40, "Eng.": 35, "Solar": 25}

recent_output = [
    {"title": "SASAS 2024 Conference", "desc": "Analysis of Surface Albedo at Irene Station"},
    {"title": "Procurement Optimization", "desc": "HLTC Braamfischer Case Study"},
    {"title": "PV Defect Detection", "desc": "Infrared Imaging Analysis"},
]

references = [
    {"initials": "KN", "name": "Dr. Ncongwane"},
    {"initials": "BM", "name": "Mr. Mabasa"},
    {"initials": "WM", "name": "Mr. Mkasi"},
]

toolkit_icons = ["📊", "🏠", "📋", "📈", "⚙️", "🔒", "📉", "👁️", "🔧"]

supervisor = {"initials": "KN", "name": "Dr. Katlego Ncongwane", "dept": "SAWS Research & Dev"}

# --- HELPER FUNCTIONS ---
def create_radar_chart():
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=competency_values + [competency_values[0]],
        theta=competencies + [competencies[0]],
        fill='toself',
        fillcolor='rgba(59, 130, 246, 0.2)',
        line=dict(color='#3b82f6', width=2),
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], showticklabels=False, gridcolor='#e5e7eb'),
            angularaxis=dict(gridcolor='#e5e7eb', linecolor='#e5e7eb'),
            bgcolor='rgba(0,0,0,0)',
        ),
        showlegend=False,
        margin=dict(l=60, r=60, t=40, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=200,
    )
    return fig

def create_donut_chart():
    fig = go.Figure(data=[go.Pie(
        labels=list(research_focus.keys()),
        values=list(research_focus.values()),
        hole=0.65,
        marker=dict(colors=['#3b82f6', '#8b5cf6', '#22c55e']),
        textinfo='none',
    )])
    fig.update_layout(
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5, font=dict(size=10)),
        margin=dict(l=20, r=20, t=20, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        height=200,
        annotations=[dict(text='<b>4 Major</b><br>Projects', x=0.5, y=0.5, font=dict(size=14, color='#1a2b3c'), showarrow=False)]
    )
    return fig

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="text-align: center; padding-bottom: 2rem;"><div style="width: 70px; height: 70px; background: #3b82f6; border-radius: 50%; margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: white;">MN</div><h4 style="color: white; margin: 0;">Motheo N.</h4><p style="color: #94a3b8; font-size: 0.8rem; margin: 0;">Researcher</p></div>', unsafe_allow_html=True)
    st.markdown('<p style="color: #64748b; font-size: 0.75rem; font-weight: 600; letter-spacing: 1px; margin-bottom: 1rem;">CONTACT</p>', unsafe_allow_html=True)
    st.markdown('<div style="display: flex; align-items: flex-start; padding: 0.5rem 0; color: #cbd5e1;"><span style="margin-right: 0.75rem; font-size: 1rem;">📍</span><span style="font-size: 0.8rem; line-height: 1.4;">Emily Hobhouse, Pretoria, 0116</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="display: flex; align-items: flex-start; padding: 0.5rem 0; color: #cbd5e1;"><span style="margin-right: 0.75rem; font-size: 1rem;">✉️</span><span style="font-size: 0.8rem; line-height: 1.4;">nkadimengmotheo8@gmail.com</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="display: flex; align-items: flex-start; padding: 0.5rem 0; color: #cbd5e1;"><span style="margin-right: 0.75rem; font-size: 1rem;">📞</span><span style="font-size: 0.8rem; line-height: 1.4;">072 294 4031 / 081 653 8078</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 2rem"></div>', unsafe_allow_html=True)
    st.markdown('<p style="color: #64748b; font-size: 0.75rem; font-weight: 600; letter-spacing: 1px; margin-bottom: 1rem;">MAIN MENU</p>', unsafe_allow_html=True)
    for label, icon in [("Dashboard", "🏠"), ("Experience", "💼"), ("Research", "🔬"), ("Education", "🎓")]:
        st.markdown(f'<div style="display: flex; align-items: center; padding: 0.75rem 0; color: #cbd5e1;"><span style="margin-right: 1rem; font-size: 1.1rem;">{icon}</span><span style="font-size: 0.9rem;">{label}</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="margin-top: 3rem;"><a href="https://github.com" target="_blank" style="display: block; width: 100%; background: #24292e; color: white; border: none; padding: 0.75rem; border-radius: 12px; font-weight: 600; cursor: pointer; text-align: center; text-decoration: none;">GitHub</a></div>', unsafe_allow_html=True)

# --- MAIN LAYOUT ---
main_col, right_col = st.columns([3, 1])

with main_col:
    # Row 1
    r1c1, r1c2 = st.columns(2)
    
    with r1c1:
        with st.container():
            st.markdown('<div class="chart-card">', unsafe_allow_html=True)
            st.markdown('<h3 class="card-title">Core Competencies</h3><p class="card-subtitle">Technical proficiency breakdown</p>', unsafe_allow_html=True)
            st.plotly_chart(create_radar_chart(), use_container_width=True, config={'displayModeBar': False})
            st.markdown('</div>', unsafe_allow_html=True)
            
    with r1c2:
        with st.container():
            skills_html = ''.join([f'<div class="skill-item"><div class="skill-name">{n}</div><div class="skill-bar"><div class="skill-fill {c}" style="width: {v}%;"></div></div></div>' for (n, v), c in zip(skills_data.items(), ['blue', 'blue', 'green', 'orange'])])
            st.markdown(f'<div class="chart-card"><h3 class="card-title">Specialized Skills</h3><p class="card-subtitle">cv & field work</p><div style="margin-top: 1.5rem;">{skills_html}</div></div>', unsafe_allow_html=True)

    # Row 2
    r2c1, r2c2 = st.columns(2)
    
    with r2c1:
        with st.container():
            st.markdown('<div class="chart-card">', unsafe_allow_html=True)
            st.markdown('<h3 class="card-title">Research Focus</h3><p class="card-subtitle">Time distribution by field</p>', unsafe_allow_html=True)
            st.plotly_chart(create_donut_chart(), use_container_width=True, config={'displayModeBar': False})
            st.markdown('</div>', unsafe_allow_html=True)
            
    with r2c2:
        with st.container():
            output_html = ''.join([f'<div class="output-item"><div class="output-icon"></div><div class="output-content"><p class="output-title">{i["title"]}</p><p class="output-description">{i["desc"]}</p></div><span class="output-arrow">›</span></div>' for i in recent_output])
            st.markdown(f'<div class="chart-card"><h3 class="card-title">Recent Output</h3><p class="card-subtitle">Active projects</p>{output_html}</div>', unsafe_allow_html=True)

    # Row 3
    r3c1, r3c2 = st.columns(2)
    
    with r3c1:
        refs_html = ''.join([f'<div class="reference-item"><div class="reference-avatar">{r["initials"]}</div><p class="reference-name">{r["name"]}</p></div>' for r in references])
        st.markdown(f'<div class="chart-card small-card"><h3 class="card-title">References</h3><p class="card-subtitle">History</p><div style="display: flex; justify-content: space-around; margin-top: 1rem;">{refs_html}</div></div>', unsafe_allow_html=True)
        
    with r3c2:
        icons_html = ''.join([f'<div class="toolkit-icon">{i}</div>' for i in toolkit_icons])
        st.markdown(f'<div class="chart-card small-card"><h3 class="card-title">Toolkit</h3><p class="card-subtitle">Reward earned 3/12</p><div class="toolkit-grid">{icons_html}</div></div>', unsafe_allow_html=True)

with right_col:
    # Profile Panel
    profile_html = '<div class="profile-panel">'
    profile_html += '<div class="profile-avatar-large">😎</div>'
    profile_html += '<h2 class="profile-name-large">Motheo Mahlatse<br>Maoto Nkadimeng</h2>'
    profile_html += '<p class="profile-handle">@researcher_motheo</p>'
    profile_html += '<div class="profile-details">'
    profile_html += '<div class="detail-row"><span class="detail-icon">📅</span> <span>Meng Industrial Engineering Data Science</span></div>'
    profile_html += f'<div class="detail-row"><span class="detail-icon">🏛️</span> <span>{profile_data["institution"]}</span></div>'
    profile_html += f'<div class="detail-row"><span class="detail-icon">📍</span> <span>{profile_data["location"]}</span></div>'
    profile_html += '</div>'
    profile_html += '<div class="profile-about">'
    profile_html += '<h4 class="about-title">About Me</h4>'
    profile_html += f'<p class="about-text">{profile_data["summary"]}</p>'
    profile_html += '</div>'
    profile_html += '<div class="supervisor-card-dark">'
    profile_html += '<div class="supervisor-header"><span class="supervisor-title">Supervisor</span><span class="supervisor-icon">⤢</span></div>'
    profile_html += '<div class="supervisor-content">'
    profile_html += f'<div class="supervisor-avatar">{supervisor["initials"]}</div>'
    profile_html += '<div class="supervisor-info">'
    profile_html += f'<h4>{supervisor["name"]}</h4>'
    profile_html += f'<p>{supervisor["dept"]}</p>'
    profile_html += '</div></div></div></div>'
    
    st.markdown(profile_html, unsafe_allow_html=True)
