'''
    Product of last K numbers
'''


# from collections import defaultdict

# class ProductOfNumbers:

#     def __init__(self):
#         self.product_map = defaultdict(int)
#         self.lst = []

#     def add(self, num: int) -> None:
#         if len(self.lst) == 0 or self.lst[-1] == 0:
#             self.product_map[num] = num
#             self.lst.append(num)
#         else:
           
#             self.product_map[num] = self.product_map[self.lst[-1]] * num 
#             self.lst.append(num)
         

#     def getProduct(self, k: int) -> int:
#         print(self.lst)
#         if self.product_map[self.lst[-k]] == 0:
#             return 0
#         elif self.product_map[self.lst[-(k+1)]] == 0:
#             return self.product_map[self.lst[-1]]
        
#         else:
#             return self.product_map[self.lst[-1]] // self.product_map[self.lst[-(k+1)]]
        
        
        
class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]
        self.last_zerro_index = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]
            self.last_zerro_index = len(self.prefix_product) - 1
        else:
            self.prefix_product.append(self.prefix_product[-1] * num ) 

    def getProduct(self, k: int) -> int:
        if k>=len(self.prefix_product):
            return 0
        
        if self.last_zerro_index > len(self.prefix_product) - k:
            return 0
        return self.prefix_product[-1]//self.prefix_product[-(k+1)]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
param_2 = obj.getProduct(2)
print(param_2)
param_2 = obj.getProduct(3)
print(param_2)
param_2 = obj.getProduct(4)
print(param_2)
obj.add(8)
param_2 = obj.getProduct(2)
print(param_2)