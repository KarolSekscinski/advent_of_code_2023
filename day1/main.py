digits = {'one': "1", 'two': "2", 'three': "3", 'four': "4", 'five': "5", 'six': "6", 'seven': "7", 'eight': "8", 'nine': "9"}
with open("file.txt", "r") as f:
    text = f.readlines()
    sum_array = []
    # Part two
    for i, line in enumerate(text):
        for value, digit in digits.items():
            temp_line = line
            if value in temp_line.strip():
                new_line = temp_line.replace(value, value[:2] + digit + value[2:])
                line = new_line
                text[i] = new_line
    # Part one
    for line in text:
        print(f"line: {line.strip()}")
        for char in line:
            if char.isnumeric():
                first_digit = char
                print(f"first digit: {char}")
                break
        for char in line[::-1]:
            if char.isnumeric():
                sec_digit = char
                print(f"second digit: {char}")
                break
        line_sum = first_digit + sec_digit
        print(f"line_sum: {line_sum}")
        sum_array.append(line_sum)
        print()
sum_val = 0
for elem in sum_array:
    sum_val = sum_val + int(elem)

print(sum_val)




