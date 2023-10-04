if __name__ == '__main__':
    nestet_list = []
    score_list = []
    for _ in range(int(input())):
        lst = []
        name = input()
        score = float(input())
        lst.append(name)
        lst.append(score)
        nestet_list.append(lst)
        score_list.append(score)
    score_list = sorted(list(set(score_list)))
    name_list = []
    for i in nestet_list:
        if i[1] == score_list[1]:
            name_list.append(i[0])
    print('\n'.join(sorted(name_list)))
