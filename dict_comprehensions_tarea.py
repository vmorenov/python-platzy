import math
def run():
    # my_dict = {}

    # for i in range(1,101):
    #     my_dict[i] = i**3
    # print(my_dict)

    my_dict = {i:math.sqrt(i) for i in range(1,1000) }
    print(my_dict)

if __name__ == '__main__':
    run()