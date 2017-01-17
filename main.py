import heapq
from struct import *

name = "Tommy D"

if name is "Bucky":
    print("Hey there Bucky")
elif name is "Lucy":
    print("What up Lucy")
elif name is "Sammy":
    print("What up Sammy!")
else:
    print("Please sing up for the site!")

foods = ["bacon", "tuna", "ham", "beef"]

# foods[:3] 从第几个元素开始，到第几个元素（不包含）
for food in foods[:3]:
    print(food)

print("--------------[0, 结束]-------------------")

for x in range(10):
    print(x)

print("-------------[开始, 结束]--------------------")

for x in range(3, 7):
    print(x)

print("--------------[开始, 结束, 步长]-------------------")

for x in range(4, 19, 4):
    print(x)

print("--------------while-------------------")

buttcrack = 5

while buttcrack < 10:
    print(buttcrack)
    buttcrack += 1

# 这是单行注释

magicNum = 26

'''
这是多行注释
用单引号
'''
for n in range(101):
    if n == 26:
        print(n, "this is the magic number!")
        break
    else:
        print(n)

print("--------------continue-------------------")

numTakens = [2, 5, 8, 12, 15, 17]

for n in range(20):
    if n in numTakens:
        continue
    print(n)

print("--------------function-------------------")


def beef():
    print("Dayum, functions are cool!")


def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)


def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age


beef()
bitcoin_to_usd(3.3)

buckys_limit = allowed_dating_age(27)
print("Bucky can date girls", buckys_limit, "or older")

print("--------------function default argument-------------------")


def get_gender(sex="Unknown"):
    if sex is "m":
        sex = "Male"
    if sex is "f":
        sex = "Female"
    print(sex)


get_gender('m')
get_gender('f')
get_gender()

print("--------------function argument order-------------------")


def dumb_sentence(name="Bucky", action="ate", item="tuna"):
    print(name, action, item)


dumb_sentence()
dumb_sentence("Sally", "farts", "gently")
dumb_sentence(item="awesome")
dumb_sentence(item="awesome", action="is")

print("--------------变长参数列表-------------------")


def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)


add_numbers(5)
add_numbers(2, 5)
add_numbers(2, 3, 5, 7, 2)

print("--------------Unpacking Arguments-------------------")


def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)


buckys_data = [27, 20, 0]

health_calculator(buckys_data[0], buckys_data[1], buckys_data[2])
health_calculator(*buckys_data)

print("--------------set 用{} list 用[]-------------------")

groceries = {"cereal", "milk", "starcrunch", "beer", "duct tape", "lotion", "beer"}
print(groceries)

if "milk" in groceries:
    print("You already have milk hoss!")
else:
    print("Oh yea, you need milk!")

print("--------------Dictionary-------------------")

classmates = {"Tony": "cool but smells", "Emma": "sits behind me", "Lucy": "asks too many questions"}

for k, v in classmates.items():
    print(k, v)


print("--------------except-------------------")


def dealExcept():
    while True:
        try:
            number = int(input("What's your favourite number hoss!\n"))
            print(18 / number)
            break
        except ValueError:
            print("Make sure and enter a number")
        except ZeroDivisionError:
            print("Don't pick zero")
        except:
            print("get a exception")
        finally:
            print("loop complete")


# dealExcept()

print("--------------Unpack List or Tuples-------------------")

data, name, price = ["December 23, 2016", "Bread Gloves", 8.5]
print(name)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print("avg = ", avg)

drop_first_last([65, 70, 78, 83, 90])
drop_first_last([45, 70, 78, 83, 94])

print("--------------Zip-------------------")

first = ["Bucky", "Tom", "Taylor"]
last = ["Roberts", "Hanks", "Swift"]

names = zip(first, last)

for a, b in names:
    print(a, b)

print("--------------Lambda-------------------")

answer = lambda x: x * 7

print(answer(5))

print("--------------Min, Max, and Sorting Dictionaries-------------------")

stocks = {
    "GOOG": 520.54,
    "FB": 76.45,
    "YHOO": 39.28,
    "AMAZON": 306.21,
    "AAPL": 99.76
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

print("--------------struct-------------------")

# Store as bytes data
packed_data = pack("iif", 6, 19, 4.73)
print(packed_data)

print(calcsize("i"))
print(calcsize("f"))
print(calcsize("iif"))

# To get bytes data back to normal (b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
original_data = unpack("iif", packed_data)
print(original_data)

print(unpack("iif", b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))

print("--------------map-------------------")

income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income))
print(new_income)

print("-------------- Binary AND -------------------")

a = 50      # 110010
b = 25      # 011001
c = a & b   # 010000

print(c)

print("-------------- Binary RIGHT SHIFT -------------------")

x = 240     # 11110000
y = x >> 2  # 00111100

print(y)

print("-------------- Finding Largest or Smallest Items -------------------")

grades = [13, 99, 18, 29, 17, 83, 65, 77, 55]
print(heapq.nlargest(3, grades))

stocks = [
    {"ticker": "AAPL", "price": 201},
    {"ticker": "GOOG", "price": 800},
    {"ticker": "FB", "price": 54},
    {"ticker": "MSFT", "price": 313},
    {"ticker": "TUNA", "price": 68}
]

print(heapq.nsmallest(3, stocks, key=lambda stock: stock["price"]))
