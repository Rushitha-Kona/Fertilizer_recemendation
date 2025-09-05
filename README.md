# 🌾 Fertilizer Recommendation System

A machine learning-powered web application that provides personalized fertilizer recommendations based on soil conditions, crop type, and environmental factors.

## 🚀 Features

- **Precision Agriculture**: Tailored recommendations for specific soil and crop combinations
- **Data-Driven**: Powered by machine learning algorithms trained on agricultural data
- **User-Friendly**: Simple web interface built with Streamlit
- **Instant Results**: Get recommendations in seconds
- **Multi-Crop Support**: Supports 17 different crop types
- **Multiple Soil Types**: Works with 5 different soil classifications

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Random Forest Classifier (scikit-learn)
- **Data Processing**: NumPy, Pandas
- **Deployment**: Streamlit Cloud

## 📋 Supported Crops

- Rice, Wheat, Tobacco, Sugarcane, Pulses
- Pomegranate, Paddy, Oil seeds, Millets
- Maize, Ground Nuts, Cotton, Coffee
- Watermelon, Barley, Kidney beans, Orange

## 🪨 Supported Soil Types

- Clayey, Loamy, Red, Black, Sandy

## 🚀 Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Fertilizer_recemendation.git
   cd Fertilizer_recemendation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run home.py
   ```

4. **Open in browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
Fertilizer_recemendation/
├── home.py                 # Main homepage
├── pages/
│   └── prediction.py      # Prediction interface
├── models/
│   ├── rf_file.pkl        # Trained Random Forest model
│   ├── soil.pkl           # Soil type encoder
│   ├── crop.pkl           # Crop type encoder
│   └── fertilizer.pkl     # Fertilizer label encoder
├── data/
│   └── f2.csv             # Training dataset
├── f_rec.jpg              # Background image
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── README.md
```

## 🌐 Deployment on Streamlit Cloud

1. **Push to GitHub**
   - Ensure all files are committed to your GitHub repository
   - Make sure `requirements.txt` is in the root directory

2. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set main file path: `home.py`
   - Click "Deploy"

3. **Environment Variables** (if needed)
   - None required for this application

## 🔧 Troubleshooting

### Common Issues:

1. **ModuleNotFoundError**: 
   - Ensure all `.pkl` files are in the root directory
   - Check that `requirements.txt` includes all dependencies

2. **File Path Issues**:
   - Verify that pickle files exist in the same directory as `home.py`
   - Check file permissions

3. **Model Loading Errors**:
   - Ensure pickle files are not corrupted
   - Try regenerating model files if necessary

### Debugging Steps:

1. **Check file structure**:
   ```bash
   ls -la  # Should show all .pkl files in root
   ```

2. **Test locally first**:
   ```bash
   streamlit run home.py
   ```

3. **Check Streamlit Cloud logs**:
   - Click "Manage app" in the lower right of your deployed app
   - Check the logs for detailed error messages

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Model Information

- **Algorithm**: Random Forest Classifier
- **Features**: Temperature, Humidity, Moisture, Soil Type, Crop Type, N, P, K
- **Accuracy**: Based on agricultural dataset training
- **Preprocessing**: Label encoding for categorical features

## 📝 Usage

1. **Navigate to the prediction page**
2. **Enter environmental data**:
   - Temperature (°C)
   - Humidity (%)
   - Moisture (%)

3. **Select agricultural parameters**:
   - Soil type from dropdown
   - Crop type from dropdown

4. **Input nutrient levels**:
   - Nitrogen (N)
   - Phosphorous (P)
   - Potassium (K)

5. **Get recommendation**:
   - Click "Predict Fertilizer"
   - View results and additional details

## ⚠️ Important Notes

- **Data Privacy**: No user data is stored or transmitted
- **Accuracy**: Recommendations are based on training data patterns
- **Professional Advice**: Consult agricultural experts for critical decisions
- **Local Conditions**: Consider local soil testing for best results

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review Streamlit Cloud documentation
3. Create an issue in the GitHub repository
4. Contact the development team

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Agricultural research community for datasets
- Streamlit team for the amazing framework
- Scikit-learn contributors for ML tools
- Open source community for support and resources

---

Made with ❤️ for sustainable agriculture
