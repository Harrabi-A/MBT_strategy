import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from collections import Counter
from imblearn.over_sampling import SMOTE

df = pd.read_csv("dataset-20221117.csv")

print(df)

### Imbalanced Dataet ### 
'''
X = df[["states", "actions", "uncertainty", "sparse", "tot_tests", "prior", "score"]]
y= df[["best_strategy"]]

X_train, X_test, y_train ,y_test = train_test_split(X, y, test_size=0.2)

train_set =  X_train.assign(best_strategy= y_train)
test_set = X_test.assign(best_strategy=y_test)

#Save to train and test sets to csv files
#train_set.to_csv("train_set.csv")
#test_set.to_csv("test_set.csv")'''


#[DELETE] for testing (lines of code to get all the available class)
output_val = []
for index, row in df.iterrows():
	if not( row["best_strategy"] in output_val):
		output_val.append(row["best_strategy"])

print(output_val)


#Check if the output classes are balanced in the dataset
count_output = [0, 0, 0, 0]
for index, row in df.iterrows():
	for x in range(4):
		if row["best_strategy"] == output_val[x]:
			count_output[x] += 1
			break


print(count_output)


# Under-sampling dataset
#X_resampled, y_resampled = SMOTE().fit_resample(X, y)


# Chcek if the test set is balanced 
'''count_test = [0, 0, 0, 0]
for index, row in test_set.iterrows():
	for x in range(4):
		if row["best_strategy"] == output_val[x]:
			count_test[x] += 1
			break


print(count_test)'''

#print(Counter(y))




####UNDERSAMPLING AND OVERSAMPLING####
# duple the class hist to reach 46 and reduce all the other to 46
sampled_list = []
hist_count=0
dist_count=0
flat_count=0
freq_count=0
for index, row in df.iterrows():
	if row['best_strategy']=='hist' and (hist_count != 46):
		#insert this row twice
		sampled_list.append(row)
		sampled_list.append(row)
		hist_count += 1
		hist_count += 1
	elif row['best_strategy']=='dist' and (dist_count != 46):
		#insert this rowv
		sampled_list.append(row)
		dist_count += 1
	elif row['best_strategy']=='flat' and (flat_count != 46):
		#insert thisflat
		sampled_list.append(row)
		flat_count += 1
	elif row['best_strategy']=='freq' and (freq_count != 46):
		#insert this row
		sampled_list.append(row)
		freq_count += 1

	if (hist_count==46 and dist_count==46 and flat_count==46 and freq_count==46):
		print("Dataset is balanced")
		break

sampled_df = pd.DataFrame(sampled_list)

#Check if the output classes are balanced in the dataset
count_sampled_df = [0, 0, 0, 0]
for index, row in sampled_df.iterrows():
	for x in range(4):
		if row["best_strategy"] == output_val[x]:
			count_sampled_df[x] += 1
			break

# Create a new sequential and unique indexes
sampled_df = sampled_df.reset_index(drop=True)

# encode "bal" with 1, "unbal" with 0
for index, row in sampled_df.iterrows():
	if row["prior"] == "bal":
		sampled_df.loc[index,"prior"]=1
	elif row["prior"] == "unbal":
		sampled_df.loc[index,"prior"]=0

#Testing 
print(sampled_df)
print(output_val)
print(count_sampled_df)

#export sampled data
sampled_df.to_csv("balanced_dataset")


#Split the data
X = sampled_df[["states", "actions", "uncertainty", "sparse", "tot_tests", "prior", "score"]]
y= sampled_df[["best_strategy"]]

X_train, X_test, y_train ,y_test = train_test_split(X, y, test_size=0.2, stratify=y)

train_set =  X_train.assign(best_strategy= y_train)
test_set = X_test.assign(best_strategy=y_test)

#Export the train set and test in csv files
train_set.to_csv("balanced_train_set.csv", index=False)
test_set.to_csv("balanced_test_set.csv", index=False)

