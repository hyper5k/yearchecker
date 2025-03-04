
groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:

    item_to_remove = input("What item do you want to remove from the list?")
    
 
    if item_to_remove.lower() == 'stop':
        break
    
    
    if item_to_remove in groceries:
        groceries.remove(item_to_remove)
        print(item_to_remove, "has been removed from the list.")
    else:
        print(item_to_remove, "is not in the list.")
    
    
    print("Updated grocery list:", groceries)


print("Final grocery list:", groceries)
