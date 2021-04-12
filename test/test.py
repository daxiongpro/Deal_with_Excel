# Time: 2020/7/3-14:54
# Author: Rex

start_money = 12000
rate = 0.1
years = 50
money_result = 1000000

def get_money_result(start_money, rate, years):
    now_money = start_money
    for year in range(years):
        now_money = now_money * rate + now_money + start_money
        print(year + 1, now_money)
    result = now_money
    return result

def get_year(start_money, rate, money_result):
    year = 0
    now_money = start_money
    while now_money < money_result:
        year += 1
        now_money = now_money * rate + now_money
        print(year, now_money)
    result = year
    return result

# print("When you {} years old, you'll get {} ".format(years + 22, get_money_result(start_money, rate, years)))
print('{0} money when you are {1} years '.format(money_result, get_year(start_money, rate, money_result) + 22))