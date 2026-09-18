# ============================================================
# AI-POWERED DYNAMIC PRICING & REVENUE OPTIMIZATION ENGINE
# DEMAND PREDICTION
# ============================================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# ------------------------------------------------------------
# 1. LOAD SALES DATA
# ------------------------------------------------------------

sales = pd.read_csv("../1_DATA/sales_data.csv")

print("Sales data loaded successfully!")


# ------------------------------------------------------------
# 2. SELECT FEATURES
# ------------------------------------------------------------

features = [
    "unit_price",
    "discount_pct",
    "competitor_price",
    "promotion_flag"
]

target = "quantity_sold"


# ------------------------------------------------------------
# 3. CREATE TRAINING DATA
# ------------------------------------------------------------

X = sales[features]
y = sales[target]


# ------------------------------------------------------------
# 4. SPLIT DATA
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ------------------------------------------------------------
# 5. TRAIN DEMAND MODEL
# ------------------------------------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


# ------------------------------------------------------------
# 6. MAKE PREDICTIONS
# ------------------------------------------------------------

predictions = model.predict(X_test)


# ------------------------------------------------------------
# 7. MODEL EVALUATION
# ------------------------------------------------------------

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nDemand Prediction Results")
print("-------------------------")
print("MAE:", round(mae, 2))
print("R² Score:", round(r2, 2))


# ------------------------------------------------------------
# 8. FEATURE IMPORTANCE
# ------------------------------------------------------------

importance = pd.DataFrame({
    "feature": features,
    "importance": model.feature_importances_
})

importance = importance.sort_values(
    "importance",
    ascending=False
)

print("\nFeature Importance:")
print(importance)


# ------------------------------------------------------------
# 9. SAVE MODEL RESULTS
# ------------------------------------------------------------

importance.to_csv(
    "../1_DATA/demand_feature_importance.csv",
    index=False
)

print("\nDemand prediction completed successfully!")
