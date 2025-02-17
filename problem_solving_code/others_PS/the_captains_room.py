# a = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6,30, 4, 3, 1, 5, 6, 2 ]
# print(set(a))
k = int(input().strip())
rooms = list(map(int, input().strip().split()))
actual_rooms = list(set(rooms))*k
difference = sum(actual_rooms) - sum(rooms)
captain_room = difference// (k-1)
print(captain_room)
