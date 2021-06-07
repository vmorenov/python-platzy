def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No puedes ingresar un vacio a la función")
        return string==string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        print(palindrome(""))
    except TypeError:
        print("solo se pueden ingresar String")
    finally:
        print("termino la funcion y este codigo siempre se va ejecutar al final de todo independiente del error")

if __name__ == '__main__':
    run()