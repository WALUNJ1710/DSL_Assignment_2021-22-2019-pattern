class Sort:
    #size of array
    print("Please note that this program is to display\n top five percentage so size must be greater than 5")
    n=int(input("Enter size of array:"))
    arr=[]  
    #Accepting percentage
    for i in range(0,n):
        array_input=float(input("Enter percentage of student:"))
        arr.append(array_input)

    print(arr)
    # For Bubble Sort
    def bubble_sort(self):
        x=Sort.n
        for i in range(0,x):
            for j in range(0,x-i-1):
                if Sort.arr[j]>Sort.arr[j+1]:
                    Sort.arr[j],Sort.arr[j+1]=Sort.arr[j+1],Sort.arr[j]
        print(Sort.arr)
        print("Top five scores are as follows:")
        print(Sort.arr[-1],">",Sort.arr[-2],">",Sort.arr[-3],">",Sort.arr[-4],">",Sort.arr[-5])
    # For Selection Sort      
    def selection_sort(self):
        x=Sort.n
        for i in range(len(Sort.arr)):
            min_n=i
            for j in range(i+1,len(Sort.arr)):
                if min_n>Sort.arr[j]:
                    min_n=j
        Sort.arr[i],Sort.arr[min_n]=Sort.arr[min_n],Sort.arr[i]            
        print(Sort.arr)
        print("Top five scores are as follows:")
        print(Sort.arr[-1],">",Sort.arr[-2],">",Sort.arr[-3],">",Sort.arr[-4],">",Sort.arr[-5])
obj=Sort()

flag=1
while flag:
    print("""*************Menu***************
    1)Bubble sort
    2)Selection sort""")
    choice=int(input("Enter your choice:"))
    if choice==1 :
        print("Array sorted by bubble sort:")
        obj.bubble_sort()
    elif choice==2 :
        print("Array sorted by selection sort:")
        obj.selection_sort()
    e=int(input("Enter 0 to exit or press 1 to go back to menu:"))
    flag=e
