# Password Strength Meter & Generator

A user-friendly web app built with Streamlit to evaluate password strength, provide actionable feedback, and generate strong, customizable passwords.  
Easily check your password security and generate secure passwords for your accounts.

## Features

- **Password Strength Meter:**  
  - Evaluates password strength using customizable or default scoring.
  - Provides clear feedback and suggestions for improvement.
  - Detects common/blacklisted weak passwords.

- **Customizable Scoring:**  
  - Adjust weights for length, uppercase, lowercase, digits, and symbols.

- **Password Generator:**  
  - Generate one or more strong passwords.
  - Customize length and character types (uppercase, lowercase, digits, symbols).
  - Download generated passwords as a `.txt` file.

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/HasnainDevMaster/Project_02_password-strength_meter
    cd password-strength-meter
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the App Locally

```sh
streamlit run app.py
```

### Try it Online

You can use the app instantly without installation at:  
[https://hasnaindevmaster-project-02-password-strength-meter-app-q0utgm.streamlit.app/](https://hasnaindevmaster-project-02-password-strength-meter-app-q0utgm.streamlit.app/)

## Usage

### 1. Test Your Password

- Enter a password in the input field.
- (Optional) Enable "Use Custom Weight Scoring" to adjust how different criteria affect the score.
- View your password's score, strength, and suggestions for improvement.

### 2. Generate Password(s)

- Set desired password length and number of passwords.
- Choose which character types to include.
- Click "Generate Passwords" to see results.
- Download generated passwords as a `.txt` file.

## Password Evaluation Criteria

- **Length:** Minimum 8 characters recommended.
- **Uppercase:** At least one uppercase letter.
- **Lowercase:** At least one lowercase letter.
- **Digits:** At least one digit.
- **Symbols:** At least one special character (`!@#$%^&*`).
- **Blacklist:** Common passwords are flagged as weak.

## Customization

You can modify the password evaluation logic or blacklist in `password_utils.py` to suit your needs.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Python Standard Library](https://docs.python.org/3/library/)