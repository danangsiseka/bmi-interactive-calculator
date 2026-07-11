# BMI Interactive Calculator (Python)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)

---

## 🔭 Project Overview

BMI Interactive Calculator is a beginner-friendly Python application that calculates Body Mass Index (BMI), classifies the user's BMI category, and provides lifestyle evaluations through a simple Yes/No questionnaire.

The project demonstrates the use of fundamental Python programming concepts, including user input, mathematical operations, conditional statements (`if-elif-else`), and basic decision-making logic.

---

## 🛠️ Features

- Calculate BMI using weight and height.
- Supports both **Male** and **Female** users.
- Automatic BMI classification:
  - Underweight
  - Normal
  - Overweight
  - Obesity
- Interactive lifestyle assessment (Yes/No questions).
- Personalized health suggestions based on:
  - BMI category
  - User habits
  - Gender
- Simple command-line interface suitable for beginners.

---

## 📐 BMI Formula

The BMI value is calculated using the standard formula:

```text
BMI = Weight (kg) / Height² (m²)
```

Example:

```text
Weight : 70 kg
Height : 170 cm

BMI = 70 / (1.70 × 1.70)
BMI = 24.22
```

---

## 🧠 Programming Concepts

This project intentionally uses only fundamental Python features:

- Variables
- Input & Output
- Arithmetic operators
- `if`, `elif`, and `else`
- Nested conditional statements
- String processing
- Basic mathematical calculations

No external libraries are required.

---

## 📋 Program Workflow

```text
Start
   │
   ▼
Input Gender
   │
Input Weight & Height
   │
Calculate BMI
   │
Determine BMI Category
   │
 ┌───────────────┐
 │ BMI Normal ?  │
 └──────┬────────┘
        │
   Yes  │  No
        │
        ▼
 Display      Lifestyle Quiz
 Success            │
 Message            ▼
              Analyze Answers
                    │
                    ▼
          Personalized Feedback
                    │
                    ▼
                   End
```

---

## ▶️ Example Output

```text
===== BMI RESULT =====

BMI = 27.45
Category = Overweight

Lifestyle Assessment

1. Do you rarely exercise? (Yes/No): Yes
2. Do you frequently consume sugary foods? (Yes/No): Yes
3. Do you sleep less than 7 hours a day? (Yes/No): No

Feedback:
Reduce sugary food intake and increase physical activity to gradually achieve a healthy BMI.
```

---

## 📚 Educational Purpose

This project was created for learning purposes to practice:

- Basic Python programming
- Conditional logic
- User interaction
- Problem solving
- Program flow design

It is **not intended to replace professional medical advice or diagnosis**.

---

## 📄 License

This project is available under the MIT License.
