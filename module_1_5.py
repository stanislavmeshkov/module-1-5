immutable_var = (2, 4, 6, 'var', False)
print(immutable_var)
#immutable_var[3] = 'Mik'
#print(immutable_var) # нельзя изменить назначение элементов, кортеж используют для защиты
                         # от случайных изменений. Занимает меньше памяти, чем список.

mutable_list = [2, 4, 6, 'list', True]
print(mutable_list)
mutable_list[3] = 'var'
print(mutable_list)