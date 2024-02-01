class OperatorException(Exception):
    '''This operation is not allowed'''
    pass


operations = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def validate(lst: list[str]) -> tuple:
    '''This function checks data input'''
    if not lst[0].isdigit() or not lst[2].isdigit():
        raise ValueError('This calculation expressions of the from [1 + 2]')
    if not isinstance(lst[1], str):
        raise ValueError('This calculation expressions of the from [1 + 2]')
    
    a, b = int(lst[0]), int(lst[2])
    oper = lst[1]
    
    if not oper in operations.keys():
        raise  OperatorException(f'This operation is not allowed "{oper}"')
    if  not 0 < a < 10 or not 0 < b < 10:
        raise ValueError(f'input value must be between 0 and 10: [a={a}, b={b}]')
    return a, b, oper

def main() -> int:
    try:
        value_lst = input().split()
        a, b, oper = validate(value_lst)
        result = int(operations[oper](a, b))
    except Exception:
        print('unexpected error')
    
    return result

print(main())
