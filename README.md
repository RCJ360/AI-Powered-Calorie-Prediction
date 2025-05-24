# AI-Powered Calorie Prediction

## Overview
**Predict Calorie Expenditure** is a **Streamlit**-based application that leverages **Machine Learning** to estimate the number of calories burned during a workout. The model is trained on a deep-learning-generated dataset to provide accurate predictions based on input features.

<p align="center">
    <img src="https://github.com/RCJ360/AI-Powered-Calorie-Prediction/blob/main/calories%20burn.jpg" alt="Calories Burn Image">
</p>

## Table of Contents
- [Goal](#goal)
- [Features](#features)
- [Dataset Description](#dataset-description)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Contributions](#contributions)
- [License](#license)
- [Author](#author)

## Goal
The objective of this project is to develop a predictive model that estimates calorie expenditure based on workout attributes.

## Features
- Interactive web app built using **Streamlit**.
- Utilizes a **pre-trained deep learning model** for calorie prediction.
- Supports dataset exploration and visualization.
- Implements **scikit-learn** tools for preprocessing and modeling.
- Compatible with **joblib** for model serialization.

## Dataset Description
The dataset has been derived from a deep learning model trained on the **Calories Burnt Prediction dataset**. While the feature distributions are close to the original dataset, they are not identical. Users can incorporate the original dataset for further exploration and to improve model performance.

### Files in the repository:
- **train.csv** - Training dataset (750,000 samples, 9 features)
- **test.csv** - Test dataset (250,000 samples, 8 features)
- **app.py** - Streamlit application script
- **scaler.pkl** - Pre-trained scaler object
- **Predict Calorie Expenditure.ipynb** - Jupyter Notebook containing the model development process
- **requirements.txt** - List of dependencies for easy setup

## Technologies Used
This project is built using the following technologies (latest versions as of May 2025):
| Technology | Version |
|------------|---------|
| Python | 3.10+ |
| Numpy | 1.25.0 |
| Pandas | 2.1.0 |
| Seaborn | 0.13.0 |
| Matplotlib | 3.8.0 |
| Scipy | 1.15.3 |
| Scikit-learn | 1.4.0 |
| Joblib | 1.3.0 |
| Streamlit | 1.30.0 |

## How It Works
1. Upload input data or manually enter workout parameters.
2. The model processes the input and predicts the calories burned.
3. Visualizations help understand feature influence and trends.

## Contributions
Contributions are welcome! If you'd like to improve the model, optimize the app, or suggest new features:

1. Fork the repository
2. Create a new branch (git checkout -b feature-name)
3. Commit your changes (git commit -m "Added new feature")
4. Push to the branch (git push origin feature-name)
5. Open a Pull Request

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Created by Rupak C. Jogi
- LinkedIn - [Rupak C. Jogi](https://www.linkedin.com/in/rupak-jogi-py-aiml/)
- GitHub - [Rupak C. Jogi](https://github.com/RCJ360)



