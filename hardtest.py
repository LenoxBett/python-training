# n = int(input("Enter number: "))
# for i in range(0,n+1):
#     print(i,end= "")
    
# if __name__ == '__main__':
#     N = int(input("Enter number: "))
#     my_list = []
#     for i in range(1,N):
#         my_list.append(i)
#     print(my_list)


if __name__ == '__main__':
    N = int(input("Enter number: "))
    my_list = []
    for i in range(1,N):
        num = input().split()
        if num[0] == "insert":
            my_list.insert(int(num[1]),int(num[2]))
        elif num[0] == "print":
            print(my_list)
        elif num[0] == "remove":
            my_list.remove(int(num[1]))
        elif num[0] == "append":
            my_list.append(int(num[1]))   
        elif num[0] == "sort":
            my_list.sort()
        elif num[0] == "pop":
            my_list.pop()
        elif num[0] == "reverse":
            my_list.reverse()      
                      
print(my_list)        
