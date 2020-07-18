a = int(input())
input_string = input()
list1 = input_string.split()
list1 = list(map(int, list1))


for num in list1:
    if num+1 not in list1 and num+1 <= a:
        print(num+1)
        break
    elif num-1 not in list1 and num-1 > 0:
        print(num-1)
        break