Step 1: Prepare Your Project Folder

CodeXR_Project/
│── app.py
│── requirements.txt
│── README.md
│── demo_screenshots/
│     ├── unity_demo.png
│     ├── unreal_demo.png
│     ├── shader_demo.png


Step 2: Prepare requirements.txt
streamlit
google-generativeai


Step 3: Readme file
# 🤖 CodeXR – AI Coding Assistant for AR/VR Developers

CodeXR is a **Streamlit-based AI assistant** that helps AR/VR developers with:
- ✅ Subtasks breakdown
- ✅ Code snippets (Unity C#, Unreal C++, Shaders)
- ✅ Gotchas (common pitfalls)
- ✅ Best practices
- ✅ Difficulty rating
- ✅ Documentation links
- ✅ Raw JSON output

Powered by **Google Gemini API**.

---

## 🚀 Demo Scenarios

### 🎮 Unity (Teleport Locomotion)
![Unity Demo](demo_screenshots/unity_demo.png)

### 🕹️ Unreal (Multiplayer Setup)
![Unreal Demo](demo_screenshots/unreal_demo.png)

### 🎨 Shader (AR Occlusion)
![Shader Demo](demo_screenshots/shader_demo.png)

---

## 🛠 Installation & Setup

1. Clone the repository:
   git clone https://github.com/your-username/CodeXR.git
   cd CodeXR
   
2. Create a virtual environment:

    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate # On Mac/Linux

3. Install dependencies:

   pip install -r requirements.txt

4. Add your Gemini API Key inside app.py:

    GEMINI_API_KEY = "your_api_key_here"

5. Run the app:
    streamlit run app.py

6. Open in your browser:
    http://localhost:8501
