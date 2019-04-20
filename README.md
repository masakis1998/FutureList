# Mal_Score_Prediction_GUI_app

Mal_Score_Prediction_GUI_app is a GUI interactive electron app that predicts anime scores using machine learning model and displays clean graphs of features.
![alt text](https://i.imgur.com/MtefOPS.jpg)

## Program Overview
```text
+-------------+  childprocess   +-----------------------+   html request   +-----------+
| Javascript  | --------------> |        Python         | ---------------> | Jikan API |
|             |                 |   (Machine Learning)  | <--------------- |           |
+-------------+                 +-----------------------+                  +-----------+
       ^                                    | Program Output
       | User Input                         V
+-------------+                 +-----------------------+
|    HTML     |      Ajax       |       CSV, JSON       |
|             | <-------------- |    (Output files)     |
+-------------+                 +-----------------------+
                                
```
## Dependencies
* Node.js
* child_process
* electron
* jQuery, jQueryUI
* Jikan.api (https://jikan.docs.apiary.io/)
* python3
* pandas
* xgboost
* bayes_opt (BayesianOptimization)
* sklearn
* lxml
* tkinter, time, requests

## Installation
Use git clone or direct zip download.
Extended version includes staffs that worked on anime. However, data fetching can be very time consuming.
Regular version does not have staffs as features but data fetching is significantly shorter.
Choose one depending on your preference.

Followings are required packages:

install Node.js: (https://nodejs.org)

install anaconda python: (https://docs.continuum.io/anaconda/install/)

install xgboost: `pip install xgboost`

install bayesian-optimization: `pip install bayesian-optimization`

## Usage
Open Terminal and set working directory to either Prediction_GUI_app_regular or Prediction_GUI_app_extended, whichever you prefer.
Then Run `npm run start`.
You should see following window.
![alt text](https://i.imgur.com/rKgSwxf.jpg)

Type in your MyAnimeList username and number of rounds for score prediction.

