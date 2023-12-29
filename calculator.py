import re
import sys

from typing import Union, List

def sumStrToFloat(number: Union[str, float, int], numberWithSign: Union[str, float, int]) -> float:
    '''
    :number: Can be a string, float or int 
    :numberWithSignal: Can be a string, float or int number, an it can has a signal for example: "+1" or "-1"
    '''

    return float(number) + float(numberWithSign)

def mulStrToFloat(number: Union[float, int], number2: Union[str, float, int]) -> float:
    return float(number) * float(number2)

def divStringtoFloat(number: Union[float, int], number2: Union[str, float, int]) -> float:
    return float(number) / float(number2)

def main(argv: List[int]) -> int:
    debug = False
    for string in argv:
        if string == "debug=true": debug=True

    func = {
        '+': sumStrToFloat,
        '-': sumStrToFloat,
        '*': mulStrToFloat,
        '/': divStringtoFloat }

    result = 0.0
    calculation: list = input("Type the Calculation: ").strip().split(' ')

    buff_calc = []
                    # float                # int        # signals
    reStrings = [r"[0-9]{1,}\.[0-9]{1,}",  r"[0-9]{1,}", r"[\+\-\*\/]"]
    for item in calculation:
        i=0 # Start with float 

        while item != '':
            try:
                match = re.match(reStrings[i], item)

                buff_calc.append(item[match.span()[0]:match.span()[1]])
                item = item[match.span()[1]:]

                i+=1
                if i>2: i=0 

            except AttributeError:
                i+=1
                if i>2: i=0

    calculation = buff_calc
    del buff_calc, reStrings

    OrderSigns = ['/','*','-','+']
   
    while len(calculation) != 1:
        if debug: print(calculation)

        signal, i = None, 0
        while not signal:
            try: signal = calculation.index(OrderSigns[i])
            except ValueError: i+=1

        calculation[signal-1] = func[calculation[signal]] (
            calculation[signal-1],
            calculation[signal+1] )
        calculation.pop(signal)
        calculation.pop(signal)
        # One example of what's going on here
        # ['11', '+', '11'}
        #    ^____^____^
        #         |
        #        22
        # [22, '+', '11'] -> two pop is called -> [22]

    result = calculation[0]

    # print result with float numbers if it has a value otherwise print at format of int
    print(f"{result:.0F}") if str(result).split('.')[1]=='0' else print(result)

if __name__ == "__main__": sys.exit(main(sys.argv))
