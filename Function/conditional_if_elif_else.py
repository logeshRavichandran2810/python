def main(day):  
    if(day ==1):
        print("Monday")
    elif(day==2):
        print("Tuesday")
    elif(day==3):
        print("Wednesday")
    elif(day==4):
        print("Thursday")
    elif(day==5):
        print("Friday")
    elif(day==6):
        print("Saturday")
    elif(day==7):
        print("Sunday")
    else:
        print("Enter a number between 1 to 7")
if __name__=="__main__":
    day=int(input("Enter a day :"))
    main(day)