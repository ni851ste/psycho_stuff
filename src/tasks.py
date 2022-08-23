import numpy as np
import random as rand


# Q1
def even_left_odd_right(n):
    out = ""
    # TODO not sure if range to n or n+1
    # range operator with step size of 2
    for i in range(0, n + 1, 2):
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
def divide_me(inlist, den):
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
    # print(matrix)

    out = []
    for col_row_index in range(n):
        row_sum = 0
        for row_element in matrix[col_row_index]:
            row_sum += row_element

        col_sum = 0
        for row in range(n):
            col_sum += matrix[row][col_row_index]

        out.append(row_sum * col_sum)
        # print("Row sum: " + str(col_row_index) + ": " + str(row_sum))
        # print("Col sum: " + str(col_row_index) + ": " + str(col_sum))

    return out


# Q8
def eight_bits():
    # format and zfill could have been wrapped in a lambda
    for i in range(256):
        print(str(i) + " = " + format(i, "b").zfill(8))


# Q9
def min_mac_range(*argv):
    min_val = argv[0]
    max_val = argv[0]

    # Don't skip first element in for loop for clean and simple code
    # performance doesn't matter here
    for arg in argv:
        if arg < min_val:
            min_val = arg
        if arg > max_val:
            max_val = arg

    return min_val, max_val, max_val - min_val


# Q10
def add_me(n):
    summands = []
    for i in range(1, n + 1):
        summands.append(int(str(n) * i))

    sum_var = 0
    for element in summands:
        sum_var += element
    return sum_var


# Q11
def remove_lower_and_higher(inlist, low, high):
    # Filter filters the elements where the statement is false
    # true filters will remain
    # w_o_low = list(filter(lambda number: number >= low, inlist))
    # w_o_high = list(filter(lambda number: number <= high, w_o_low))
    # return w_o_high

    return list(filter(lambda number: number <= high, list(filter(lambda number: number >= low, inlist))))


# Q12
def balanced_brackets(instr):
    open_brackets = 0
    for char in instr:
        if char == "(":
            open_brackets += 1
        if char == ")":
            open_brackets -= 1

    # return the bool directly and not a previous var
    return open_brackets == 0


# Q13
def count_me(instr):
    # TODO dont understand what is meant with capital letters
    # Capital letters will be ignored
    char_dict = {}
    for char in instr:
        if char.isupper():
            continue

        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] = char_dict[char] + 1

    for key in char_dict:
        print("Letter: " + key + ", Count: " + str(char_dict[key]))


# Q14
def sum_odd_sum_even(inlist):
    sum_even = 0
    sum_odd = 0
    for element in inlist:
        if element % 2 == 0:
            sum_even += element
        else:
            sum_odd += element
    # return odd then even
    return sum_odd, sum_even


# Q15
def mean_rt_er(rts, errors):
    mean_rt = sum(rts) / len(rts)
    error_rate = (sum(errors) / len(errors)) * 100

    print("Mean RT: {:.0f} ms".format(mean_rt))
    print("Mean ER: {:.1f} %".format(error_rate))


# Q16
def firstname_lastname():
    # TODO Das Beispiel mit Angela Merkel is einfach falsch lol
    first_name_vowel_count = 0
    last_name_vowel_count = 0

    vowels = ['a', 'e', 'i', 'o', 'u']

    in_text = input("Please insert your full name!\n")

    # Input validation
    # check for 2 words, separated by a whitespace
    if len(in_text.split(" ")) != 2:
        print("Input error!")
        exit(-1)

    # check for non alphanumeric chars, "-" and " " are permitted
    for char in in_text:
        if not char.isalnum():
            if char == ' ' or char == '-':
                continue
            print("Input error!")
            exit(-1)

    split_in_text = in_text.split(" ")

    # First name counting
    for char in split_in_text[0]:
        if char.lower() in vowels:
            first_name_vowel_count += 1

    # Last name counting
    for char in split_in_text[1]:
        if char.lower() in vowels:
            last_name_vowel_count += 1

    # More vowels in first name
    if first_name_vowel_count > last_name_vowel_count:
        return "first"
    # More in last name
    elif first_name_vowel_count < last_name_vowel_count:
        return "second"
    # Equal
    else:
        return "equal"


# Q17
def basic_analysis():
    # allowed imports: pandas, matplotlib
    # TODO datafile is missing
    return


# Q18
def shuffle_me(inlist):
    # Not 2 time same string directly after each other
    target_length = len(inlist) * 20
    target_list = []
    index_before = -1

    while True:
        # Break condition
        if len(target_list) == target_length:
            break

        # randint upper border is inclusive, -1 to fix for that
        i = rand.randint(0, len(inlist) - 1)
        if i == index_before:
            continue

        target_list.append(inlist[i])
        index_before = i

    return target_list


# Q19
def repeated_letter(instr):
    prev_char = ""
    for char in instr:
        # check if char is letter
        if not char.isalpha():
            prev_char = ""
            continue
        if char == prev_char:
            return True
        prev_char = char
    return False


# Q20
def first_index(inlst):
    out_dict = {}
    for i in range(len(inlst)):
        if inlst[i] not in out_dict:
            out_dict[inlst[i]] = i
    return out_dict


# Q21
def permutation_subset(n1, n2):
    out_lst = []
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if (i + j) % 2 == 0:
                out_lst.append([i, j])
    return out_lst


# Q22
def letter_order(instr, l1, l2):
    # 3rd example does not make sense, because the second 'A' comes after
    # a 'B'
    # So apparently the rules stated reset for each word

    second_letter_appeared = False
    for letter in instr:
        if letter == l2 and not second_letter_appeared:
            second_letter_appeared = True
            continue

        if letter == l1 and second_letter_appeared:
            return False

        # special case space character resets the search
        if letter == ' ':
            second_letter_appeared = False

    return True


# Q23
def item_distance(inlist):
    out_dict = {}
    range_saver_dic = {}
    for i in range(len(inlist)):
        element = inlist[i]
        # not in dict
        if element not in out_dict:
            out_dict[element] = []
            range_saver_dic[element] = i

        # element already in dict
        else:
            # -1 to correct the calculation using the indices
            distance = (i - 1) - range_saver_dic[element]
            out_dict[element].append(distance)
            range_saver_dic[element] = i

    return out_dict


# Q24
def n_repetitions(inlist):
    out_lst = []

    # use for i because first element is needed for setup
    current_element = inlist[0]
    current_element_count = 1

    for i in range(1, len(inlist)):
        element = inlist[i]
        # if element is same as element before
        if element == current_element:
            current_element_count += 1

        # if element is a different one that before
        else:
            out_lst.append(current_element_count)
            current_element = element
            current_element_count = 1

    # after iterating through list save for last element aswell
    out_lst.append(current_element_count)

    return out_lst


# Q25
def odd_vowels_upper(instr):
    # Examples show that this question has inconsistencies
    # Does the counter reset after every word?
    # One example makes it seem like it does, the other negates this
    # ToDo Question apparently unclear
    # Note: it seems like if there are two spaces between words it works
    # But the example inputs only have one space
    vowels = ['a', 'e', 'i', 'o', 'u']
    out_str = ""
    i = 0

    for current_char in instr:

        # if vowel and odd position
        if current_char in vowels and i % 2 == 1:
            out_str += current_char.upper()
        elif current_char == ' ':
            out_str += current_char
            i = -1
        else:
            out_str += current_char
        i += 1

    return out_str


# Q26
# given function header is wrong, is missing div1 and div2
def filter_divisitors(inlist, div1, div2):
    out_lst = []
    for element in inlist:
        if (element / div1) % 1 == 0 and (element / div2) % 1 == 0:
            out_lst.append(element)

    return out_lst


# Q27
def ascii_fun1(n):
    matrix = []

    # create matrix
    for i in range(n):
        matrix.append([])
        for j in range(n + 1):
            matrix[i].append([])
            matrix[i][j] = False

    # half_row_index is an integer that is used to invert the algorithm after
    # the first half of the shape is drawn
    half_row_index = int(n / 2)
    # fill matrix
    for row in range(n):
        # variable for possible adjustments after inversion of the alg
        adjusted_row = row
        if row > half_row_index:
            # Inversion
            adjusted_row = (n - 1) - row

        for col in range(adjusted_row + 1):
            matrix[row][col] = True
            matrix[row][(col * -1) - 1] = True

    # convert matrix to string
    out_str = ""
    for row in matrix:
        for col in row:
            if col:
                out_str += "*"
            else:
                out_str += " "
        out_str += "\n"

    write_to_file("ascii_fun1.txt", out_str)


# Q28
def python_power(nrows, ncols):
    matrix = []

    # Create matrix
    for i in range(nrows):
        matrix.append([])
        for j in range(ncols):
            matrix[i].append([])

    max_pow_value = -1

    for i in range(nrows):
        for j in range(ncols):
            corr_i = i + 1
            corr_j = j + 1
            pow_result = corr_i ** corr_j

            matrix[i][j] = pow_result
            max_pow_value = max(max_pow_value, pow_result)
            # matrix[i][j] = str(corr_i) + " ** " + str(corr_j) + " = " + str(pow_result)

    out_string = ''
    max_result_length = len(str(max_pow_value))

    for i in range(nrows):
        for j in range(ncols):
            corr_i = i + 1
            corr_j = j + 1

            out_string += f"{corr_i} ** {corr_j} = {matrix[i][j]:>{max_result_length}}\t\t"

        out_string += "\n"

    write_to_file("python_power.txt", out_string)


# Q29
def odd_lower_even_upper(instr):
    # ToDo again the special case that after every whitespace the count is reset
    #  is not mentioned

    out_str = ''
    split_instr = instr.lower().split(" ")

    for word in split_instr:

        char_count_dict = {}
        # fill the dict
        for char in word:
            if not char.isalpha():
                continue

            # char not in dict
            if char not in char_count_dict:
                char_count_dict[char] = 1
            # char in dict
            else:
                char_count_dict[char] = char_count_dict[char] + 1

        for char in word:
            # For whitespaces and others
            if not char.isalpha():
                out_str += char

            # if 1-infinity = True
            elif char_count_dict[char] % 2:
                # Odd
                out_str += char.lower()
            else:
                # Even
                out_str += char.upper()

        out_str += ' '

    return out_str


# Q30
def longest_substring_with_vowel(instr):
    vowels = ['a', 'e', 'i', 'o', 'u']

    found_substrings = []
    current_substring = ""
    current_substring_has_vowel = False

    for char in instr:
        # space char found
        if char == " ":
            if current_substring_has_vowel:
                found_substrings.append(current_substring)
            current_substring = ""
            current_substring_has_vowel = False

        # new char found
        elif char not in current_substring:
            current_substring += char
            if char in vowels:
                current_substring_has_vowel = True

        # old char found
        else:
            if current_substring_has_vowel:
                found_substrings.append(current_substring)
            current_substring = current_substring[current_substring.find(char):]

            # Reset the vowel boolean
            current_substring_has_vowel = False
            for substring_char in current_substring:
                if substring_char in vowels:
                    current_substring_has_vowel = True

    if current_substring_has_vowel:
        found_substrings.append(current_substring)


    if len(found_substrings) == 0:
        return ""
    else:
        return max(found_substrings, key=len)
def main():
    # even_left_odd_right(5)
    # print(common_values([1, 2, 3], [1, 2, 3], [3, 4, 5]))
    # print(only_the_last(10, 10))
    # print(unique_digit_dict(122, 124))
    # print(divide_me([0, 1, 2, 3, 4, 5], 2))

    # print(ndigits_times_nletters(123, "abc"))
    # print(grid_sum_prod(4))
    # eight_bits()
    # print(min_mac_range(10, 2, 99))
    # print(add_me(4))

    # print(remove_lower_and_higher([1, 3, 2, 19, 23], 3, 20))
    # print(balanced_brackets("((())()))"))
    # count_me("qaYqy")
    # print(sum_odd_sum_even([1, 2, 3, 4]))
    # mean_rt_er([500, 600, 700], [1, 0, 0])

    # print(firstname_lastname())
    # TODO basic analysis needs to be implemented
    # basic_analysis()
    # print(shuffle_me(["A", "B", "C", "D", "E"]))
    # print(repeated_letter("a bc def ghij"))
    # print(first_index([3, 2, 1, 3]))

    # print(permutation_subset(2,3))
    # print(letter_order("AB AB", "A", "B"))
    # print(item_distance([1, 2, 3, 1, 3, 2, 1, 1, 3]))
    # print(n_repetitions([1, 1, 3, 2, 2, 1, 2]))
    # print(odd_vowels_upper("car elephant"))

    # print(filter_divisitors([2, 4, 6, 8], 2, 5))
    # ascii_fun1(23)
    # python_power(3, 5)
    # print(odd_lower_even_upper("test that"))
    print(longest_substring_with_vowel("abcd ef"))

    #frequent_first("abbccc abc")
    return


def write_to_file(filename, string):
    with open("outs/" + filename, "w") as file:
        file.write(string)


main()
