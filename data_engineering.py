import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

df = pd.read_csv("dataset-20221117.csv")

print(df)

X = df[["states", "actions", "uncertainty", "sparse", "tot_tests", "prior", "score"]]
y= df[["best_strategy"]]

X_train, X_test, y_train ,y_test = train_test_split(X, y, test_size=0.2)

train_set =  X_train.assign(best_strategy= y_train)
test_set = X_test.assign(best_strategy=y_test)

train_set.to_csv("train_set.csv")
test_set.to_csv("test_set.csv")

