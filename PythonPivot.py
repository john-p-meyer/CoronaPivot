import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the input data from a CSV file
#input_data = pd.read_csv("covid_confirmed_usafacts.csv")
#urllib.request.urlretrieve("https://static.usafacts.org/public/data/covid-19/covid_confirmed_usafacts.csv", "covid_confirmed_usafacts.csv")
input_data = pd.read_csv("covid_confirmed_usafacts.csv")

# Drop the StateFIPS and countyFIPS columns
input_data = input_data.drop(["StateFIPS", "countyFIPS"], axis=1)

# Melt the input data to reshape it from wide to long format
case_output_data = pd.melt(input_data, id_vars=["State", "County Name"], var_name="Date", value_name="Overall Cases")

# Group the output data by State and Date and sum the Amount column
case_output_data = case_output_data.groupby(["State", "Date"], as_index=False).sum(numeric_only=True)

#output_data.insert(loc=2, column='New Cases', value=output_data['Overall Cases'])
#output_data['New Cases'] = output_data['Overall Cases'].shift(1)
#output_data['New Cases'] = output_data['Overall Cases'].apply(lambda x: x + 1)
case_output_data['New Cases'] = case_output_data['Overall Cases'].diff()
case_output_data['Case State'] = case_output_data['State'].shift(1)
case_output_data['New Cases'] = case_output_data['State'].eq(case_output_data['Case State']).astype(int) * case_output_data['New Cases']
case_output_data = case_output_data.drop('Case State', axis=1)

input_data = pd.read_csv("covid_deaths_usafacts.csv")

# Drop the StateFIPS and countyFIPS columns
input_data = input_data.drop(["StateFIPS", "countyFIPS"], axis=1)

# Melt the input data to reshape it from wide to long format
death_output_data = pd.melt(input_data, id_vars=["State", "County Name"], var_name="Date", value_name="Overall Deaths")

# Group the output data by State and Date and sum the Amount column
death_output_data = death_output_data.groupby(["State", "Date"], as_index=False).sum(numeric_only=True)

death_output_data['New Deaths'] = death_output_data['Overall Deaths'].diff()
death_output_data['Death State'] = death_output_data['State'].shift(1)
death_output_data['New Deaths'] = death_output_data['State'].eq(death_output_data['Death State']).astype(int) * death_output_data['New Deaths']
death_output_data = death_output_data.drop('Death State', axis=1)

#duplicates = case_output_data[case_output_data[['State', 'Date']].duplicated()]

output_data = case_output_data.merge(death_output_data, on=['State', 'Date'], how='outer')

subdata = output_data.loc[output_data['State'] == 'OH']
subdata = output_data.loc[output_data['Date'] >= '2023-04-15']

#subdata.replace('nan', np.nan, inplace=True)
subdata = subdata.astype({"New Cases": np.float64})

fig, axs = plt.subplots(ncols=2, figsize=(30,5))
#sns.violinplot(x="survived", y="age", hue="sex", data=data, ax=axs[0])
sns.lineplot(x="Date", y="New Cases", data=subdata, errorbar=None, ax=axs[0])
sns.lineplot(x="Date", y="New Deaths", data=subdata, errorbar=None, ax=axs[1])
#sns.pointplot(x="parch", y="survived", hue="sex", data=data, ax=axs[2])
#sns.pointplot(x="pclass", y="survived", hue="sex", data=data, ax=axs[3])
#sns.violinplot(x="survived", y="fare", hue="sex", data=data, ax=axs[4])

# Write the output data to a new CSV file
#output_data.to_csv("output.csv", index=False)
