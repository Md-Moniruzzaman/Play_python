def list_operation(operation_name,data):

    if operation_name == 'insert':
        lst.insert(data[0],data[1])
    elif operation_name == 'append':
        lst.append(data[0])
    elif operation_name == "remove":
        lst.remove(data[0])
    elif operation_name == "pop":
        lst.pop()
    elif operation_name == "reverse":
        lst.reverse()
    elif operation_name == "sort":
        lst.sort(reverse=False)
    elif operation_name == "print":
        print(lst)


if __name__=="__main__":
    N = int(input())
    lst = []
    for _ in range(N):
        operation_name, *val = input().split()
        data = list(map(int, val))
        list_operation(operation_name,data)