import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import mplcursors

# Load the dataset
data = pd.read_csv('noStrings.csv')

# Preprocessing
# Encode 'OFFENSE' column into numerical labels
label_encoder = LabelEncoder()
data['OFFENSE_LABEL'] = label_encoder.fit_transform(data['OFFENSE'])

# Split data into features and target variables
X = data[['HOUR_FROM']]
y = data[['LONGITUDE_X', 'LATITUDE_X', 'OFFENSE_LABEL']]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Generate predictions for a range of hours
hours = np.arange(0, 2400, 100)  # Generate predictions for every 100 hours
predictions = regressor.predict(hours.reshape(-1, 1))

# Plotting the data and predictions
plt.figure(figsize=(10, 8))

# Plot past crime locations by crime type
scatter = plt.scatter(data['LONGITUDE_X'], data['LATITUDE_X'], c=data['OFFENSE_LABEL'], cmap='viridis', label='Crimes')

# Plot predicted next crime locations
plt.plot(predictions[:, 0], predictions[:, 1], color='red', marker='X', label='Predicted Next Crime')

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Locations and Predictions for All Hours')

# Enable hover functionality to display longitude, latitude, and offense name
mplcursors.cursor(hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(f"Longitude: {data.iloc[sel.target.index]['LONGITUDE_X']}\nLatitude: {data.iloc[sel.target.index]['LATITUDE_X']}\nOffense: {data.iloc[sel.target.index]['OFFENSE']}")
)

plt.legend()
plt.grid(True)
plt.show()