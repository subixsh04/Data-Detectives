# DATA DETECTIVES: Finding Our Next Crime Spot

## Authors
- Anuja Alluri
- Makaela Bennett
- Subiksha Vaidhyanathan
- Varshitha Thanam

## Overview
Crime prevention is essential for maintaining safety and security in our communities. Traditional methods of predicting crime patterns have limitations in terms of accuracy. This project explores crime data detection using two predictive models:

- Linear Regression
- Neural Networks

Both models analyze historical crime data to predict future crime locations, helping law enforcement and policymakers make data-driven decisions.

## Table of Contents

- Introduction
- Liner Regression vs Neural Networks
- Linear Regression: Crime Detection
- Neural Networks: Crime Detection
- Predictions
- Key Takeaways

### Introduction

Traditional crime prediction methods are limited in their ability to analyze complex patterns. By leveraging machine learning techniques such as Linear Regression and Neural Networks, we can improve crime forecasting accuracy and enhance public safety efforts. 
The two approaches in this study:

- Linear Regression: Simple, interpretable, and effective for linear relationships.
- Neural Networks: More powerful, capable of capturing non-linear relationships, but require higher computational resources.

### Linear Regression vs Neural Networks

| Feature             | Linear Regression                   | Neural Networks       |
|---------------------|-------------------------------------|-----------------------|
| Complexity          | Simple                              | High                  |
| Interpretability    | Easy to understand                  | Harder to interpret   |
| Performance         | Works well for linear relationships | Handles non-linear relationships   |
| Computational Cost  | Low                                 | High                  |

### Linear Regression: Crime Detection
#### Steps:
 1. Data Collection: Gather historical crime data, including burglary, theft, assault, etc.
 2. Feature Selection: Identify key features influencing crime rates (e.g., demographics, weapons, offense type, time of occurrence).
 3. Model Training: Train a linear regression model to establish relationships between selected features and crime rates.
 4. Model Evaluation: Assess accuracy and visualize crime locations alongside predictions.
 5. Prediction and Analysis: Use trained models to forecast potential crime hotspots.

#### Next Possible Crime Location
 - Longitude: -84.52472551657075
 - Latitude: 39.13818585967552

#### Predicted Crime Locations

##### Theft:
 - Crime 1: (-84.527152, 39.136186)
 - Crime 2: (-84.527347, 39.136097)
 - Crime 3: (-84.527542, 39.136008)

##### Criminal Damaging/Endangering:
 - Crime 1: (-84.515512, 39.136219)
 - Crime 2: (-84.515095, 39.136263)
 - Crime 3: (-84.514679, 39.136308)

##### Assault:
 - Crime 1: (-84.522161, 39.136583)
 - Crime 2: (-84.522178, 39.136427)
 - Crime 3: (-84.522195, 39.136272)

### Neural Networks: Crime Detection

#### Steps:
 1. Data Collection and Preparation: Use the same dataset as Linear Regression.
 2. Model Selection: Utilize multiple dense (fully connected) layers with ReLU activation functions.
 3. Training: Adjust model parameters to minimize loss and improve prediction accuracy.
 4. Evaluation: Monitor loss curves to assess performance and prevent overfitting.
 5. Deployment and Iterative Improvement: Continuously refine the model for better accuracy.

#### Neural Network Predictions

Output graphs provide insights into model performance and guide further improvements.

### Key Takeaways:
 - Linear Regression is simple and effective for basic crime pattern detection.
 - Neural Networks are more robust but require significant computational resources.
 - Predictive models help law enforcement proactively address crime-related challenges.
 - Data-driven decision-making enhances crime prevention strategies.

### Repository Details

This project includes datasets, code, and visualization tools.

Contributions are welcome!

License: MIT License
