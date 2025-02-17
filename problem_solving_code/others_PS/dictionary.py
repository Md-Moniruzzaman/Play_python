n = int(input())
phoneBook = {}

for _ in range(n):
    name, phoneNumber = input().split()

    phoneBook[name] = phoneNumber

while True:
    try: 
        query = input()
        if query in phoneBook:
            print(query + '=' + phoneBook[query])
        else:
            print('Not found')
    except EOFError:
        break


