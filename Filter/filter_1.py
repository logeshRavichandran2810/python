from functools import reduce
def checknum(num):
    if(num<=25 and num>=10):
        return True
    return False
def increment(num):
    return num+10
def addition(num1,num2):
    return num1+num2
def main():
    number=[11,12,13,14,15,16,17,18] # sequence or iterable
    
    filter_result=tuple(filter(checknum,number))
    print("Filter result : ",filter_result)
    
    map_result=list((map(increment,filter_result)))
    print("Map result : ",map_result)
    
    reduce_result=reduce(addition,map_result)
    print("Reduce result : ",reduce_result)
    
if __name__=="__main__":
    main()
    