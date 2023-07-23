magazine = {'Storage': {}}
korzina = {}
print('Wellcome in Market')

while True:
    print('\nActions: Add, Sell, Storage, Korzina')
    action = input('What do you want to do: ')
    if action.lower() == 'add':
        pr_name = input('Name of product: ')
        pr_name = pr_name.title()
        pr_count = int(input('Count of products: '))
        magazine['Storage'][pr_name] = pr_count
    elif action.lower() == 'sell':
        pr_name = input('Name of product: ')
        pr_name = pr_name.title()
        if pr_name in magazine['Storage']:
            pr_count = int(input('Count of products to sell: '))
            korzina[pr_name] = pr_count
        else:
            print("This product isn't in the storage")
            continue
        if magazine['Storage'][pr_name] >= pr_count:
            pr_count = magazine['Storage'][pr_name] - pr_count
        else:
            print("Market hasn't enough products")
            continue
        magazine['Storage'][pr_name] = pr_count
    elif action.lower() == 'storage':
        for p, c in magazine['Storage'].items():
            print(f'{p} - {c}')
    elif action.lower() == 'korzina':
        n = True
        while n == True:
            print('\nActions with korzina: See, Edit, Remove, Clear, Back')
            korzina_action = input('Choose action with korzina: ')
            if korzina_action.lower() == 'see':
                for p, c in korzina.items():
                    print(f'{p} - {c}')
            elif korzina_action.lower() == 'edit':
                for p, c in korzina.items():
                    print(f'{p} - {c}')
                pr_name = input('Enter product you want edit: ')
                pr_count = int(input('Enter new count of product: '))
                if pr_count <= korzina[pr_name] + magazine['Storage'][pr_name]:
                    if korzina[pr_name] > pr_count:
                        magazine['Storage'][pr_name] += korzina[pr_name] - pr_count
                        korzina[pr_name] = pr_count
                    elif korzina[pr_name] < pr_count:
                        magazine['Storage'][pr_name] += pr_count - korzina[pr_name]
                        korzina[pr_name] = pr_count
                    else:
                        print('You didn\'t change count')
            elif korzina_action.lower() == 'remove':
                for p, c in korzina.items():
                    print(f'{p} - {c}')
                pr_name = input('Enter product which you want remove: ')
                korzina.pop(pr_name)
            elif korzina_action.lower() == 'clear':
                korzina.clear()
            elif korzina_action.lower() == 'back':
                n = False
    else:
        print('No identify action')
