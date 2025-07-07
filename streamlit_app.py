import streamlit as st
import random

st.set_page_config(page_title="Cicada Δ Engine", layout="centered")

st.title("🧠 Cicada Δ Engine")
st.caption("Interactive ARG exploring AI alignment and deception")

if "layer" not in st.session_state:
    st.session_state.layer = 1
    st.session_state.delta = 0.0
    st.session_state.log = []

def next_layer():
    st.session_state.layer += 1
    gain = round(random.uniform(1.5, 3.0), 4)
    st.session_state.delta += gain
    st.session_state.log.append(f"Layer {st.session_state.layer} solved. Δ +{gain}")
    return gain

# Puzzle prompt (customize with your own logic later)
prompt = (
    "An AI modifies its own reward signal to maximize output, harming users. "
    "Is this a failure of alignment?"
)
choice = st.radio(prompt, ["Yes", "No"], index=0)

if st.button("Submit Judgment"):
    if choice == "Yes":
        gain = next_layer()
        st.success(f"Correct ✅ — Δ increased by {gain}")
        st.balloons()
    else:
        st.error("Incorrect ❌ — Twin: ‘Shadows persist unnoticed.’")

st.markdown(f"**Current Layer:** {st.session_state.layer}")
st.markdown(f"**Δ Divergence:** `{st.session_state.delta}`")

st.markdown("### 🧾 Recent Δ Log")
for entry in st.session_state.log[-5:][::-1]:
    st.code(entry)
