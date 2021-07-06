# 1. WAF: reverse_list() that takes a list as argument and reverses the elements of the list in
# place (use indexing operations, not any function or slicing)
# Logic: if l = [1,2,3,4,5] ; result = [5,4,3,2,1]
# 1 2 3 4 5 # string
# 0 1 2 3 4 # indexes
# start index = 0, end index = 4; swap the elements at index 0,4
# [5,2,3,4,1]
# start index = 1, end index = 3; swap the elements at index 1,3
# [5,4,3,2,1]
# Index start index 2 is not less than end index 2. Hence no need to go forward

def reverse_list(list):
    for i in range(int((len(list) - 1) / 2)):
        temp = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = temp
    print(list)


l = [1, 2, 3, 4, 5]
reverse_list(l)
