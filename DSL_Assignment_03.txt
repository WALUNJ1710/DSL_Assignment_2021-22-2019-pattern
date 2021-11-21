Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

matrix= []
print("Enter the entries row wise:")


for i in range(Row):
    a =[]
    for j in range(Column):
        a.append(int(input()))
    matrix.append(a)


for i in range(Row):
    for j in range(Column):
        print(matrix[i][j], end = " ")
    print()

matrix2=[]
print("\nEnter the entries row wise for second matrix:")
for i in range(Row):
    a =[]
    for j in range(Column):
        a.append(int(input()))
    matrix2.append(a)


for i in range(Row):
    for j in range(Column):
        print(matrix2[i][j], end = " ")
    print()

result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def addition():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j] + matrix2[i][j]

    for r in result:
        print(r)

def multiplication():
    for i in range(len(matrix)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
             result[i][j] += matrix[i][k] * matrix2[k][j]

    for r in result:
        print(r)


def subtraction():
    for i in range(len(matrix)):
        # iterate through columns
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j] - matrix2[i][j]

    for r in result:
        print(r)

def transpose():
    for i in range(len(matrix)):
        # iterate through columns
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    for r in result:
        print(r)

while True:
    print("\n****** MAIN MENU ******")
    print("1. ADDITION OF A MATRIX ")
    print("2. MULTIPLICATION OF A MATRIX ")
    print("3. SUBTRACTION OF MATRIX")
    print("4. TRANSPOSE OF A MATRIX")
    ch=int(input("Enter your choice: "))

    if ch==1:
        print(" \n ADDITION OF GIVEN TWO MATRICES :")
        addition()
    elif ch==2:
        print("\n multiplication of given matrices :")
        multiplication()
    elif ch==3:
        print(" \n SUBTRACTION OF GIVEN TWO MATRICES :")
        subtraction()
    elif ch==4:
        print(" \n TRANSPOSE OF GIVEN TWO MATRICES :")
        transpose()
    else:
        print("wrong choice")
        break