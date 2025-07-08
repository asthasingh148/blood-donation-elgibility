

#  Blood Donation Willingness Prediction using Machine Learning

This project aims to predict whether an individual is likely to donate blood based on historical and input data using machine learning algorithms. The goal is to support blood banks and healthcare systems in identifying potential donors proactively.



##  Objective

To build a smart system that predicts an individual’s willingness to donate blood by analyzing patterns in their previous donation history and health-related attributes using supervised learning models.



##  Key Features

- Takes user input (like age, last donation date, total donations, etc.)
- Predicts likelihood of blood donation
- Provides user-friendly prediction via web interface (Flask)
- Integrates Google Maps API to show nearby donation centers
- Visualizes donor trends using Matplotlib / Seaborn



# Tech Stack

| Tool / Library          | Purpose                                   |
|-------------------------|-------------------------------------------|
| Python (scikit-learn)   | ML model creation and evaluation          |
| Flask                   | Web app and API integration               |
| HTML5, Bootstrap        | Front-end UI design                       |
| SQLite / JSON           | User data storage                         |
| Matplotlib / Seaborn    | Data visualization                        |
| Google Maps API         | Display nearby blood donation centers     |


# How It Works

1. User provides basic details via form (age, donation frequency, etc.)
2. Backend processes input and feeds it to the trained ML model
3. Model predicts and displays the donation willingness
4. Visual indicators and Google Maps show next steps or nearby centers



# Installation & Setup

###  Prerequisites

- Python 3.7+
- Flask
- scikit-learn
- Google Maps API Key

###  Installation

git clone https://github.com/asthasingh148/blood-donation-predictor.git
cd blood-donation-predictor
pip install -r requirements.txt


###  Running the App


python app.py




## Project Structure


├── templates/               # HTML files
├── static/                  # CSS and JS
├── model/                   # Saved ML model (pkl)
├── app.py                   # Flask app
├── prediction.py            # Prediction logic
├── dataset.csv              # Training data
├── requirements.txt         # Python dependencies
└── README.md                # Project overview




##  Future Enhancements

* SMS/Email notification for nearby blood drives
* Real-time eligibility check with live health data
* Multilingual user interface
* Integration with hospital/NGO donor management systems



##  Social Impact

This project encourages voluntary blood donation and aims to assist organizations in maintaining a healthy, available blood supply — potentially saving lives through early outreach and engagement.



##  Contributors

* Astha - https://github.com/asthasingh148




