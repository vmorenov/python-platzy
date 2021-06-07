def run():
    my_list= [1,"Hello",True,4.5]
    my_dict = {"firstname": "Victor", "lasname": "Moreno"}

    super_list = [
        {"firstname": "Victor", "lastname": "Moreno"},
        {"firstname": "Vanessa", "lastname": "Porma"},
        {"firstname": "Antonella", "lastname": "Moreno"},
        {"firstname": "Vania", "lastname": "Moreno"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5,6],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }
    for x in super_list:
        print(x["firstname"],"-",x["lastname"])
    
    for pepito, pepita in super_dict.items():
        print(pepito,"-",pepita)

if __name__ == '__main__':
    run()