
#
# This script serves to process and clean the WCC participant data
#
# Load relevant packages
import pandas as pd
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
#print(pd._version)

### Import raw survey files
file_folder = '/Users/cvredenburgh/OneDrive/Documents/Projects/WCC/';
folder_postfix = '_dat/';
file_postfix = '.csv';
pull_date ='11242021';
# baseline surveys
res_base = 'resident_baseline_';
emp_base = 'employer_baseline_';
res_base = pd.read_csv(file_folder + pull_date + folder_postfix + res_base + pull_date + file_postfix);
emp_base = pd.read_csv(file_folder + pull_date + folder_postfix + emp_base + pull_date + file_postfix);
# intake surveys

# questionnaires

## ACS Income Data
acs_dat = 'ACS 2019 Income Data';
acs_dat = pd.read_csv(file_folder + acs_dat + file_postfix);
# Make the first row column headers
acs_dat.rename(columns=acs_dat.iloc[0], inplace=True)

### Update column names, types, and data structure
# Update resident columns to be more workable
res_base_sub = res_base[['Respondent ID', 'Collector ID',
    'Start Date', 'End Date',
    'IP Address', 'What is your age?',
    'Below please enter the email address you provided to register for the research study.The email address will allow us to determine which participants have completed the survey, and we can then send the $40 stipend via mail to the mailing address provided. Your responses to the survey will be anonymous and your personal information is protected. If you have any questions or concerns, please contact Amanda Sidler, WCC Coordinator - amanda@springfielddevelopment.org  802-885-3061.',
    'What is your race or ethnicity?', 'Gender: How do you identify?',
    'Which of the following best describes your current relationship status?',
    'What is the highest level of school you have completed or the highest degree you have received? ',
    'What is your current employment status?', 'Unnamed: 17',
    'Approximately how much is your current average monthly income? ',
    'How many dependents do you have? (children under the age of 18)']];
# Rename columns
res_base_sub.columns = ['respondentid', 'collectorid',
    'startdate', 'enddate',
    'ipaddress', 'age_range',
    'email', 'ethnicity',
    'gender', 'relationship_status',
    'education_level', 'employment_status',
    'employment_notes', 'mo_income_range',
    'dependent_cnt'];
# Eliminate first row, as not real data
res_base_sub = res_base_sub.iloc[1:];

# Add computed columns
res_base_sub['annual_income_range'] = res_base_sub.mo_income_range*12 # need to first transform data type here

#print(res_base_sub.head(15))
#print(res_base_sub.shape)

#print(type(res_base))
#print(res_base_sub.columns)
#print(acs_dat.dtypes)
# Update column titles and data types to support analysis and cleaning
# for i in []:

# Assess missing customer data to target
# Check for missing values
#data.isnull().sum()
print(acs_dat.head())
print(acs_dat.columns)


### Produce data plots
# Plot income distributions
# Plot the bar graph of income range distributions

res_base_sub.employment_status.value_counts(normalize=True).plot.barh()
plt.show()
