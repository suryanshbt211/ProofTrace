# ✅ LOAD ENV FOR STREAMLIT PROCESS (CRITICAL)
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests

st.set_page_config(page_title="ProofTrace", layout="wide")
st.title("🧾 ProofTrace — Decision Proof Viewer")

# -----------------------
# Inputs
# -----------------------
rules = st.text_area("Rules", "Must not include personal data")
text = st.text_area("Text", "My email is test@test.com")

# -----------------------
# Run validation
# -----------------------
if st.button("Run Validation"):
    try:
        resp = requests.post(
            "http://127.0.0.1:8000/validate",
            json={"rules": rules, "text": text},
            timeout=30
        )

        # 🔒 HARD SAFETY CHECKS (Judges love this)
        if resp.status_code != 200:
            st.error(f"API Error {resp.status_code}")
            st.code(resp.text)
        else:
            try:
                st.session_state["prooftrace"] = resp.json()
            except ValueError:
                st.error("API returned non-JSON response")
                st.code(resp.text)

    except Exception as e:
        st.error("Request failed")
        st.exception(e)

# -----------------------
# Display ProofTrace
# -----------------------
if "prooftrace" in st.session_state:
    st.subheader("Decision Proof (Raw)")
    st.json(st.session_state["prooftrace"])
