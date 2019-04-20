# Mal_Score_Prediction_GUI_app

Mal_Score_Prediction_GUI_app is a GUI interactive electron app that predicts scores of your unscored anime on your MyAnimeList list with clear graphs for each features.
![alt text](https://i.imgur.com/MtefOPS.jpg)

## Program Overview
+-------------+  childprocess   +-----------------------+   html request   +-----------+
| Javascript  | --------------\ |        Python         | ---------------> | Jikan API |
| (GUI input) | --------------/ | (Run by bash command) | <--------------- |           |
+-------------+                 +-----------------------+                  +-----------+
                                           | |
                                           | |
                                          \   / 
                                           \ /
                                +-----------------------+
                                |       
                                |
                                +-----------------------+
                                
## Installation
Use git clone or direct zip download.
Extended version includes staffs that worked on anime. However, data fetching can be very time consuming.
Regular version does not have staffs as features but data fetching is significantly shorter.
Choose one depending on your preference.

### Dependencies
* Node.js
* Jikan.api (https://jikan.docs.apiary.io/)
* python3
* pandas
* xgboost
* bayes_opt (BayesianOptimization)
* sklearn
* lxml
* tkinter, time, requests (should be already installed with python)

To install those, follow this:

install Node.js (https://nodejs.org)

`xcode-select --install` (only for mac users)

install anaconda python (https://docs.continuum.io/anaconda/install/)

`pip install xgboost` or `conda install -c conda-forge xgboost`

`pip install bayesian-optimization`

## Usage

This is the application window.

![alt text]()

