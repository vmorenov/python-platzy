def divisors(num):
    divisor = []
    for i in range(1,num+1):
        if num % i  ==  0 :
            divisor.append(i)
    return divisor

def run():
    try:
        num =  int(input("Ingresa un numero "))
        try:
            if num < 0 :
                raise ValueError("Debes ingresar un numero mayor a 0")            
            print(divisors(num))
        except ValueError as ve:
            print(ve)      
    except ValueError:
        print("Debes ingresar un numero")


if __name__ == '__main__':
    run()