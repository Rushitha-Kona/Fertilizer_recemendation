import pickle

# Load once
model = pickle.load(open("rf_file.pkl", "rb"))
soil_enc = pickle.load(open("soil.pkl", "rb"))
crop_enc = pickle.load(open("crop.pkl", "rb"))
ferti_enc = pickle.load(open("fertilizer.pkl", "rb"))

def recommend_fertilizer(n, p, k, soil, crop, temp, humidity, moisture):
    try:
        soil_encoded = soil_enc.transform([soil])[0]
        crop_encoded = crop_enc.transform([crop])[0]
        features = [[n, p, k, soil_encoded, crop_encoded, temp, humidity, moisture]]
        label = model.predict(features)[0]
        return ferti_enc.classes_[label]
    except Exception as e:
        return f"❌ Error: {e}"

# Example usage
if __name__ == "__main__":
    print(recommend_fertilizer(34, 67, 62, "Loamy", "Wheat", 30, 22, 26))
