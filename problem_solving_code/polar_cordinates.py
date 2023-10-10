import cmath
import math
a=complex(input())
print(format(math.sqrt(pow(a.real,2)+pow(a.imag,2)),'.3f'))
print(format(cmath.phase(a),'.3f'))

