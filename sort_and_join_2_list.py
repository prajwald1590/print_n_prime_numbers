# initializing lists
Input_1 = [4,3,6,5,1,2]
Input_2 = ['F','C','D','B','A']

#Displaying the inputs
print('Input-1 is - ',str(Input_1))
print('Input_2 is - ',str(Input_2))

#To sort and convert list to dictionary
Output={}
for i in sorted(Input_1):
    for j in sorted(Input_2):
        Output[i]=j
        Input_2.remove(j)
        break

#Loadind the Output into the dictionary
print("Sorted and combined both the input result is - ", Output)