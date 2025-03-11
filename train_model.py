#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, f1_score, recall_score
sns.set(style='white')

# Load Data
dataset = pd.read_csv(r'C:\Users\A3MAX SOFTWARE TECH\A VS CODE\CICD\code-2\iris.csv')

# Feature names (Ensure no extra spaces or parentheses)

