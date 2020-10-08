products_keys = list()
sum = 0
products = {}
while True:
    name = input('Enter q For Quit Or Enter The Name Of The Product Please Write A Name That Is Not In This Receipt: ')
    if name == 'q':
        calculate()
        break
    price = input('Enter The Price Of The Product: ')
    f = open('products.txt', 'w')
    f.write('')
    f.close()
    def calculate(write = False):
        products_keys = list(products)
        for i in range(len(products)):
            print(f'{products_keys[i]} =', end=' ')
            print(f'{products[products_keys[i]]}')
            if write == True:
                f = open('products.txt', 'a')
                f.write(
                        f'''{products_keys[i]} = {products[products_keys[i]]}
''')
                f.close()
        print(f'Total = {sum}')

    try:
        price = int(price)
        sum += price
        products[name] = price
        calculate(True)
    except Exception as e:
        print(f'Enter A Valid Price! The Error Is: {e}')

print('Thank For Using Our Calculator')
print('The Receipt Is Saved On products.txt')