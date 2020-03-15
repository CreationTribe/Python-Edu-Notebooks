# import

name = 'thommy'.title()
date_today = 24
welcomemsg = "hit "+name+' '+str(date_today)

print(welcomemsg)

nodes = ['BACKPORTS','DISABLER','DUNKIRK','BRASSWALL']
nodes.append('BAGTROPE')
nodes.insert(nodes.index('DISABLER'),'LOCKHEARTE')
del nodes[nodes.index('BAGTROPE')]

print(nodes)

elPopped = nodes.pop(2)

print(nodes)
print(elPopped)
nodes.sort()
print(nodes)
nodes.sort(reverse=True)
print(nodes)
print(sorted(nodes, reverse=True))

print(len(nodes))

for node in nodes:
    if node == 'DUNKIRK':
        print('got dangit, you dunkirked it!')
    print(node)

print('hey')

for value in range(1, 100):
    print(value)