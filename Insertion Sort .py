# Happy coding ,code by Md Arif uddin
# This example of Insertion sort code 
# coding time 10:41 PM ,date 7/2/2021

def Insertion_sort(num):
    for i in range(1,len(num)):
        j = i
        while num[j-1] > num[j] and j > 0:
            num[j-1], num[j] = num[j], num[j-1]
            j -= 1




num = [55,2,45,56,12,3]
Insertion_sort(num)

print(num)

# output this code : [2, 3, 12, 45, 55, 56]

# 