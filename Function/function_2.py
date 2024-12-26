# positional argument
def main():
    # print(full_name(fname,lname)) positional
    # print(full_name(fname,lname,nationality='india')) keyword , defalut
    print(full_name(fname='Logesh',lname='Ravichandran',nationality='us'))
def full_name(fname,lname,nationality='india'):
    # return f"My name is {fname} {lname}
    # return f"My name is {fname} {lname} nationality {nationality}
    return f"My name is {fname} {lname} nationality {nationality}"
if __name__=="__main__":
    main()
