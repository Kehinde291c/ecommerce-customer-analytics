# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Clone and Setup
```bash
git clone https://github.com/yourusername/ecommerce-customer-analytics.git
cd ecommerce-customer-analytics
pip install -r requirements.txt
```

### Step 2: Generate Data (if needed)
```bash
python src/generate_data.py
```

### Step 3: Run Analysis
```bash
# Option A: Interactive Jupyter Notebook (Recommended)
jupyter notebook notebooks/customer_analytics.ipynb

# Option B: Python Script
python src/churn_model.py
```

## 📊 What You'll Get

### Analysis Outputs
- **customer_data.csv**: Main dataset with 5,000 customers
- **high_risk_customers.csv**: List of at-risk customers
- **Visualizations**: 7 publication-quality charts

### Key Metrics
- Overall churn rate: 18.7%
- Model accuracy: 85%+ ROC-AUC
- Identified: 300+ high-risk customers
- Revenue at risk: $237k+

## 🎯 Key Files

| File | Purpose |
|------|---------|
| `customer_analytics.ipynb` | Main analysis notebook |
| `generate_data.py` | Create synthetic dataset |
| `churn_model.py` | Standalone model training |
| `customer_data.csv` | Main dataset |
| `README.md` | Full documentation |

## 💡 Quick Tips

### For Interviews/Presentations
1. Start with the **churn_distribution.png** visualization
2. Highlight the **18.7% churn rate** finding
3. Show the **feature importance** chart
4. Discuss the **business recommendations**

### For GitHub Portfolio
1. Add screenshots to README
2. Include badges for technologies used
3. Link to live Jupyter notebook (nbviewer)
4. Mention specific skills demonstrated

### For LinkedIn
- "Reduced potential churn-related revenue loss by identifying 300+ at-risk customers"
- "Built predictive model with 85% accuracy using Random Forest"
- "Performed customer segmentation using RFM analysis"
- "Generated actionable insights from 5,000 customer records"

## 🔍 Project Highlights for Resume

**Skills Demonstrated:**
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Feature engineering
- Machine learning (classification)
- Model evaluation and validation
- Data visualization
- Business insight generation

**Technologies:**
Python | Pandas | NumPy | Scikit-Learn | Matplotlib | Seaborn | Jupyter

**Methodologies:**
- RFM Segmentation
- Random Forest Classification
- Cross-validation
- ROC-AUC Analysis
- Feature Importance Analysis

## 📈 Customization Ideas

Want to make this project your own? Try:

1. **Add Time Series Analysis**: Track churn trends over time
2. **Compare Models**: Try Logistic Regression, XGBoost, Neural Networks
3. **Feature Engineering**: Create interaction features, polynomial features
4. **Hyperparameter Tuning**: Use GridSearchCV or RandomizedSearchCV
5. **Deploy Model**: Create a Flask API or Streamlit dashboard
6. **A/B Testing Framework**: Simulate retention campaign effectiveness

## 🤝 Questions?

Check the main [README.md](README.md) for comprehensive documentation.

## ⭐ Showcase Your Work

Don't forget to:
- ⭐ Star your repo
- 📝 Write a blog post about your findings
- 📱 Share on LinkedIn with #datascience #machinelearning
- 🎤 Prepare a 3-minute project walkthrough for interviews

---

Good luck with your job search! 🎯
