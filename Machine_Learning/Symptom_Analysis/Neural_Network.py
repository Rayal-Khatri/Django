import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
import joblib
import numpy as np
import warnings
from sklearn.metrics import accuracy_score


def train_model():
    dataset_path = 'C:\\Users\\user\\Desktop\\Repositories\\Django\\Machine_Learning\\Symptoms_dataset.csv'
    df = pd.read_csv(dataset_path)
    X = df.iloc[:, 1:]  # Symptoms columns
    y = df['Disease']
    
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    # Shuffle the dataset
    shuffled_X, shuffled_y = shuffle(X, y, random_state=42)
    
    # Split the shuffled data into training and testing sets
    train_X, test_X, train_y, test_y = train_test_split(
        shuffled_X, shuffled_y, test_size=0.2, random_state=42
    )
    
    warnings.filterwarnings("ignore", category=UserWarning, message="X does not have valid feature names, but MLPClassifier was fitted with feature names")

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model to a file
    model_filename = 'disease_prediction_model.joblib'
    joblib.dump(model, model_filename)


def predict_top_3_diseases(user_symptoms):
    model_filename = 'disease_prediction_model.joblib'
    loaded_model = joblib.load(model_filename)
    
    dataset_path = 'C:\\Users\\user\\Desktop\\Repositories\\Django\\Machine_Learning\\Symptoms_dataset.csv'
    df = pd.read_csv(dataset_path)
    X = df.iloc[:, 1:]  # Symptoms columns
    
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(df['Disease'])
    
    num_features = len(X.columns)
    input_data = np.zeros(num_features)  # Initialize an array of 0s
    
    for symptom in user_symptoms:
        if symptom in X.columns:
            symptom_index = X.columns.get_loc(symptom)
            input_data[symptom_index] = 1
    
    input_data = input_data.reshape(1, -1)  # Reshape the input data
    
    predicted_probabilities = loaded_model.predict_proba(input_data)
    
    # Get the indices of the top 3 predicted diseases
    top_3_indices = predicted_probabilities.argsort()[0][-3:][::-1]
    
    # Reverse the encoding to obtain disease names
    top_3_disease_names = label_encoder.inverse_transform(top_3_indices)
    
    # Get the top 3 probabilities
    top_3_probabilities = predicted_probabilities[0][top_3_indices]
    
    top_3_predictions = []
    
    for disease, probability in zip(top_3_disease_names, top_3_probabilities):
        top_3_predictions.append({
            'Disease': disease,
            'Probability': probability
        })
    
    return top_3_predictions


# Train the model and save it
# train_model()

# Test Symptoms
# user_symptoms = ["Circular Red Patches", "Bleeding/Bruises,Irritated", "Itchy", "Odor from Skin", "Skin Infection", "Greasy Skin"]
# predictions = predict_top_3_diseases(user_symptoms)


# print(predictions)
