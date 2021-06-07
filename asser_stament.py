def palindrome (string):
    assert len(string) > 0, "no se pueden ingresar cadenas vacias"
    return string == string[::-1]

def run():
    print(palindrome(""))

if __name__ == '__main__':
    run()