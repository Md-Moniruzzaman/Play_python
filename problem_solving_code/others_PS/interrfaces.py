
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        lst = []
        sum2  = 0

        if n == 1:
            return 1

        for ln in range((n//2)+1):
           
            if ln == 0:
                pass
            elif (n%ln == 0):
                print(ln)
                lst.append(ln)
                lst.append(n//ln)
        lst2 =  list(set(lst))
        for i in lst2:
            sum2+=i

        
        
        return sum2


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)