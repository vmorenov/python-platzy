from functools import reduce

def run():
    #funcion de alto orden filter, se agrega una condicional que se debe cumplir para incluir en nueva lista
    my_list = [1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x: x%2 != 0,my_list))
    print(odd)

    #funcion de alto orden map, ejecuta un calculo sobre cada campo de la lista
    my_list_map = [1,2,3,4,5,6]
    squares = list(map(lambda z: z**2, my_list_map))
    print(squares)

    #funcion de alto orden reduce, evita la iteración para llegar a un resultado
    all_multiplied = [2,2,2,2,2] 
    app = reduce(lambda x,z: x*z,all_multiplied)

    print(app)


if __name__ == '__main__':
    run()