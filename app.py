import streamlit as st
from password_utils import (
    evaluate_password, generate_strong_password, evaluate_with_weights
)
import io

st.set_page_config(page_title="Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Meter")

# --- Password Strength Section ---
st.header("🧪 Test Your Password")
password = st.text_input("Enter a password to evaluate:", type="password")

use_custom_weights = st.checkbox("Use Custom Weight Scoring")

if use_custom_weights:
    st.markdown("### 🎯 Customize Weights (0–5)")
    length_w = st.slider("Length", 0, 5, 1)
    upper_w = st.slider("Uppercase", 0, 5, 1)
    lower_w = st.slider("Lowercase", 0, 5, 1)
    digit_w = st.slider("Digits", 0, 5, 1)
    symbol_w = st.slider("Symbols", 0, 5, 1)

weights = {
    'length': length_w if use_custom_weights else 1,
    'uppercase': upper_w if use_custom_weights else 1,
    'lowercase': lower_w if use_custom_weights else 1,
    'digits': digit_w if use_custom_weights else 1,
    'symbols': symbol_w if use_custom_weights else 1,
}

if password:
    try:
        score, max_score, strength, suggestions = evaluate_with_weights(password, weights)

        st.markdown(f"**Score**: {score} / {max_score}")
        if strength == "Strong":
            st.success("✅ Password Strength: Strong")
        elif strength == "Moderate":
            st.warning("⚠️ Password Strength: Moderate")
        else:
            st.error("❌ Password Strength: Weak")

        if suggestions:
            st.markdown("### 🔧 Suggestions:")
            for s in suggestions:
                st.write(f"- {s}")
        else:
            st.success("✅ No suggestions needed!")
    except Exception as e:
        st.error(f"An error occurred while evaluating the password: {str(e)}")

# --- Password Generator ---
st.markdown("---")
st.subheader("🔄 Generate Password(s)")

length = st.slider("Password Length", 8, 32, 12)  # Increased minimum length to 8
num_passwords = st.number_input("Number of passwords", 1, 10, 1)
use_upper = st.checkbox("Include Uppercase (A-Z)", value=True)
use_lower = st.checkbox("Include Lowercase (a-z)", value=True)
use_digits = st.checkbox("Include Digits (0–9)", value=True)
use_symbols = st.checkbox("Include Symbols (!@#$%^&*)", value=True)

generated_passwords = []

if st.button("Generate Passwords"):
    if not (use_upper or use_lower or use_digits or use_symbols):
        st.error("Please select at least one character type for password generation.")
    else:
        try:
            st.markdown("### 🔐 Your Password(s):")
            for _ in range(num_passwords):
                pwd = generate_strong_password(length, use_upper, use_lower, use_digits, use_symbols)
                st.code(pwd, language="text")
                generated_passwords.append(pwd)
        except ValueError as e:
            st.error(str(e))

# --- Download as Text File ---
if generated_passwords:
    st.markdown("### 📁 Download Passwords as `.txt`")
    text_data = "\n".join(generated_passwords)
    st.download_button(
        label="📥 Download .txt",
        data=text_data.encode(),  # ✅ Convert to bytes
        file_name="generated_passwords.txt",
        mime="text/plain"
    )
