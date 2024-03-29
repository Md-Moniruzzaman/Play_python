#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def extra_available(all_neo, max_neo_count):
    for count in all_neo.values():
        if count>max_neo_count:
           
            return True
    return False

def steadyGene(gene):
    # Write your code here
    gene_lenth = len(gene)
    max_neocl_count = gene_lenth/4
    all_neoc = {
        "A":0,
        "C":0,
        "G":0,
        "T":0
    }

    for neo in gene:
        all_neoc[neo]+=1

    print(all_neoc)
    if not extra_available(all_neoc, max_neocl_count):
        return 0

    min_sub_count = float("inf")
    left_itt = 0
    right_itt = 0
    while right_itt<gene_lenth:
        while right_itt<gene_lenth and extra_available(all_neoc, max_neocl_count):
            s_gene = gene[right_itt]
            all_neoc[s_gene]-=1
            right_itt+=1

        while left_itt<gene_lenth and not extra_available(all_neoc, max_neocl_count):
            s_gene = gene[left_itt]
            all_neoc[s_gene]+=1
            left_itt+=1
        min_sub_count = min(min_sub_count, right_itt-left_itt+1)
    
    return min_sub_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    gene = 'GAAATAAA'
    # gene = input()

    result = steadyGene(gene)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
