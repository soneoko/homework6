my_dict = {'Софья': 2008, 'Карина': 2010, 'Лилия': 2015, 'Анна': 2021}
print('Dict:', my_dict)
print('Exiting value:', my_dict['Софья'])
print('Not exiting value:', my_dict.get('Андрей'))
my_dict.update({'Андрей': 1986, 'Елена': 1987} )
print('Deleted value:', my_dict.pop('Андрей'))
print('Modified dictionary:', my_dict)
my_set = {2, 3, 2.5, 4.7, 'Home', 'Python', True, 4.7, 'Home', True}
print()
print('Set:', my_set)
my_set.add(9)
my_set.add(False)
my_set.discard(2.5)
print('Modified set:',my_set)