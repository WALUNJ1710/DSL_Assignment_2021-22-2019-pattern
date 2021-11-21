def removeDuplicate(d):
    L=[]
    for i in d:
        if i not in L:
            L.append(i)
    return L

# Function for finding intersection between two sets (A&B)

def intersection(L1,L2):
    L3=[]
    for val in L1:
        if val in L2:
            L3.append(val)
    return L3

# Function for finding union of two sets (A|B)

def union(L1,L2):
    L3=L1.copy()
    for val in L2:
        if val not in L3:
            L3.append(val)
    return L3

# Function for finding difference between two sets (A-B)
def diff(L1,L2):
    L3=[]
    for val in L1:
        if val not in L2:
            L3.append(val)
    return L3

# Function for finding symmetric difference of two sets (A^B)

def sym_diff(L1,L2):
    L3=[]
    D1=diff(L1,L2)
    print("Difference between Cricket and Badminton (C-B) is : ", D1)
    D2=diff(L2,L1)
    print("Difference between Badminton and Cricket (B-C) is : ", D2)
    L3=union(D1,D2)
    return L3

# Function for finding List of students who play both cricket and badminton

def CB(L1,L2):
    L3=intersection(L1,L2)
    print("\n List of students who play both cricket and badminton is : ", L3)
    return len(L3)

# Function for finding List of students who play either cricket or badminton but not both

def eCeB(L1,L2):
    L3=sym_diff(L1,L2)
    print("\n List of students who play either cricket or badminton but not both is : ",L3)
    return len(L3)

# Function for finding Number of students who play neither cricket nor badminton

def nCnB(L1,L2,L3):
    L4=diff(L1,union(L2,L3))
    print("\n List of students who play neither cricket nor badminton is : ",L4)
    return len(L4)

# Function for finding Number of students who play cricket and football but not badminton

def CBnF(L1,L2,L3):
    L4=diff(intersection(L1,L2),L3)
    print("\n List of students who play cricket and football but not badminton is : ",L4)
    return len(L4)

# Main function

# Creating an empty list for SE COMP
SEComp = []
n = int(input("\n Enter number of students in SE COMP: "))
print("Enter the names of",n,"students (Please press ENTER after entering each students name) :")
for i in range(0, n):
    element = input()
    SEComp.append(element)  # adding the element
print("Original list of students in SEComp : " + str(SEComp))

# Creating an empty list for Cricket
Cricket = []
n = int(input("\n Enter number of students who play cricket : "))
print("Enter the names of",n,"students who play cricket (Please press ENTER after entering each students name) :")
for i in range(0, n):
    element = input()
    Cricket.append(element)  # adding the element
print("Original list of students playing cricket is :" +str(Cricket))
Cricket=removeDuplicate(Cricket)
print("The list of students playing cricket after removing duplicates : " +str(Cricket))

# Creating an empty list for Football
Football = []
n = int(input("\n Enter number of students who play football : "))
print("Enter the name of",n,"students who play football (Please press ENTER after entering each students name) :")
for i in range(0, n):
    element = input()
    Football.append(element)  # adding the element
print("Original list of students playing football :" +str(Football))
Football=removeDuplicate(Football)
print("The list of students playing football after removing duplicates : " +str(Football))

# Creating an empty list for Badminton
Badminton = []
n = int(input("\n Enter number of students who play badminton : "))
print("Enter the name of",n,"students who play badminton (Please press ENTER after entering each students name) :")
for i in range(0, n):
    element = input()
    Badminton.append(element)  # adding the element
print("Original list of students playing badminton :" +str(Badminton))
Badminton=removeDuplicate(Badminton)
print("The list of students playing badminton after removing duplicates : " +str(Badminton))

flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        print("Number of students who play both cricket and badminton : ", CB(Cricket,Badminton))
        a = input("\n Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thankyou!")

    elif ch==2:
        print("Number of students who play either cricket or badminton but not both : ", eCeB(Cricket, Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Bye")

    elif ch==3:
        print("Number of students who play neither cricket nor badminton : ", nCnB(SEComp,Cricket,Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thankyou!")

    elif ch==4:
        print("Number of students who play cricket and football but not badminton : ", CBnF(Cricket,Football,Badminton))
        a = input("\n\nDo you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thankyou!")

    elif ch==5:
        flag=0
        print("Thankyou!")

    else:
        print("!!Wrong Choice!! ")
        a=input("\n Do you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thankyou!")