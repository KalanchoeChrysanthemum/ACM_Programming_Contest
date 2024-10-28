from itertools import permutations

def main():

    num_cases = int(input())

    operations = ['*', '//', '+', '-', '*', '//', '+', '-', '*', '//', '+', '-', '*', '//', '+', '-']
    full_list = permutations(operations, 3)
    unique_list = []
    results = []

    for item in full_list:
        if item in unique_list:
            continue
        unique_list.append(item)

    for _ in range(0, num_cases):
        num = int(input())

        found = False
        result = 'no solution'
        for item in unique_list:
            function = f'4 {item[0]} 4 {item[1]} 4 {item[2]} 4'
            if eval(function) == num:
                result = function.replace('//', '/') + ' = ' + str(num)
                found = True
                break

        results.append(result)

    for result in results:
        print(result)

def solve(nums: list, operations: list) -> list:
    sol = nums
    for index, operation in enumerate(operations):
        if operation == '*':
            result = nums[index] * nums[index + 1]
        if operation == '/':
            result = nums[index] / nums[index + 1]
        if operation == '+':
            result = nums[index] + nums[index + 1]
        if operation == '-':
            result = nums[index] - nums[index + 1]
        
        if index == 0:
            sol = [result, sol[1:]]
        elif index == 1:
            sol = [sol[0]]
        else:
            return


if __name__ == '__main__':
    main()