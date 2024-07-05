# Car Price Predictor

Welcome to the Car Price Predictor repository! This project is a machine learning regression model designed to predict the selling price of a car based on various input features provided by the user.

## Project Overview

The Car Price Predictor uses a regression model to estimate the selling price of a car. The model takes into account several factors that typically influence the price of a car, such as the year of manufacture, the number of kilometers driven, the type of fuel used, the type of seller, the transmission type, the ownership history, and the car brand.

## Features

- **Year**: The year of manufacture, ranging from 1992 to 2020.
- **Kilometers Driven**: The total kilometers the car has been driven, ranging from 1 to 223,159 km.
- **Fuel Type**: The type of fuel used by the car. Possible values include petrol, diesel, CNG, LPG, and electric.
- **Seller Type**: The type of seller. Possible values include Individual, Dealer, and Trustmark Dealer.
- **Transmission Type**: The type of transmission (e.g., manual or automatic).
- **Owner**: The ownership history of the car. Possible values include 1st, 2nd, 3rd, 4th & above owner, and test drive car.
- **Brand**: Various car brands.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Harshkumar6200/CarPricePredictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CarPricePredictor
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Car Price Predictor, you need to provide the required inputs as specified. You can run the model and get predictions by executing the following command:
```bash
python predict.py
```

You will be prompted to enter the details of the car, and the model will output the predicted selling price.

## Contributing

We welcome contributions to improve the Car Price Predictor. If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## Acknowledgements

We would like to thank all the contributors and the open-source community for their valuable support.

