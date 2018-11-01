inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = "'seashell', 'strange berry', and 'lint'"
print("Here is your iventory with new category:",'\n',inventory)

inventory['backpack'].remove('dagger')
print("Here is your inventory when removing one item:",'\n',inventory)

inventory['gold'] += 50 
print("gold:",inventory['gold'])