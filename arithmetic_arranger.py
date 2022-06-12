def format_exp(str, eval=False):
    res = str.split()

    if(res[1] not in '+-'):
        return 1  # Invalid operator

    if(not res[0].isdigit() or not res[2].isdigit()):
        return 2  # Invalid characters in values

    # Evaluate Expresssion
    ans = int(res[0])

    if(res[1] == '+'):
        ans += int(res[2])
    else:
        ans -= int(res[2])

    # Get difference of the lengths of the two numbers located at res[0] and res[2]
    len_diff = abs(len(res[0]) - len(res[2])) + 1
    max_len = max(len(res[0]), len(res[2]))

    if(max_len > 4):
        return 3

    if(len(res[0]) > len(res[2])):
        res[0] = ' ' * 2 + res[0]
        res[2] = ' ' * len_diff + res[2]
    else:
        res[0] = ' ' * (len_diff + 1) + res[0]
        res[2] = ' ' + res[2]

    result = []
    result.append(res[0])
    result.append(res[1] + res[2])
    result.append('-' * (max_len + 2))

    ans = "{}".format(ans)
    ans = ' ' * (max_len - len(ans) + 2) + ans
    result.append(ans)

    return result


def arithmetic_arranger(expressions, eval=False):
    expr_len = len(expressions)
    if(expr_len > 5):
        return 'Error: Too many problems.'

    ans = ''
    results = []

    for exp in expressions:
        outcome = format_exp(exp, eval)

        if(outcome == 1):
            return "Error: Operator must be '+' or '-'."
        elif(outcome == 2):
            return 'Error: Numbers must only contain digits.'
        elif(outcome == 3):
            return 'Error: Numbers cannot be more than four digits.'
        else:
            results.append(outcome)

    loop_limit = 4 if eval else 3

    for i in range(0, loop_limit):
        j = 1

        for val in results:
            ans += val[i] + ' ' * (4 if j < expr_len else 0)
            j += 1

        ans += '\n'

    return ans.rstrip()


print(repr(arithmetic_arranger(
    ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])))
