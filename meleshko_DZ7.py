# #task1
# from datetime import datetime
# def working_hours_only(func):
#     def wrapper():
#         if 9 <= int(datetime.now().strftime('%H')) <= 18:
#             func()
#         else:
#             print('Работать нельзя!')
#     return wrapper
# @working_hours_only
# def work():
#     print("Работаем")
#     return
# work()
#task2
def type_check(correct_type):
    def inner(func):
        def wrapper(object):
            if type(object) == correct_type:
                print(func(object))
            else:
                print('Bad type')
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num*2


@type_check(str)
def first_letter(word):
    return word[0]


@type_check(bool)
def boolean_mean(arg):
    return arg

@type_check(float)
def float_mean(fl):
    return fl

times2(2)
times2('2')

first_letter('hello world')
first_letter(False)

boolean_mean(True)
boolean_mean(1)

float_mean(3.5)
float_mean(3)