

def average_calculate(query_name, student_marks):
    avrg = sum(student_marks[query_name])/len(student_marks[query_name])
    return avrg

if __name__== "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
   
    query_name = input()
    res = average_calculate(query_name, student_marks)
    print(format(res,".2f"))
   