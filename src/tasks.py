import numpy as np


# Q1
def even_left_odd_right(n):
    out = ""
    # TODO not sure if range to n or n+1
    # range operator with step size of 2
    for i in range(0, n+ 1, 2):
        out += str(i) + " "
        if i == n:
            break
        out += str(i + 1) + "\n"
    print(out)


# Q2
def common_values(lst1, lst2, lst3):
    out_lst = []
    for element in lst1:
        if element in lst2 and element in lst3:
            out_lst.append(element)

    return out_lst


# Q3
def only_the_last(n1, n2):
    product = n1 * n2
    # product gets called to string and since string is an array
    # of chars we can use the [] operator to get single chars
    # and the char at location -1 is the last char in the array
    return str(product)[-1]


# Q4
def unique_digit_dict(n1, n2):
    to_do_numbers = []
    out_dict = {}
    # get min and max for range to allow for inputs where
    # n2 < n1
    # Create list of numbers from n1 to n2
    for i in range(min(n1, n2), max(n1, n2) + 1):
        to_do_numbers.append(i)

    for current_number in to_do_numbers:
        unique_digits = []
        # iterate over chars in string
        for char in str(current_number):
            # look for unique chars and save them
            if char not in unique_digits:
                unique_digits.append(char)
        out_dict[current_number] = len(unique_digits)

    return out_dict


# Q5
def divide_me (inlist, den):
    # maybe this is a bit too hacky, but I like it a lot and
    # it is really clean, just ask me and I will explain it :)
    return list(map(lambda x: x / den, inlist))


# Q6
def ndigits_times_nletters(inint, instr):
    # figure out how long the string is
    str_length = 0
    for _ in instr:
        str_length += 1

    # figure out how long the number is by dividing by 10
    # repeatedly
    int_length = 1
    current_number = inint
    while True:
        if current_number / 10 > 1:
            int_length += 1
            current_number = int(current_number / 10)
        else:
            break

    return int_length * str_length


# Q7
def grid_sum_prod(n):
    # print comments left for better understanding

    # Matrix creation
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            # Fill with values from 0 to 1
            matrix[i].append(np.random.randint(2))
    #print(matrix)

    out = []
    for col_row_index in range(n):
        row_sum = 0
        for row_element in matrix[col_row_index]:
            row_sum += row_element

        col_sum = 0
        for row in range(n):
            col_sum += matrix[row][col_row_index]

        out.append(row_sum * col_sum)
        #print("Row sum: " + str(col_row_index) + ": " + str(row_sum))
        #print("Col sum: " + str(col_row_index) + ": " + str(col_sum))

    return out
    

# Q8
def eight_bits():
    # format and zfill could have been wrapped in a lambda
    for i in range(256):
        print(str(i) + " = " + format(i, "b").zfill(8))


# Q9
def min_mac_range(*argv):
    numbers = []
    for arg in argv:
        numbers.append(arg)

    min_val = min(numbers)
    max_val = max(numbers)

    return min_val, max_val, max_val - min_val


# Q10
def add_me(n):
    summands = []
    for i in range(1, n + 1):
        summands.append(int(str(n)*i))

    sum_var = 0
    for element in summands:
        sum_var += element
    return sum_var


# Q11
def remove_lower_and_higher(inlist, low, high):
    # Filter filters the elements where the statement is false
    # true filters will remain
    #w_o_low = list(filter(lambda number: number >= low, inlist))
    #w_o_high = list(filter(lambda number: number <= high, w_o_low))
    #return w_o_high


    return list(filter(lambda number: number <= high, list(filter(lambda number: number >= low, inlist))))


# Q12
def balanced_brackets(instr):
    open_brackets = 0
    for char in instr:
        if char == "(":
            open_brackets += 1
        if char == ")" :
            open_brackets -= 1

    # return the bool directly and not a previous var
    return open_brackets == 0


# Q13
def count_me(instr):
    # TODO dont understand what is meant with capital letters
    return

def main():
    #even_left_odd_right(5)
    #print(common_values([1, 2, 3], [1, 2, 3], [3, 4, 5]))
    #print(only_the_last(10, 10))
    #print(unique_digit_dict(122, 124))
    #print(divide_me([0, 1, 2, 3, 4, 5], 2))

    #print(ndigits_times_nletters(123, "abc"))
    #print(grid_sum_prod(4))
    #eight_bits()
    #print(min_mac_range(10, 2, 99))
    #print(add_me(4))

    #print(remove_lower_and_higher([1, 3, 2, 19, 23], 3, 20))
    print(balanced_brackets("((())()))"))
    return


main()
