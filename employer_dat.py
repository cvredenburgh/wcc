
#
# This script serves to process and clean the WCC participant data
#
# Load relevant packages
import pandas as pd
import numpy as np
print(pd._version)

# Import Baseline Participant Information
file_folder = '/Users/cvredenburgh/Downloads/';
res = 'residents_baseline_211013.csv';
emp = 'employers_baseline_211013.csv';
res = pd.read_csv(file_folder + res);
emp = pd.read_csv(file_folder + emp);

# Update column titles and data types to support analysis and cleaning
for i in []:

# Assess missing customer data to target
print(res.dtypes)
