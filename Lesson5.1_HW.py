multiple5 = [i for i in range(1, 101) if i % 5 == 0]
print(multiple5)

devider999 = [i for i in range(1, 1000) if 999 % i == 0]
print(devider999)

names = ['Alex', 'Kira', 'Michael', 'Alisa', 'Lida', 'John', 'Rita', 'Mitt', 'Benjamin']
end_with = [i for i in names if i.endswith('a')]
print(end_with)

start_with = [i for i in names if i.startswith('A')]
print(start_with)

names_len = [i for i in names if len(i) == 4]
print(names_len)

a_in_name = [i for i in names if 'a' in i]
print(a_in_name)

without_l = [i for i in names if 'l' not in i]
print(without_l)
