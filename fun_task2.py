# task 1
# menu Card 
# Menu_card=['Dosa','Idly','Biriyani']
# 1.display
# 2.add
# 3.update
# 4.delete

# 1.dispaly (given menu) added successfuly
# 2.add(what you want to add menu card?'paratha')
# 3.update
# 4.delete

# task 2 calculator [+,-,*,/,//,**]

# task 3 shopping cart (add to cart,remove from cart,total item)


def display():
    print("Menu : ",Menu)
    
def add(additem):
    addeditem=Menu.append(additem)
    display()
    print("Item Added Successfully \n")

    
def update(old,new):
    index=Menu.index(old)
    Menu.remove(old)
    Menu.insert(index,new)
    display()
    print("Item Updated Successfully \n")
    
def delete(delitem):
    deleteitem=Menu.remove(delitem)
    display()
    print("Item Deleted successfully")
    
    
def main():
    while(True):
        
        print("\n 1.Display The Items \n 2.Add The Item \n 3.Update The Item \n 4.Delete The Item \n")
        option=int(input("Enter Your Option : "))
        if(option==1):
            display()
        elif(option==2):
            additem=input("Enter the Item To Add :")
            add(additem)
        elif(option==3):
            old = input("Enter the element to replace : ")
            new = input("Enter your new Item : ")
            update(old,new)
        elif(option==4):
            delitem = input("Enter the Item to delete :")
            delete(delitem)
        else:
            print("Enter the above option 1 / 2 / 3 / 4 ")
        
    
if __name__=="__main__":
   
    Menu=['Dosa','Idly','Biriyani']
    main()