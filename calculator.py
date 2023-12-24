from typing import Union, Optional

import sys
import re

result: Union[int, float] = 0

def main() -> int:
    global result

    calculation: str = input("Type the Calculation: ").strip()
    calculate: bool = False

    while True:
        if calculation == '': break

        strNumber: Optional[re.Match] = re.match(r"[0-9]{1,}", calculation)
        strSignal: Optional[re.Match] = re.match(r"[\+\-\*\/]", calculation)

        number: int = 0
        signal: str = ''

        if strNumber:
            start, stop = strNumber.span()
            strNumber = calculation[start:stop]
            
            number = int(strNumber)
            calculation = calculation[stop:].strip()

            if result == 0:
                result = number

            elif calculate:
                if signal == '+':
                    result += number
                
                elif signal == '-':
                    result -= number
                
                elif signal == '*':
                    result *= number
                
                elif signal == '/':
                    result /= number
                
                calculate = False

        if strSignal:
            start, stop = strSignal.span()
            signal = calculation[start]
            calculation = calculation[stop:].strip()

            calculate = True

    print("It's equal ", result)

    return 0


if __name__ == "__main__": sys.exit(main())
