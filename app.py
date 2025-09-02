import streamlit as st
import google.generativeai as genai
import json

# 🔑 Put your Gemini API key here directly
GEMINI_API_KEY = "AI******ZI09TR******5bFmd*******RlM"

if not GEMINI_API_KEY:
    st.error("⚠️ Gemini API key missing! Add it in the code.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="CodeXR - AI Coding Assistant", layout="wide")
st.title("🤖 CodeXR: AI Coding Assistant for AR/VR Developers")

query = st.text_area("Enter your question (Unity, Unreal, Shader):", height=120)

def call_gemini(user_query: str):
    """
    Calls Gemini and forces JSON output for AR/VR developer queries.
    """
    prompt = f"""
You are CodeXR, an AI coding assistant for AR/VR developers (Unity C#, Unreal C++, Shaders).

User query: {user_query}

Respond ONLY in valid JSON format with these keys:
- subtasks (list of steps)
- code_snippet (string)
- gotchas (list of pitfalls)
- best_practices (list of tips)
- difficulty (Easy, Medium, Hard)
- documentation_link (string URL)

⚠️ Rules:
- Do NOT include explanations outside JSON.
- Do NOT use markdown.
- Output ONLY raw JSON.
    """

    response = model.generate_content(prompt)
    text = response.text.strip()

    # Try to parse JSON
    try:
        return json.loads(text)
    except:
        # If Gemini still adds extra text, clean it up
        try:
            start = text.index("{")
            end = text.rindex("}") + 1
            clean_text = text[start:end]
            return json.loads(clean_text)
        except:
            return {
                "subtasks": ["Model did not return valid JSON."],
                "code_snippet": text,
                "gotchas": [],
                "best_practices": [],
                "difficulty": "Unknown",
                "documentation_link": ""
            }


if st.button("Generate Answer"):
    if not query.strip():
        st.warning("Please enter a question first.")
    elif not GEMINI_API_KEY:
        st.error("⚠️ No Gemini API key provided. Add it in app.py.")
    else:
        with st.spinner("🤖 Thinking..."):
            output = call_gemini(query)

        # Display structured response
        st.subheader("📌 Subtasks")
        for step in output.get("subtasks", []):
            st.write("- " + step)

        st.subheader("💻 Code Snippet")
        st.code(output.get("code_snippet", ""), language=None)

        st.subheader("⚠️ Gotchas")
        for g in output.get("gotchas", []):
            st.write("- " + g)

        st.subheader("✅ Best Practices")
        for bp in output.get("best_practices", []):
            st.write("- " + bp)

        st.subheader("🎯 Difficulty")
        st.write(output.get("difficulty", "Unknown"))

        st.subheader("📖 Documentation")
        link = output.get("documentation_link", "")
        if link:
            st.markdown(f"[Open docs]({link})")
        else:
            st.write("No link provided.")

        st.subheader("🛠 Raw JSON")
        st.json(output)


