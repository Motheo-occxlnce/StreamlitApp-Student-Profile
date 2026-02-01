import streamlit as st
import pandas as pd
import base64
import os

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set page configuration
st.set_page_config(
    page_title="Motheo N. - Research Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to mimic the clean look of the HTML
st.markdown("""
<style>
    /* Global Styles */
    .main {
        background-color: #f8fafc; /* Slate-50 */
        color: #0f172a; /* Slate-900 */
        font-family: 'Inter', sans-serif;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #0f172a;
    }
    
    /* Cards/Containers */
    .stContainer {
        border-radius: 0.75rem;
    }
    
    /* Metrics/Stats */
    div[data-testid="stMetricValue"] {
        font-size: 1.5rem;
    }
    
    /* Custom Badge Style */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid #e2e8f0;
    }
    
    /* Remove padding at top */
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Profile Header in Sidebar
    col_sb1, col_sb2 = st.columns([1, 3])
    with col_sb1:
        st.markdown("""
        <div style="width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(to top right, #3b82f6, #2dd4bf); display: flex; align-items: center; justify-content: center; font-weight: bold; color: white;">MN</div>
        """, unsafe_allow_html=True)
    with col_sb2:
        st.markdown("**Motheo N.**\n\n<span style='color: #94a3b8; font-size: 0.75rem;'>Researcher</span>", unsafe_allow_html=True)
    
    st.divider()
    
    # Navigation
    selected = st.radio(
        "Navigation",
        ["Dashboard", "Experience", "Research", "Education"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Download CV
    # Sidebar Utilities
    st.write("") # Spacer
    
    col_btn = st.columns(1)
    
    st.write("") # Micro spacer

    # Source Code Button
    st.link_button(
        "Source Code (GitHub)",
        "https://github.com/Motheo-occxlnce/StreamlitApp-Student-Profile",
        use_container_width=True,
        icon="💻" 
    )

# Main Content
if selected == "Dashboard":
    # Header
    st.title("Dashboard")
    st.markdown("**Research Profile** > **Dashboard**")
    
    st.divider()

    # Row 1: Profile & About
    col1, col2 = st.columns([1, 2])
    
    with col1:
        with st.container(border=True):
            # Load Profile Image
            img_path = "High_DA25128-038.jpg"
            if os.path.exists(img_path):
                img_base64 = get_base64_of_bin_file(img_path)
                img_html = f'<img src="data:image/jpeg;base64,{img_base64}" style="width: 96px; height: 96px; border-radius: 50%; object-fit: cover; margin: 0 auto 1rem auto; display: block; border: 4px solid white; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);">'
            else:
                img_html = '<div style="width: 96px; height: 96px; border-radius: 50%; background-color: #f1f5f9; margin: 0 auto 1rem auto; display: flex; align-items: center; justify-content: center; font-size: 1.875rem; font-weight: bold; color: #cbd5e1; border: 4px solid white; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);">MN</div>'

            st.markdown(f"""
            <div style="text-align: center;">
                {img_html}
                <h2 style="font-size: 1.25rem; font-weight: bold; margin-bottom: 0.25rem;">Motheo Mahlatse Maoto Nkadimeng</h2>
                <p style="color: #2563eb; font-weight: 500; font-size: 0.875rem;">MEng Industrial Engineering Data Science Student</p>
                <p style="color: #64748b; font-size: 0.875rem; display: flex; align-items: center; justify-content: center; gap: 0.25rem; margin-bottom: 1rem;">
                    🎓 Stellenbosch University
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            
            st.markdown("""
            <div style="font-size: 0.875rem; color: #475569; display: flex; flex-direction: column; gap: 0.5rem;">
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <span>📍</span> <span>Emily Hobhouse, Pretoria, 0116</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <span>📧</span> <a href="mailto:nkadimengmotheo8@gmail.com" style="color: inherit; text-decoration: none; hover: color: #2563eb;">nkadimengmotheo8@gmail.com</a>
                </div>
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <span>📞</span> <span>072 294 4031 / 081 653 8078</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    with col2:
        # About Me
        with st.container(border=True):
            st.subheader("👤 About Me")
            st.markdown("""
            Highly motivated, dedicated, and results-oriented Industrial Engineering Master’s student with experience in research and development. Former Energy and application research intern at the South African Weather Service (SAWS). I am eager to contribute through innovative solutions, continuous learning, and tackling of new challenges.
            """)
        
        # Stats
        st.write("") # Spacer
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        
        with stat_col1:
            with st.container(border=True):
                st.markdown("**Focus**")
                st.markdown("### Data Science")
                st.caption("Industrial Eng.")
                
        with stat_col2:
            with st.container(border=True):
                st.markdown("**Toolkit Reward**")
                st.markdown("### 3/12")
                st.progress(25)
                
        with stat_col3:
            with st.container(border=True):
                st.markdown("**Output**")
                st.markdown("### 3")
                st.caption("Active Projects")

    # Row 2: Skills & Research Focus
    st.write("") # Spacer
    col3, col4 = st.columns([1, 2])
    
    with col3:
        # Technical Skills
        with st.container(border=True):
            st.subheader("Technical Skills")
            skills = [
                ("🔍", "Research Methodology", "blue"),
                ("📊", "Data Analysis", "purple"),
                ("🖊️", "Scientific Report Writing", "green"),
                ("📂", "Project Administration", "orange"),
                ("💻", "Programming", "gray")
            ]
            for icon, name, color in skills:
                st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.75rem;">
                    <div style="padding: 0.5rem; border-radius: 0.5rem; background-color: {color if color != 'gray' else '#e2e8f0'}; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center;">{icon}</div>
                    <span style="font-weight: 500; font-size: 0.875rem; color: #334155;">{name}</span>
                </div>
                """, unsafe_allow_html=True)

    with col4:
        # Research Focus
        with st.container(border=True):
            st.subheader("Research Focus & Specialization")
            st.caption("2024-2025")
            
            st.markdown("**Time Distribution**")
            
            # Custom Progress Bars
            research_areas = [
                ("Data Science", 40),
                ("Energy Systems", 35),
                ("Photonics", 15),
                ("Admin/Writing", 10)
            ]
            
            for area, pct in research_areas:
                subcol_a, subcol_b = st.columns([1, 4])
                with subcol_a:
                    st.text(area)
                with subcol_b:
                    st.progress(pct)
            
            st.markdown("**Core Areas**")
            core_areas = ["Data Science", "Data Analytics", "Applied Deep Learning", "Energy & Applications", "Photonics"]
            
            badges_html = "".join([f'<span class="badge" style="background-color: #f8fafc; color: #475569;">{area}</span>' for area in core_areas])
            st.markdown(f"<div>{badges_html}</div>", unsafe_allow_html=True)

    # Row 3: Output & Toolkit
    st.write("") # Spacer
    col5, col6 = st.columns(2)
    
    with col5:
        # Recent Output
        with st.container(border=True):
            st.subheader("Recent Output")
            
            projects = [
                ("Procurement Optimization", "HLTC Braamfischer Case Study", "2025", "amber"),
                ("Analysis of Surface Albedo", "SASAS Conference at Irene Station", "2024", "blue"),
                ("PV Defect Detection", "Infrared Imaging Analysis", "2023", "green")
            ]
            
            for title, desc, year, color in projects:
                st.markdown(f"""
                <div style="padding-left: 1rem; border-left: 2px solid #e2e8f0; margin-bottom: 1rem; position: relative;">
                    <div style="position: absolute; left: -5px; top: 0; width: 8px; height: 8px; border-radius: 50%; background-color: #3b82f6;"></div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div>
                            <div style="font-weight: bold; color: #1e293b;">{title}</div>
                            <div style="font-size: 0.875rem; color: #64748b;">{desc}</div>
                        </div>
                        <span style="font-size: 0.75rem; padding: 0.125rem 0.5rem; border-radius: 0.25rem; background-color: #fffbeb; border: 1px solid #fcd34d; color: #b45309;">{year}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with col6:
        # Toolkit
        with st.container(border=True):
            st.subheader("Toolkit")
            
            # Grid of tools (Using columns)
            tools = [
                ("📊", "Data Viz"), ("🏠", "Streamlit"), ("📋", "Reporting"),
                ("📈", "Analytics"), ("⚙️", "Engineering"), ("🔒", "Security"),
                ("📉", "Modeling"), ("👁️", "Comp Vision"), ("🔧", "Optimization")
            ]
            
            t_cols = st.columns(3)
            for i, (icon, name) in enumerate(tools):
                with t_cols[i % 3]:
                    st.markdown(f"""
                    <div style="background-color: #f8fafc; border-radius: 0.5rem; padding: 0.5rem; text-align: center; margin-bottom: 0.5rem; border: 1px solid transparent;">
                        <div style="font-size: 1.5rem;">{icon}</div>
                        <div style="font-size: 0.75rem; color: #475569; font-weight: 500;">{name}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
        # References
        with st.container(border=True):
            st.subheader("References")
            ref_cols = st.columns(3)
            refs = [
                ("KN", "Dr. Ncongwane"),
                ("BM", "Mr. Mabasa"),
                ("WM", "Mr. Mkasi")
            ]
            for i, (initials, name) in enumerate(refs):
                with ref_cols[i]:
                    st.markdown(f"""
                    <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
                        <div style="width: 40px; height: 40px; border-radius: 50%; background-color: #1e293b; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.75rem; margin-bottom: 0.25rem;">{initials}</div>
                        <div style="font-weight: bold; font-size: 0.875rem; color: #0f172a;">{name}</div>
                        <div style="font-size: 0.75rem; color: #64748b;">Reference</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
# Other tabs placeholders
elif selected == "Experience":
    st.title("Professional Experience")
    st.markdown("**Research Profile** > **Experience**")
    
    st.divider()
    
    # Experience Timeline
    with st.container(border=True):
        col_exp1, col_exp2 = st.columns([1, 4])
        with col_exp1:
            st.markdown("**May 2024 – May 2025**")
            st.caption("Internship")
        with col_exp2:
            st.subheader("Energy and Application Research Intern")
            st.markdown("**South African Weather Service (SAWS)**")
            st.markdown("""
            - Performed analysis of large environmental and optical-related datasets using Python and Bash.
            - Conducted quality checks on observational data from biometeorological stations to ensure accuracy.
            - Assisted with installation and hardware alignment of Sky Vue 8 LIDAR optical measurement equipment.
            - Produced scientific reports and monthly statistical summaries with traceable data documentation.
            - Consolidated verification documents (invoices, timesheets) ensuring traceable record-keeping.
            """)
            
    st.write("")
    
    with st.container(border=True):
        col_exp3, col_exp4 = st.columns([1, 4])
        with col_exp3:
            st.markdown("**May 2021 – Dec 2021**")
            st.caption("Assistant")
        with col_exp4:
            st.subheader("Student Assistant")
            st.markdown("**Tshwane University of Technology**")
            st.markdown("""
            - Provided academic aid for the Department of Mathematics and Statistics.
            - Invigilated second-year mathematics students during assessments.
            - Assisted with the marking of scripts for second-year students.
            """)
            
    st.divider()
    
    # References
    st.subheader("References Available")
    
    ref_col1, ref_col2 = st.columns(2)
    
    with ref_col1:
        with st.container(border=True):
            st.markdown("### Dr. Katlego Ncongwane")
            st.markdown("**Senior Manager, SAWS R&D**")
            st.markdown("📧 katlego.ncongwane@weathersa.co.za")
            
    with ref_col2:
        with st.container(border=True):
            st.markdown("### Mr. Brighton Mabasa")
            st.markdown("**Scientist, SAWS Energy**")
            st.markdown("📧 Brightmabasa@gmail.com")
elif selected == "Research":
    st.title("Research Projects & Output")
    st.markdown("**Research Profile** > **Research**")
    
    st.divider()
    
    # Project 1
    with st.container(border=True):
        col_r1, col_r2 = st.columns([1, 3])
        with col_r1:
            st.caption("2024-2025")
            st.markdown("**Data Science**")
            st.markdown('<span class="badge" style="background-color: #f0f9ff; color: #0284c7; border: 1px solid #bae6fd;">Framework</span>', unsafe_allow_html=True)
        with col_r2:
            st.subheader("Procurement Optimization Framework")
            st.markdown("**HLTC Braamfischer Case Study**")
            st.markdown("Developed a framework for optimizing the procurement and resource allocation process within a large-scale housing project context.")
            
            st.write("")
            st.markdown("""
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">Industrial Eng</span>
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">Process Optimization</span>
            """, unsafe_allow_html=True)
            
    st.write("")
    
    # Project 2
    with st.container(border=True):
        col_r3, col_r4 = st.columns([1, 3])
        with col_r3:
            st.caption("SASAS 2024")
            st.markdown("**Conference Paper**")
            st.markdown('<span class="badge" style="background-color: #fff7ed; color: #ea580c; border: 1px solid #fed7aa;">Published</span>', unsafe_allow_html=True)

        with col_r4:
            st.subheader("Surface Albedo Characteristics")
            st.markdown("**Analysis at Irene Station, Pretoria**")
            st.markdown("Validated surface albedo characteristics (minutely to seasonal). Compared remotely sensed datasets (CMSAF CLARA, MERRA-2, ERA5) with observed data using statistical metrics.")
            
            st.write("")
            st.markdown("""
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">Remote Sensing</span>
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">Statistical Analysis</span>
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">Industrial Physics</span>
            """, unsafe_allow_html=True)

    st.write("")

    # Project 3
    with st.container(border=True):
        col_r5, col_r6 = st.columns([1, 3])
        with col_r5:
            st.caption("2022")
            st.markdown("**Defect Detection**")
        with col_r6:
            st.subheader("PV Module Defect Detection")
            st.markdown("**Infrared Imaging Analysis**")
            st.markdown("Utilized Infrared Imaging technology to detect and analyze defects in photovoltaic modules, contributing to quality assurance protocols in renewable energy tech.")
            
            st.write("")
            st.markdown("""
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">IR Imaging</span>
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">NDT</span>
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">Material Science</span>
            """, unsafe_allow_html=True)
            
    st.write("")

    # Project 4
    with st.container(border=True):
        col_r7, col_r8 = st.columns([1, 3])
        with col_r7:
            st.caption("2021")
            st.markdown("**Fabrication**")
        with col_r8:
            st.subheader("Thermal Measurement Fabrication")
            st.markdown("**Epoxy and Carbon Nanotubes**")
            st.markdown("Research focused on the fabrication of thermal measurement devices using a composite of epoxy and carbon nanotubes.")
            
            st.write("")
            st.markdown("""
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">Nanotech</span>
            <span class="badge" style="background-color: #f1f5f9; color: #475569;">Photonics</span>
            """, unsafe_allow_html=True)
elif selected == "Education":
    st.title("Education & Qualifications")
    st.markdown("**Research Profile** > **Education**")
    
    st.divider()

    # Edu 1
    with st.container(border=True):
        col_ed1, col_ed2 = st.columns([1, 4])
        with col_ed1:
            st.markdown("**Current**")
            st.caption("Started 2026")
            st.markdown("🎓 **Masters**")
        with col_ed2:
            st.subheader("MEng Industrial Engineering Data Science")
            st.markdown("**Stellenbosch University**")
            st.info("Specializing in advanced data analytics, industrial engineering applications, and research methodology.")

    st.write("")

    # Edu 2
    with st.container(border=True):
        col_ed3, col_ed4 = st.columns([1, 4])
        with col_ed3:
            st.markdown("**2024 - 2025**")
            st.caption("Postgrad Diploma")
        with col_ed4:
            st.subheader("Postgraduate Diploma in Industrial Engineering")
            st.markdown("**North-West University**")
            st.markdown("**Key Coursework:** Software Engineering (Python Focus), Operations Excellence, Data & Decision Science, Quality Management, Simulation Modelling, Supply Chain Management.")

    st.write("")

    # Edu 3
    with st.container(border=True):
        col_ed5, col_ed6 = st.columns([1, 4])
        with col_ed5:
            st.markdown("**2022**")
            st.caption("Postgrad Diploma")
        with col_ed6:
            st.subheader("Postgraduate Diploma in Industrial Physics")
            st.markdown("**Tshwane University of Technology**")
            st.markdown("**Key Coursework:** Industrial Ventilation, Photovoltaic Technology, Quantum & Solid-state Physics, Optical Design II, Laser & Fibre Optics II, Nanotechnology Analytical Techniques.")

    st.write("")

    # Edu 4
    with st.container(border=True):
        col_ed7, col_ed8 = st.columns([1, 4])
        with col_ed7:
            st.markdown("**2021 - 2022**")
            st.caption("Advanced Diploma")
        with col_ed8:
            st.subheader("Advanced Diploma in Industrial Physics")
            st.markdown("**Tshwane University of Technology**")
            st.markdown("**Focus:** Advanced Physics, Optical Design, Electromagnetism, Radiometry, and Photometry.")

    st.write("")

    # Edu 5
    with st.container(border=True):
        col_ed9, col_ed10 = st.columns([1, 4])
        with col_ed9:
            st.markdown("**2018 - 2021**")
            st.caption("Diploma")
        with col_ed10:
            st.markdown("**Focus:** Non-destructive Testing (NDT), Electronics, Engineering Drawing, Photonics I & II, Physics & Chemistry.")

