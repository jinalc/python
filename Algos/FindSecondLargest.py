# 4. WAF: second_maximum() Create a new version of above code to return the second largest
# number.

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []


def second_maximum(data_list):
    while data_list:
        maximum = data_list[0]
        for x in data_list:
            if x > maximum:
                maximum = x
        new_list.append(maximum)
        data_list.remove(maximum)
    print(new_list)
    print('Second maximum is {}'.format(new_list[1]))

second_maximum(data_list)
