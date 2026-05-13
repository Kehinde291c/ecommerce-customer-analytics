"""
Churn Prediction Model Training Script

This script trains a Random Forest model to predict customer churn
and saves the trained model for future use.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import pickle
import warnings
warnings.filterwarnings('ignore')


def load_and_prepare_data(filepath):
    """Load and prepare data for modeling."""
    print("Loading data...")
    df = pd.read_csv(filepath)
    
    # Select features
    feature_columns = [
        'age', 'account_age_days', 'total_purchases', 'avg_order_value',
        'days_since_last_purchase', 'email_open_rate', 'website_visits_per_month',
        'satisfaction_score', 'support_tickets', 'discount_usage_rate',
        'uses_mobile_app', 'newsletter_subscribed'
    ]
    
    X = df[feature_columns]
    y = df['is_churned']
    
    print(f"Dataset shape: {X.shape}")
    print(f"Churn rate: {y.mean()*100:.2f}%")
    
    return X, y, feature_columns


def train_model(X, y):
    """Train the churn prediction model."""
    print("\nSplitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    print("Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    print("Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=20,
        min_samples_leaf=10,
        random_state=42,
        class_weight='balanced',
        n_jobs=-1
    )
    
    model.fit(X_train_scaled, y_train)
    
    # Cross-validation
    print("\nPerforming cross-validation...")
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, 
                                scoring='roc_auc', n_jobs=-1)
    print(f"Cross-validation ROC-AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")
    
    # Evaluate on test set
    print("\nEvaluating on test set...")
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Active', 'Churned']))
    
    print(f"\nROC-AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    return model, scaler, X_test, y_test


def display_feature_importance(model, feature_columns):
    """Display feature importance rankings."""
    feature_importance = pd.DataFrame({
        'feature': feature_columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print("=" * 50)
    for idx, row in feature_importance.iterrows():
        print(f"{row['feature']:30s}: {row['importance']:.4f}")
    
    return feature_importance


def save_model(model, scaler, feature_columns, model_path='../data/churn_model.pkl'):
    """Save the trained model and preprocessing objects."""
    model_package = {
        'model': model,
        'scaler': scaler,
        'feature_columns': feature_columns
    }
    
    with open(model_path, 'wb') as f:
        pickle.dump(model_package, f)
    
    print(f"\nModel saved to {model_path}")


def predict_churn(model, scaler, feature_columns, customer_data):
    """
    Predict churn probability for new customers.
    
    Parameters:
    -----------
    model : trained model
    scaler : fitted StandardScaler
    feature_columns : list of feature names
    customer_data : dict or DataFrame with customer features
    
    Returns:
    --------
    churn_probability : float between 0 and 1
    """
    if isinstance(customer_data, dict):
        customer_df = pd.DataFrame([customer_data])
    else:
        customer_df = customer_data
    
    X = customer_df[feature_columns]
    X_scaled = scaler.transform(X)
    churn_prob = model.predict_proba(X_scaled)[:, 1]
    
    return churn_prob


def main():
    """Main execution function."""
    print("="*60)
    print("CUSTOMER CHURN PREDICTION MODEL TRAINING")
    print("="*60)
    
    # Load data
    X, y, feature_columns = load_and_prepare_data('../data/customer_data.csv')
    
    # Train model
    model, scaler, X_test, y_test = train_model(X, y)
    
    # Display feature importance
    display_feature_importance(model, feature_columns)
    
    # Save model
    save_model(model, scaler, feature_columns)
    
    print("\n" + "="*60)
    print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
    print("="*60)
    
    # Example prediction
    print("\n\nExample: Predicting churn for a sample customer...")
    sample_customer = {
        'age': 35,
        'account_age_days': 365,
        'total_purchases': 5,
        'avg_order_value': 75.0,
        'days_since_last_purchase': 120,  # High risk - inactive for 4 months
        'email_open_rate': 0.15,  # Low engagement
        'website_visits_per_month': 2,  # Low activity
        'satisfaction_score': 2.5,  # Low satisfaction
        'support_tickets': 3,
        'discount_usage_rate': 0.8,
        'uses_mobile_app': 0,
        'newsletter_subscribed': 0
    }
    
    churn_prob = predict_churn(model, scaler, feature_columns, sample_customer)
    print(f"Churn Probability: {churn_prob[0]*100:.1f}%")
    
    if churn_prob[0] > 0.7:
        print("⚠️  HIGH RISK - Immediate intervention recommended")
    elif churn_prob[0] > 0.5:
        print("⚠️  MEDIUM RISK - Monitor and engage")
    else:
        print("✓ LOW RISK - Customer appears stable")


if __name__ == "__main__":
    main()
