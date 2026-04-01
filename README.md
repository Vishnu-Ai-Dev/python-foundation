# 🐍 Python Foundation — 30-Day Master Plan

> "Invest in silence during the building phase. Let the work speak when the time comes." — Dad's Philosophy

From zero to confident Python developer. This repository documents my 30-day journey from basic syntax to advanced OOP, data manipulation, and visualization.

---

## 📊 Repository Overview

**Status:** Complete ✅ (March 4 - March 31, 2026)

**What's Inside:**
- 30 days of structured Python learning
- Daily progress tracked with Git commits
- 6 completed projects demonstrating mastery
- Clean code following PEP 8 standards

**Tech Stack:**
- Python 3.12
- Jupyter Notebooks (Week 4 onwards)
- NumPy, Pandas, Matplotlib
- Scikit-learn (preview)

---

## 🎯 Learning Path

### **Week 1-3: Python Fundamentals**
Syntax → Data Types → Control Flow → Functions → OOP Basics

- Variables, operators, and control structures
- Lists, tuples, dictionaries, sets
- Function definition and scope
- Introduction to Object-Oriented Programming

**Key Files:** `day_01_to_21/` folder

---

### **Week 4: Data Science Toolkit**

#### NumPy — Numerical Computing
- Array creation and manipulation
- Mathematical operations
- Broadcasting
- Linear algebra basics

#### Pandas — Data Manipulation
- DataFrames and Series
- Data cleaning
- Filtering and grouping
- Reading/writing CSV files

#### Matplotlib — Data Visualization
- Line plots, bar charts, scatter plots
- Subplots and styling
- Real-world data visualization

**Key Files:** `day_22_onwards/numpy_advanced.ipynb`, `pandas_operations.ipynb`, `matplotlib_guide.ipynb`

---

## 🚀 Projects Completed

### **1. Anime Password Generator** 🎌
**What:** Random password generator using external anime APIs

**Why:** Shows independent thinking beyond basic tutorials — using real APIs instead of hardcoded data

**Tech:** Python requests library, JSON parsing

**File:** `projects/anime_password_generator.py`

---

### **2. Military Drone Inheritance** 🚁
**Day:** 17 | **Concept:** Multi-Level Inheritance

**What:** 
```
autonomous_robot (parent)
  └─ surveillance_drone
       └─ stealth_drone (child)
```

**Features:**
- Battery state management
- Inheritance chain demonstrating real-world hierarchy
- Polymorphic methods

**File:** `projects/day_17_military_drone.py`

**Lesson Learned:** Inheritance is about modeling REAL relationships, not syntax.

---

### **3. CNN/RNN/Transformer Polymorphism** 🧠
**Day:** 18 | **Concept:** Polymorphism in Action

**What:** Three different ML model classes with identical `train()` method signature but different behavior

```python
class CNNModel(BaseModel):
    def train(self): # CNN-specific training
    
class RNNModel(BaseModel):
    def train(self): # RNN-specific training
    
class TransformerModel(BaseModel):
    def train(self): # Transformer-specific training
```

**Why This Matters:** Accidentally mirrors PyTorch architecture — understanding polymorphism unlocks understanding modern ML frameworks

**File:** `projects/day_18_ml_polymorphism.py`

---

### **4. AI Research Kernel — Full OOP Master** 🤖
**Day:** 20 | **Concept:** Complete OOP Integration

**Architecture:**
```
BaseAI (parent class)
  ├─ ComputerVision
  ├─ NaturalLanguage
  └─ RobotController
```

**Features:**
- `__api_key` encapsulation (private attribute)
- Method inheritance and overriding
- Real-world initialization
- Demonstrates all 4 OOP pillars

**Planned First:** Drew on paper, understood the hierarchy, THEN coded

**File:** `projects/day_20_ai_research_kernel.py`

**Key Insight:** "Plan on paper first" changed everything about how I approach problems

---

### **5. Linear Regression Preview** 📈
**Day:** 22 (NumPy Day)

**What:** Built linear regression manually with NumPy before learning Scikit-learn

**Why:** Understanding the math (slope, intercept, predict) makes frameworks less magical

```python
slope = covariance(X, y) / variance(X)
intercept = mean(y) - slope * mean(X)
predictions = slope * X + intercept
```

**File:** `day_22_onwards/linear_regression_preview.ipynb`

---

### **6. Tamil Nadu Budget 2025 Visualization** 📊
**Date:** March 30, 2026

**What:** Real government data → Cleaned → Visualized

**Dataset:** Tamil Nadu State Budget 2025 (actual CSV)

**Process:**
1. Downloaded official budget CSV
2. Cleaned with Pandas (handled missing values, formatted dates)
3. Created bar charts comparing budget allocations
4. Posted on LinkedIn

**File:** `projects/tamil_nadu_budget_viz.ipynb`

**GitHub:** [Pushed & committed](https://github.com/Vishnu-Ai-Dev)

**Why This Matters:** Shows I can work with REAL data, not just toy datasets

---

## 📈 Skills Progression

| Week | Focus | Confidence |
|------|-------|-----------|
| 1-2 | Syntax & Fundamentals | ⭐⭐⭐⭐⭐ |
| 3 | Functions & OOP Intro | ⭐⭐⭐⭐⭐ |
| 4 | NumPy, Pandas, Matplotlib | ⭐⭐⭐⭐ |

---

## 💡 Key Learnings

### **"Think on Paper First"**
- Day 20 (AI Kernel): Drew the class hierarchy before coding
- Result: Code was clean, logical, required fewer rewrites

### **Independent Thinking**
- Day 1: Used external API instead of hardcoded list
- This signals "I don't copy-paste tutorials blindly"

### **Real Data > Toy Data**
- Tamil Nadu Budget: Government data, real problems
- Forces you to handle messy reality

### **OOP is About Modeling Reality**
- Not just syntax rules
- Inheritance = "is-a" relationships
- Polymorphism = "different objects, same interface"

---

## 📂 File Structure

```
python_foundation/
├── day_01_to_21/
│   ├── day_01_variables.py
│   ├── day_05_lists_tuples.py
│   ├── day_10_functions.py
│   ├── day_15_oop_basics.py
│   └── day_17_inheritance_intro.py
│
├── day_22_onwards/ (Jupyter Notebooks)
│   ├── numpy_basics.ipynb
│   ├── numpy_advanced.ipynb
│   ├── pandas_operations.ipynb
│   ├── matplotlib_guide.ipynb
│   └── linear_regression_preview.ipynb
│
├── projects/
│   ├── anime_password_generator.py
│   ├── day_17_military_drone.py
│   ├── day_18_ml_polymorphism.py
│   ├── day_20_ai_research_kernel.py
│   └── tamil_nadu_budget_viz.ipynb
│
├── data/
│   ├── tamil_nadu_budget_2025.csv
│   └── sample_datasets/
│
└── README.md (this file)
```

---

## 🎓 What This Proves

**To Myself:**
- I can learn systematically
- I follow through on goals
- I understand WHY, not just HOW

**To Universities/Employers:**
- Daily commits = consistency
- 6 completed projects = follow-through
- Real data projects = practical thinking
- Clean code = professional standards

---

## 🔥 Next Phase

**Phase 2:** Machine Learning Foundations (April - May 2026)
- Scikit-learn: Linear/Logistic Regression, Decision Trees, KNN, SVM
- Real ML datasets (Kaggle competitions)
- Model evaluation: Accuracy, confusion matrix, cross-validation

**Phase 3:** Deep Learning + Feature Engineering (June - July 2026)
- PyTorch basics
- MNIST digit recognition
- Anime image classifier

---

## 📝 How to Use This Repo

**For Learning:**
1. Start with `day_01_to_21/` for fundamentals
2. Week 4 Jupyter notebooks for data science
3. `projects/` folder for integrated examples

**For Reference:**
- Each file has comments explaining logic
- Projects have docstrings explaining architecture

**For Inspiration:**
- See how OOP applies to real problems
- Data visualization with real datasets
- Building beyond tutorials

---

## 🎯 The Philosophy

> "Not like I am trying — I need to ensure I am going there."

This repository is proof of that mindset:
- ✅ Consistent daily progress
- ✅ Projects with depth, not breadth
- ✅ Understanding over memorization
- ✅ Real data, real problems
- ✅ Professional code quality

---

## 🚀 Stats

- **30 days:** March 4 - March 31, 2026
- **Daily commits:** ✅ Logged
- **Projects completed:** 6
- **Lines of code:** 2,000+
- **Concepts mastered:** 40+
- **From:** Zero Python
- **To:** Ready for ML Phase

---

## 🤝 Connect

- **GitHub:** [@Vishnu-Ai-Dev](https://github.com/Vishnu-Ai-Dev)
- **LinkedIn:** Building in public 🔥
- **Goal:** Masters in AI/ML from Japan (2029)

---

**Last Updated:** March 31, 2026

"Invest in silence during the building phase. Let the work speak when the time comes."
