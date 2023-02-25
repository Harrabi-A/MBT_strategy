import pandas as pd

def getScore():
	pass


dataset = []

#Numebr of data for each different type of class
N = 200

classes = ["hist","flat","freq","dist"]
count_target = [0, 0, 0, 0]

features = ["states","actions","uncertainty","sparse","tot_tests","prior","best_strategy","score"]

#Read log files 
log_files = ["out-all-20220708.log","out-all-20220728.log","out-all-20220818.log","out-all-20220725.log","out-all-20220811.log","out-all-20220829.log"]
for f in log_files:
	with open(f) as f:
		lines = f.readlines()
		#read all the lines
		for line in lines:
			tmp_unit = []
			print(line)
			line_list = line.split()
			print(line_list)
			print("line elements: ", len(line_list))
			states= line_list[0]
			tmp_unit.append(states)
			actions= line_list[1]
			tmp_unit.append(actions)
			uncertainty = line_list[2]
			tmp_unit.append(uncertainty)
			sparse= line_list[3]
			tmp_unit.append(sparse)
			tot_tests= line_list[4]
			tmp_unit.append(tot_tests)
			prior= line_list[5]
			tmp_unit.append(prior)
			best_strategy= line_list[6]
			tmp_unit.append(best_strategy)
			#compute the score
			tmp_sum = 0
			tmp_n=0
			for i in range(8, len(line_list), 2):
				tmp_sum += float(line_list[i])
				tmp_n +=1
			score = tmp_sum/tmp_n
			tmp_unit.append(score)			
			print("score: ", score)

			#add the unit into dataset
			dataset.append(tmp_unit)
			#increment class number
			for x in range(4):
				if best_strategy == classes[x]:
					count_target[x] +=1
					break




print("\n\n\nDatset size: ", len(dataset))
print(classes)
print(count_target)

df = pd.DataFrame(dataset)
df.columns = features
print(df)
print(df.describe())

df.to_csv("full_dataset.csv")

