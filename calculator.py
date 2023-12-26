import sys


def main() -> int:
    result: float = 0.0

    calculation: str = input("Type the Calculation: ").strip().split(' ')
    if calculation[0].replace('.', '').isnumeric():
        result=float(calculation[0])
        calculation.pop(0)
        
    for i in range(len(calculation)):
        if calculation[i] in '+-':
            # Check string of next index is float or int
            if calculation[i+1].replace('.', '').isnumeric():
                result += float(calculation[i] + calculation[i+1])
                i += 1

        elif calculation[i] == '*':
            if calculation[i+1].replace('.', '').isnumeric():
                result *= float(calculation[i+1])
                i += 1

        elif calculation[i] == '/':
            if calculation[i+1].replace('.', '').isnumeric():
                result /= float(calculation[i+1])
                i += 1

    print(result)

if __name__ == "__main__":
    sys.exit(main())
