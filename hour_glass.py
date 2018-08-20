#Python code to print hour glass

rows=input("Enter rows : ")

if rows == 0 or rows == 1:
    print("Invalid row Specified !!")
else:
    for i in range((-rows+1),0):
        print ((rows+i)*' '+((-i)*'*')+(((-i)+1)*'*'))
    for i in range(0,(rows)):
        print ((rows-i)*' '+((i)*'*')+((i+1)*'*'))

