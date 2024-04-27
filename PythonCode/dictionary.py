# dictionary = a changeable, unorderd collection of unique key: value pairs
#             fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'Inda':'New Dehli',
            'China':'Beihing',
            'Russia':'Moscow'}
#add germany index
capitals.update({'Germany':'Berlin'})
#update index
capitals.update({'USA': 'LAS VEGAS'})
#remove index
capitals.pop('China')
#clear all indexc
# capitals.clear()
# print(capitals['Russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
print(capitals.values())
#print(capitals.items())

for key, value in capitals.items():
    print(key, value)
