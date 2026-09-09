''' 👉 [4, 9, 1, 6]

🧠 Task:
Second element ko first + last ka sum bana do
List me last element remove karo
New element add karo: (first element × second element)

👉 Final list kya banegi?'''


my_list=[4, 9, 1, 6]

my_list[2]= my_list[0] + my_list[3]
my_list.pop()
my_list.append(my_list[1] * my_list[2])
print(my_list)