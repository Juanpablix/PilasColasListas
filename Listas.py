frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
frutas.count('manzana')
2
frutas.count('mandarina')
0
frutas.index('banana')
3
frutas.index('banana', 4) 
6
frutas.reverse()
frutas
['banana', 'manzana', 'kiwi', 'banana', 'pera', 'manzana', 'naranja']
frutas.append('uva')
frutas
['banana', 'manzana', 'kiwi', 'banana', 'pera', 'manzana', 'naranja', 'uva']
frutas.sort()
frutas
['manzana', 'manzana', 'banana', 'banana', 'uva', 'kiwi', 'naranja', 'pera']
frutas.pop()
'pera'

print(frutas)