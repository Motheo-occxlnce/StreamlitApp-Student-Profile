# Research Student Profile Dashboard 🎓

A professional, single-page "Bento-style" dashboard built with Streamlit to showcase the research profile, skills, and academic output of *Motheo Mahlatse Maoto Nkadimeng*.

![Dashboard Preview](https://via.placeholder.com/800x450.png?text=Dashboard+Preview)

## 🚀 Features

*   **Responsive Bento Grid Layout**: A modern 3-column layout that organizes information into cohesive cards.
*   **Interactive Visualizations**:
    *   **Radar Chart**: Visualizes core technical competencies.
    *   **Donut Chart**: Displays research focus distribution.
    *   **Skill Bars**: Showcases proficiency in specialized tools.
*   **Dynamic Sidebar**: Navigation menu, contact details, and Github integration.
*   **Custom Styling**: Integrated `style.css` for a polished, dark-themed sidebar and clean card aesthetics (soft shadows, rounded corners, uniform heights).
*   **No-Scroll Design**: Optimized for a single-screen experience on standard desktop displays.

## 🛠️ Tech Stack

*   **Python 3.10+**
*   **Streamlit**: Frontend framework.
*   **Plotly**: Interactive charting library.
*   **HTML/CSS**: Custom component styling.

## 📦 Installation

1.  **Clone the repository** (or download code):
    ```bash
    git clone <repository_url>
    cd research-profile-dashboard
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install streamlit plotly
    ```

## ▶️ Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open automatically in your default browser at `http://localhost:8501`.

## 📂 Project Structure

```
├── app.py           # Main application logic and layout
├── style.css        # Custom CSS for styling cards and sidebar
├── README.md        # Project documentation
└── extract_cv.py    # (Utility) Script for extracting text from source CV
```

## 👤 Author

**Motheo Mahlatse Maoto Nkadimeng**
*Meng Industrial Engineering Data Science*

---
*Built with ❤️ using Streamlit*
