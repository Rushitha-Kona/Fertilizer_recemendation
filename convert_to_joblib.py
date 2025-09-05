import pickle
import joblib

files = ["rf_file.pkl", "soil.pkl", "crop.pkl", "fertilizer.pkl"]

for f in files:
    with open(f, "rb") as file:
        obj = pickle.load(file)
    joblib.dump(obj, f)
