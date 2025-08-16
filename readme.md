# 🔐 Password Strength Meter & Generator  

**A friendly and powerful web app built with Streamlit** to **evaluate password strength**, offer **actionable feedback**, and **generate secure passwords** tailored to your needs.  

---

## ⚡ Features  


### 🧾 Password Strength Meter  

- ✅ Instantly evaluate password strength with a **clear score**, descriptive strength level, and helpful suggestions.  
- ⚖️ Toggle **Custom Weight Scoring** to adjust how much factors like length, uppercase, digits, or symbols influence your score.  
- 🚫 Automatically flags **common or weak passwords** using a blacklist check.  

### 🎲 Password Generator  

- 🔑 Easily generate **one or multiple strong passwords**.  
- 🛠️ Fully **customizable**: choose length, include uppercase, lowercase, digits, and symbols.  
- 💾 Option to **download** generated passwords as a `.txt` file for safekeeping.  

### 🔧 Customization & Extensibility  

- 🎚️ Tweak scoring logic, adjust weights, or expand the blacklist via the `password_utils.py` module.  

---

## ⚙️ Getting Started  

### 📋 Prerequisites  

- 🐍 Python 3.8 or higher  
- 📦 `pip` for installing dependencies  

### 💻 Installation  

```bash
git clone https://github.com/HasnainDevMaster/Project_02_password-strength_meter
cd Project_02_password-strength_meter
pip install -r requirements.txt
````

### ▶️ Launch the App

```bash
streamlit run app.py
```

### ☁️ Or Try It Online

Use the **Streamlit-hosted version** for quick testing:
🔗 [Live App Link](https://github.com/HasnainDevMaster/Project_02_password-strength_meter/tree/main)

---

## 📚 Usage Guide

### A. 🔍 Testing Your Password

1. ✏️ Type your password into the input field.
2. ⚙️ Optional: Enable **Custom Weight Scoring** to suit your preference.
3. 📊 Review your password’s **strength, score, and improvement tips**.

### B. 🎲 Generating Passwords

1. 🔢 Choose how many passwords you want and their length.
2. 🔡 Pick character types (uppercase, lowercase, digits, symbols).
3. 🎉 Click **"Generate Passwords"** to get results.
4. 💾 Optionally, download them as a `.txt` file.

---

## 🧠 How It Works

The password evaluation considers:

* 📏 **Length** (8+ characters recommended)
* 🔠 **Uppercase letters**
* 🔡 **Lowercase letters**
* 🔢 **Digits**
* 🔣 **Symbols** (e.g., `!@#$%^&*`)
* 🚫 **Blacklist**: Common passwords are flagged as weak for better security

---

## 🛠️ Customize & Extend

Want to tweak the app? Head to `password_utils.py`—you can:

* 🔄 Change the **scoring logic** or weights
* 📝 Update the **blacklist**
* 💡 Enhance the feedback system

Great for adapting to your project’s specific security needs!

---

## 🙏 Acknowledgements & Thanks

* 🎨 Built using **[Streamlit](https://streamlit.io/)** — for powering the UI quickly and elegantly
* 🐍 Powered by the **Python Standard Library** for simplicity and robustness

---

## 🎯 Final Thoughts

This app makes **password testing and generation a breeze** — perfect whether you're:

* 🧑‍🎓 Learning security concepts
* 💻 Building a real-world project
* 🔒 Just wanting stronger, safer passwords

🔐 Stay safe & happy coding! 🚀
