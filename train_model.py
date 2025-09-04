import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

# Load dataset
data = pd.read_csv("f2.csv")

# Separate features & target
X = data.drop('Fertilizer', axis=1)
y = data['Fertilizer']

# Encode categorical variables
soil_enc = LabelEncoder()
crop_enc = LabelEncoder()
ferti_enc = LabelEncoder()

X['Soil_Type'] = soil_enc.fit_transform(X['Soil_Type'])
X['Crop_Type'] = crop_enc.fit_transform(X['Crop_Type'])
y_encoded = ferti_enc.fit_transform(y)

# Handle imbalance using SMOTE
# Before using SMOTE, check the minimum class count
min_class_count = y.value_counts().min()
# Set k_neighbors to min_class_count - 1 (must be >=1)
k_neighbors = max(1, min_class_count - 1)

smote = SMOTE(random_state=42, k_neighbors=k_neighbors)
X_res, y_res = smote.fit_resample(X, y_encoded)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.2, random_state=42
)

# Train RandomForest
model = RandomForestClassifier(n_estimators=200, max_depth=7, random_state=42, class_weight="balanced")
model.fit(X_train, y_train)

# Save model & encoders
pickle.dump(model, open("rf_file.pkl", "wb"))
pickle.dump(soil_enc, open("soil.pkl", "wb"))
pickle.dump(crop_enc, open("crop.pkl", "wb"))
pickle.dump(ferti_enc, open("fertilizer.pkl", "wb"))

# Print class balance after SMOTE
print("Class balance after SMOTE:")
unique, counts = np.unique(y_res, return_counts=True)
for u, c in zip(unique, counts):
    print(f"{ferti_enc.classes_[u]}: {c} samples")
