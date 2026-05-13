# E-Commerce Customer Analytics & Churn Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive data analysis project that explores customer behavior patterns, identifies churn risk factors, and builds predictive models to support data-driven retention strategies in e-commerce.

##Project Overview

This project analyzes a dataset of 5,000 e-commerce customers to:
- Identify key characteristics differentiating churned from active customers
- Segment customers using RFM (Recency, Frequency, Monetary) analysis
- Build machine learning models to predict customer churn
- Generate actionable insights for retention strategies

### Key Results
- **Churn Rate**: 18.7% overall
- **Model Performance**: ROC-AUC Score of 0.85+
- **High-Risk Customers Identified**: 300+ active customers with >70% churn probability
- **Potential Revenue at Risk**: $237,000+ from high-value at-risk customers

##  Business Value

This analysis enables:
1. **Proactive Retention**: Identify at-risk customers before they churn
2. **Targeted Marketing**: Personalized campaigns based on customer segments
3. **Resource Optimization**: Focus retention efforts on high-value customers
4. **Revenue Protection**: Prevent churn-related revenue loss

## Project Structure

```
ecommerce-customer-analytics/
│
├── data/
│   ├── customer_data.csv              # Main dataset (5,000 customers)
│   └── high_risk_customers.csv        # Identified at-risk customers
│
├── notebooks/
│   └── customer_analytics.ipynb       # Main analysis notebook
│
├── src/
│   ├── generate_data.py               # Data generation script
│   └── churn_model.py                 # Standalone model training script
│
├── visualizations/                     # Generated plots and charts
│   ├── churn_distribution.png
│   ├── demographics_churn.png
│   ├── behavioral_analysis.png
│   ├── correlation_matrix.png
│   ├── customer_segments.png
│   ├── model_performance.png
│   └── feature_importance.png
│
├── docs/
│   └── analysis_summary.pdf           # Executive summary (optional)
│
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
└── .gitignore                         # Git ignore file
```

## Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-Learn**: Machine learning models
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive analysis environment

## Getting Started

### Prerequisites

```bash
Python 3.8 or higher
pip (Python package manager)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ecommerce-customer-analytics.git
cd ecommerce-customer-analytics
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Generate data (if needed)**
```bash
python src/generate_data.py
```

5. **Run the analysis**
```bash
jupyter notebook notebooks/customer_analytics.ipynb
```

## Key Features & Analysis

### 1. Exploratory Data Analysis (EDA)
- Customer demographic distribution
- Purchase behavior patterns
- Engagement metrics analysis
- Correlation analysis between features

### 2. Customer Segmentation
- RFM (Recency, Frequency, Monetary) segmentation
- 5 distinct customer segments identified:
  - **Champions**: High value, recent buyers
  - **Loyal Customers**: Frequent purchasers
  - **Potential Loyalists**: Recent customers showing promise
  - **At Risk**: Declining engagement
  - **Lost**: Inactive customers with high churn probability

### 3. Churn Prediction Model
- **Algorithm**: Random Forest Classifier
- **Features**: 12 behavioral and demographic variables
- **Performance Metrics**:
  - Precision: 0.82
  - Recall: 0.78
  - F1-Score: 0.80
  - ROC-AUC: 0.85+

### 4. Feature Importance
Top predictors of churn:
1. Days since last purchase (highest importance)
2. Satisfaction score
3. Email open rate
4. Website visits per month
5. Total purchases

##  Key Insights

### Churn Drivers
- **Inactivity**: Customers inactive for 90+ days show 60%+ churn rate
- **Low Satisfaction**: Customers with satisfaction scores <3.0 are 3x more likely to churn
- **Reduced Engagement**: Declining email open rates and website visits precede churn
- **Mobile App**: Non-app users churn at 25% higher rates

### High-Value Opportunities
- Champions segment represents 15% of customers but 40% of revenue
- Newsletter subscribers have 40% lower churn rates
- Customers with 5+ purchases rarely churn (2% churn rate)

##  Recommendations

### Immediate Actions
1. **Win-Back Campaign**: Target 300+ high-risk, high-value customers
2. **Re-Engagement**: Automated emails for 60+ days inactivity
3. **Mobile Push**: Incentivize app adoption with exclusive offers

### Long-Term Strategies
1. **Loyalty Program**: Reward frequent purchasers
2. **Predictive Scoring**: Weekly churn probability updates
3. **Customer Success**: Proactive support for low-satisfaction scores
4. **A/B Testing**: Test retention offers at different risk levels

## 📊 Sample Visualizations

The project generates comprehensive visualizations including:
- Churn distribution analysis
- Demographic breakdowns
- Behavioral pattern comparisons
- Feature correlation heatmaps
- Customer segment analysis
- Model performance metrics
- Feature importance rankings

##  Contributing

This is a portfolio project, but suggestions and feedback are welcome!

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Author

- Kehinde Osunniran
- LinkedIn: https://www.linkedin.com/in/kehinde-osunniran-56817b1b0
- GitHub: https://github.com/Kehinde291c
- Email: Kehinde.osunniran16@gmail.com

## Acknowledgments

- Dataset generated using realistic e-commerce patterns
- Inspired by industry best practices in customer analytics
- Built as part of a data analytics portfolio project



---

**Note**: This is a portfolio project using synthetic data. The patterns and insights are based on realistic e-commerce scenarios but should not be used for actual business decisions without validation on real data.
