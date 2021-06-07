def read():
    number = []
    with open("./archivos/prueba.txt","r",encoding="utf-8") as f:
        for line in f:
            assert line.isnumeric, "Tenemos un registro que no es numerico"
            number.append(int(line))
        print(number)
        f.close

def write():
    names = ["víctor","antonella","vanessa"]
    with open("./archivos/nombres.txt","w",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
        f.close
def run():
    #read()
    write()

if __name__ == '__main__':
    run()