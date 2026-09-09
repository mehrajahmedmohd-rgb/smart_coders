'''👉 [2, [5, 8], 3, [1, 4]]

Steps:
Second sublist ke first element me 2 add karo
Last sublist ke second element ko first sublist ke second element se multiply karo
First element ko last sublist ke first element se replace karo'''


data=[2, [5, 8], 3, [1, 4]]
#Second sublist ke first element me 2 add karo
data[1][0] += 2
#Last sublist ke second element ko first sublist ke second element se multiply karo
data[3][1] =  data[3][1] * data[1][1]
#First element ko last sublist ke first element se replace karo
data[0] = data[3][0]
print(data)

