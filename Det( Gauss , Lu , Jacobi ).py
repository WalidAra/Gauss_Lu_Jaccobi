import numpy as np

def Re_range_lines(arr,size):
    
    for i in range(size):
        pos = -1
        for j in range(size):
            if( arr[i][j] == 0):
                pos = j
                print("Found zero at : ",i,pos)
                
        if( pos >= 0 and i != pos ):
            A_copy = arr[i][:]
            arr[i][:] = arr[pos][:]
            arr[pos][:] = A_copy

def Lu(arr, size):
 
    upper = [[0 for _ in range(size)] for _ in range(size)]
    lower = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for k in range(i, size):

            sum = 0

            for j in range(i):

                sum += (lower[i][j] * upper[j][k])

            upper[i][k] = arr[i][k] - sum

        for k in range(i, size):

            if (i == k):

                lower[i][i] = 1 

            else:

                sum = 0

                for j in range(i):

                    sum += (lower[k][j] * upper[j][i])

                lower[k][i] = int((arr[k][i] - sum) /

                                  upper[i][i])

    print("Print Lower && Upper Matrix")

    for i in range(size):

        for j in range(size):

            print(lower[i][j], end="\t")

        print("", end="\t")

        for j in range(size):

            print(upper[i][j], end="\t")
            
        print("")

def Jacobi(arr , size , result ):

    print("\nVerify the Matrix \n\n")
    
    Re_range_lines(arr,size)

    do_it = True 
    for row in range(size):
        for colum in range(size):
            if( row == colum ):

                sum = 0
                for index in range(size):
                    if( arr[row][index] != arr[row][colum] ):
                        sum += arr[row][index]
                if( sum > arr[row][colum]):
                    do_it = False
                    break

    if( do_it == True ):

        print("\nThe Targets\n\n")
        for row in range(size):
            for colum in range(size):
                if( row == colum ):
                    print(arr[row][colum],end="\t")

        iteration = int(input("\n\nTime of iteration : "))

        print("\n\n Full The Vector\n\n")
        vector = [0 for _ in range(size)]

        for index in range(size):
            print("Enter " + str(index) + " vector element : ",end="")
            vector[index] = int(input(""))

        X = [0 for _ in range(size)]

        print("\n\n")
        
        for case in range(iteration):

            print("Case --"+str(case+1)+"--\n\n")
            for row in range(size):
                for colum in range(size):
                    if( row == colum ):

                        sum = 0
                        for index in range(size):
                            if( arr[row][colum] != arr[row][index]):
                                sum += (arr[row][index] * vector[row])

                        X[row] = ( (-sum) + result[row]) / (arr[row][colum])
                        print( "( " +  str(sum) + " + " + str(result[row]) + " ) / " + str(arr[row][colum]) + " = " + str(X[row]) )
            print("\n\n")                    

    else:
        print("You Can't apply Jacobi on This Matrix !!!\n")

def Gauss( arr , size , result ):
    
    det = np.linalg.det(arr)

    print("The Det of Matrix " + str(size) + " x " + str(size) + " is : ",det,end="\n\n")

    if( det != 0 ):

        print("The Targets\n\n")

        for i in range(size):
            for j in range(size):
                if( i > j):
                    print(arr[i][j],end="\t")
        print("\n\n")

        #Gauss Elimination

        for row in range(size):
            for colum in range(size):
                if( row > colum ):

                    s_exp = arr[row][colum] # the current element's value 

                    if( colum > 0 and arr[ row ][ colum - 1 ] == 0):
                        f_exp = arr[row - 1][ colum]
                        pos = row - 1

                    else:
                        f_exp = arr[0][0]
                        pos = 0
                    
                    for index in range(size):
                        num = ( s_exp * arr[pos][index] ) - ( f_exp * arr[row][index] )
                        arr[row][index] = num

                    result[row] = ( s_exp * result[pos]) - (f_exp * result[row]) 

        print("\n\nThe New Matrix")

        for i in range(size):
            for j in range(size):
                print(arr[i][j], end="  ")

            print("\t",result[i],end="\n")

        print("\n\n")
        line = 0
        X = 0
        for i in range(size - 1  , -1 , -1):
            for j in range(size - 1 , -1 , -1):

                if( i == j ):
                    sum = 0
                    for z in range(size  - 1, -1 , -1):
                        if( arr[i][j] != arr[i][z]):
                            sum += arr[i][z]

                    if( arr[i][j] != 0 ):
                        X = ( result[i] - sum ) / (arr[i][j])
                    
                    print("X" + str(line+1) + " = " + str(X))

            line += 1
            print("\n")
    else:

        print("Can't Do Gauss method\n")

print("\n\nEnter the size of Matrix : ",end="")
size = int(input(""))

while size == 0 or size < 0:
    print("Zero is not a valid size \n")
    print("Enter the size of Matrix : ",end="")
    size = int(input(""))

arr = [ [0 for _ in range(size) ] for _ in range(size) ]
result = [ 0 for _ in range(size) ]

print("\n")

def Full(arr , size , result ):

    for row in range(size):
        for colum in range(size):
            print("Enter the number ["+str(row)+"]["+str(colum)+"] : ",end="")
            number = int(input(""))
            arr[row][colum] = number 

    print("\n\n")

    for index in range(size):
        print("Enter the EQA : ",end="")
        num = int(input(""))
        result[index] = num 

    print("\n\n")

Full(arr , size , result )

print("***Matrix Methods***\n\n\n\t 1) Gauss \n\n\t 2) - Jacobi \n\n\t 3) - Lu \n\n\t")
option = int(input("INPUT :"))

if( option == 1 ):
    Gauss(arr , size , result )
    
elif( option == 2):
    Jacobi(arr , size , result )
    
elif( option == 3):
    Lu(arr,size)