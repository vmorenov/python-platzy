def run():
    palindromo =  lambda string: string == string[::-1]

    print(palindromo('victor'))

if __name__ == '__main__':
    run()