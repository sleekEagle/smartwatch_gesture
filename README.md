# smartwatch_gesture
This repository contains code for training gesture recognition models using the database from https://tev.fbk.eu/technologies/smartwatch-gestures-dataset
This also uses GANs to create synthetic data to improve performance. 

## dataprep.ipynb
    data preparation and database exbloration
## gesture_conditional-linear.ipynb
    creates conditional GAN to generate sysnthetic data that would simulate data from the database
   
## CNN.ipynb
    Builds classification models using Pytorch to classify gestures

## CNN_eval_mydata.ipynb
    CLassifies data that I created with the models trained in the CNN.ipynb
    
## user_dataprep.py
    extracts data from smartwatch data file created from wada (https://github.com/abumondol/WaDa)
    
