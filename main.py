import enquiries

# tempo ✓
# velocidade ✓
# temperatura 
# comprimento ✓

def velocidade():
    options = ['m/s', 'km/h', 'mph', 'ft/s']

    opt_from = enquiries.choose('De:  ', options)
    opt_to = enquiries.choose(f'De: {opt_from} \nPara: ', options)

    print(f"[*] {opt_from} → {opt_to}\n")

    num = int(input("Digite o número a ser convertido\n> "))

    def convert(opt_from, opt_to, num):

        x = {
            'm/s': lambda x: x,
            'km/h': lambda x: x/3.6,
            'mph': lambda x: x*0.44704,
            'ft/s': lambda x: x*0.3048,
        }[opt_from](num)

        result = {
            'm/s': lambda x: x,
            'km/h': lambda x: x*3.6,
            'mph': lambda x: x/0.44704,
            'ft/s': lambda x: x/0.3048,
        }[opt_to](x)

        result = round(result, 5)

        print(f"\n[✓] {num} {opt_from} = {result} {opt_to}\n")

        pass

    convert(opt_from, opt_to, num)

    pass

def temperatura():
    print('test temperatura')
    pass

def comprimento():
    options = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km', 'light-year']

    opt_from = enquiries.choose('De:  ', options)
    opt_to = enquiries.choose(f'De: {opt_from} \nPara: ', options)

    print(f"[*] {opt_from} → {opt_to}\n")

    num = int(input("Digite o número a ser convertido\n> "))

    def convert(opt_from, opt_to, num):

        x = {
            'mm': lambda x: x/10/10/10,
            'cm': lambda x: x/10/10,
            'dm': lambda x: x/10,
            'm': lambda x: x,
            'dam': lambda x: x*10,
            'hm': lambda x: x*10*10,
            'km': lambda x: x*10*10*10,
            'light-year': lambda x: x * (60*60*24*365) * (3*10**8)
        }[opt_from](num)

        result = {
            'mm': lambda x: x*10*10*10,
            'cm': lambda x: x*10*10,
            'dm': lambda x: x*10,
            'm': lambda x: x,
            'dam': lambda x: x/10,
            'hm': lambda x: x/10/10,
            'km': lambda x: x/10/10/10,
            'light-year': lambda x: x / (60*60*24*365) / (3*10**8)
        }[opt_to](x)

        result = round(result, 5)

        print(f"\n[✓] {num} {opt_from} = {result} {opt_to}\n")

        pass

    convert(opt_from, opt_to, num)

    pass

def tempo():
    options = ['ms', 's', 'min', 'hour', 'day', 'week', 'year']

    opt_from = enquiries.choose('De:  ', options)
    opt_to = enquiries.choose(f'De: {opt_from} \nPara: ', options)

    print(f"[*] {opt_from} → {opt_to}\n")

    num = int(input("Digite o número a ser convertido\n> "))

    def convert(opt_from, opt_to, num):

        x = {
            'ms': lambda x: x/1000,
            's': lambda x: x,
            'min': lambda x: x*60,
            'hour': lambda x: x*60*60,
            'day': lambda x: x*60*60*24,
            'week': lambda x: x*60*60*24*7,
            'year': lambda x: x*60*60*24*365,
        }[opt_from](num)

        result = {
            'ms': lambda x: x*1000,
            's': lambda x: x,
            'min': lambda x: x/60,
            'hour': lambda x: x/60/60,
            'day': lambda x: x/60/60/24,
            'week': lambda x: x/60/60/24/7,
            'year': lambda x: x/60/60/24/365,
        }[opt_to](x)

        result = round(result, 5)

        print(f"\n[✓] {num} {opt_from} = {result} {opt_to}\n")

        pass

    convert(opt_from, opt_to, num)

    pass

def show_main_menu():
    options = [{
        'label' : '1. Tempo',
        'func': 'tempo'
    },{
        'label' : '2. Velocidade',
        'func': 'velocidade'
    },
    {
        'label' : '3. Temperatura',
        'func': 'temperatura'
    },
    {
        'label' : '4. Comprimento',
        'func': 'comprimento'
    }]

    options_label = []

    for option in options:
        options_label.append(option['label'])

    print("""
#############################
#                           #
#   Conversor de Unidades   #
#                           #
#############################
""")

    choice = enquiries.choose('Escolhe uma destas opções: ', options_label)

    for option in options:
        if option['label'] == choice:
            globals()[option['func']]()


if __name__ == '__main__':
    show_main_menu()
