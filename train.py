"""
   ___                  _                
  / _/______ ____  ____(_)__ _______     
 / _/ __/ _ `/ _ \/ __/ (_-</ __/ _ \    
/_//_/  \_,_/_//_/\__/_/___/\__/\___/    
  ___ _____(_)__ ___ ____  / /_(_)       
 / _ `/ __/ (_-</ _ `/ _ \/ __/ /        
 \_, /_/ /_/___/\_,_/_//_/\__/_/         
/___/

franciscogrisanti@gmail.com

"""

# USAGE
# python train.py --model model_name --data dataset_path --output output_path

print("[INFO] loading libraries...")

#import the necessary packages
import logging
import argparse
import matplotlib.pyplot as plt
import numpy as np
import random
import os
import sys
import pandas as pd
import warnings

# local functions
from Project_Name.models import Model_1
import Project_Name.utils as utils

#Reproducibility
seed = 10
np.random.seed(seed)

################construct the argument parser and parse the arguments###################
ap = argparse.ArgumentParser()

ap.add_argument(
    "-m",
    "--model",
    type=str,
    default="XXX",
    choices=["XXX", "XXX"],
    help="type of model architecture",
)

ap.add_argument(
    "-dt",
    "--data_train",
    type=str,
    required=True,
    help="Path of training dataset"
)

ap.add_argument(
    "-dp",
    "--data_predict",
    type=str,
    required=True,
    help="Path of prediction dataset"
)

ap.add_argument(
    "-o",
    "--output",
    type=str,
    required=True,
    help="Path of outputs"
)

args = vars(ap.parse_args())


################LOAD DATA###################

print("[INFO] loading training data...")

print("[INFO] loading predict data...")

################ SAVE PREDICTIONS ###################

if not os.path.exists(args["output"]):
        os.makedirs(args["output"])

predictions.to_csv(str(args["output"])+str(args["project"])+"_predictions.csv")

################ SAVE MODEL ###################

print("[INFO] saving .h5 model ...")
model.save(str(args["output"])+str(args["project"])+"_model.h5")
    