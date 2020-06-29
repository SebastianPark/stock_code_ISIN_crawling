import pandas as pd


# df = pd.read_csv('ISIN_codes.csv')
#
# codes = [f for f in df[' codes']]
#
# print(len(codes))


def krw2other(current_rate):
    return lambda krw: round(krw/current_rate,3)
def solution(n):
    numbers = []
    for i in range(10):
        remain = n%10
        numbers.append(remain)
        n = n//10
        if n == 0:
            break
    answer = numbers
    return answer

def solution2(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ''
        a_1 = arr1[i]
        a_2 = arr2[i]
        for y in range(n):
            res_1 = a_1%2
            res_2 = a_2%2
            if res_1 == 1 or res_2 ==1:
                tmp += "#"
            else:
                tmp += ' '
            a_1 = a_1//2
            a_2 = a_2//2

        print(tmp)
        tmp = tmp[::-1]
        print(tmp)
        answer.append(tmp)

    return answer

def binary_searching(budgets, M):

    mean = mean()

    answer = 0



    return answer


if __name__ == '__main__':
    # krw2usd = krw2other(1223.5)
    # krw2jpy = krw2other(9.83)
    #
    # print("3600원은 달러로 ", krw2usd(3600),"달러 입니다.\n",
    #       "3600원은 엔화로 ", krw2jpy(3600),"엔 입니다.\n")
    arr1 = [3, 1, 7]
    arr2 = [6, 3, 0]

    print(solution2(3 , arr1, arr2))


