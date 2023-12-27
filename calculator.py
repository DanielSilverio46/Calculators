import re
import sys


def main() -> int:
    result = 0.0

    calculation: list = input("Type the Calculation: ").strip().split(' ')
    buff_calc = []

    for item in calculation:
        while item != '':
            number = re.match("[0-9]{1,}", item)
            if number:
                buff_calc.append(item[number.span()[0]:number.span()[1]])
                item = item[number.span()[1]:]

            sign = re.match("[\+\-\*\/]", item)
            if sign:
                buff_calc.append(item[sign.span()[0]:sign.span()[1]])
                item = item[sign.span()[1]:]

    calculation = buff_calc
    del buff_calc

    signs = ['+','-','*','/']
    # Check string of next index is a number
    if calculation[0].replace('.', '').isnumeric():
        result=float(calculation[0])
        calculation.pop(0)
        
    for i in range(len(calculation)):
        if calculation[i] in '+-':
            i += 1

            if calculation[i].replace('.', '').isnumeric():
                result += float(calculation[i-1]+calculation[i])

        elif calculation[i] in '*/':
            i += 1

            if calculation[i].replace('.', '').isnumeric():
                number = float(calculation[i])
                if calculation[i-1] == '*': result *= number
                else: result /= number

    print(result)

if __name__ == "__main__":
    sys.exit(main())
