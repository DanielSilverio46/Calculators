from typing import Union, Optional

import sys
import re

result: Union[int, float] = 0

def sum(adder: Union[int, float]) -> Union[int, float]:
    global result
    result += adder

    return result

def sub(subtractor: Union[int, float]) -> Union[int, float]:
    global result
    result -= subtractor

    return result

def mul(multiplier: Union[int, float]) -> Union[int, float]:
    global result
    result *= multiplier

    return result  

def div(divider: Union[int, float]) -> Union[int, float]:
    global result
    result /= divider

    return result


def findNumber(calculation: str) -> re.Match:
    return re.match(r"[0-9]{1,}", calculation)

def findSignal(calculation: str) -> re.Match:
    return re.match(r"[\+\-\*\/]", calculation)


def main() -> int:
    global result

    calculation: str = input("Type the Calculation: ").strip()
    calculate: bool = False

    functions = { '+': sum, '-': sub, '*': mul, '/': div }

    while calculation != '':
        number = findNumber(calculation)

        if number:
            start_num, stop_num = number.span()
            calculation = calculation[stop_num:].strip()

            number = float(number.string[start_num:stop_num])

        signal = findSignal(calculation)

        if signal:
            start_sig, stop_sig = signal.span()
            calculation = calculation[stop_sig:].strip()

            signal = signal.string[start_sig:stop_sig]

            if type(number) == float:
                result = number
                number = findNumber(calculation)

                if number:
                    start_num, stop_num = number.span()
                    calculation = calculation[stop_num:].strip()

                    number = float(number.string[start_num:stop_num])

                    functions[signal](number)


    if str(result).split('.')[1] == '0':
        result = int(result)

    print("It's equal ", result)

    return 0


if __name__ == "__main__": sys.exit(main())
