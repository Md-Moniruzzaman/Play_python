import re

def print_sorted_name(emails):

    rs = []
    for i in emails:
        if  re.search('@gmail.com$', i[1]):
            rs.append(i[0])
    print('\n'.join(sorted(rs)))

if __name__ == "__main__":
    num_input = int(input().strip())
    emails = []

    for i in range(num_input):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailId = first_multiple_input[1]
        emails.append(first_multiple_input)
    print_sorted_name(emails)