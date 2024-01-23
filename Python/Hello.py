# def validator():
#     a = int(input("Enter the age: "))
#     if(a<18):
#         print("You are not eligible to vote")
#     else:
#         print("you are eligible to vote")

# validator()

import array


def array_sort(arr):
 arr_list = arr.tolist()
 arr_list.sort()

 sorted_arr = array.array(arr.typecode, arr_list)

 return sorted_arr

n = int(input("Enter the number of element to be sorted: "))

x = float(input("Enter the 0 element: "))

arr = array.array('f', [x])

for i in range(1, n):
 str1 = "Enter the " + str(i) + "th element: "

 x = float(input(str1))
 arr.append(x)

 sorted_arr = array_sort(arr)

 for element in sorted_arr:
  print(element, end=" ")