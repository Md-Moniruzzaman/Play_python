width = int(input())
c='H'
# top cone
for i in range(width):
    print((c*i).rjust(width-1)+c+(c*i).ljust(width-1))

# top pillers
for i in range(width+1):
    print((c*width).center(width*2)+(c*width).center(width*6))

# middle part
for i in range((width+1)//2):
    print((c*width*5).center(width*6))

# lower pillers
for i in range(width+1):
    print((c*width).center(width*2)+(c*width).center(width*6))

# bottom cone
for i in range(width):
    print(((c*(width-i-1)).rjust(width)+c+(c*(width-i-1)).ljust(width)).rjust(width*6))