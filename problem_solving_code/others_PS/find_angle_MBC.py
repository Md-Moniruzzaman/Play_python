
import math

def angle(bc,ab):
    ang = math.degrees(math.atan(ab/bc))
    return ang

if __name__ == "__main__":
    ab = float(input())
    bc = float(input())
    result = angle(bc,ab)
    print(round(result),chr(176),sep='')
