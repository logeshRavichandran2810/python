def main():
    number=["loki",123,"ram",124,10.2] # sequence or iterable
    
    filter_result=tuple(filter(lambda num:isinstance(num ,int),number))
    print("Filter result : ",filter_result)
    

if __name__=="__main__":
    main()
     