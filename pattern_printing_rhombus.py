row = int(input("Enter the number no. of rows: "))

#loop to print the upper half of the pyramid
for i in range(1,row+1):
    #loop to print spaces before the astericks
    for j in range(1,row-i+1):
        print(" ",end="")
    #loop to print astericks or spaces
    for j in range(1,2*i):
        if(j==1 or j==i*2-1):
            print("*",end="")
        else:
            print(" ",end="")

    print()#to print new line


#loop to print the lower half of the pyramid
for i in range(row-1,0,-1):
    #loop to print spaces before the astericks
    for j in range(1,row-i+1):
        print(" ",end="")
    #loop to print astericks and spaces
    for j in range(1,2*i):
        if(j==1 or j==i*2-1):
            print("*",end="")
        else:
            print(" ",end="")

    print()#to print new line

