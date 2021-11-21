def fibonacci_number(n):
   
    f = 0
    fibonacci_num = 1
    while n != 0:
        temp = f + fibonacci_num
        f = fibonacci_num
        fibonacci_num = temp
        n -= 1

    return fibonacci_num


class Training:
    

    def __init__(self):
       
        # Accept the roll no. in sorted order
        self.__roll_no_list = str(input("Enter the roll no. of students who attended training in sorted order: "))
        self.__roll_no_list = self.__roll_no_list.split()
        self.__roll_no_list.sort()  # To ensure the roll numbers are in sorted order
        self.__roll_no_list = [int(roll) for roll in self.__roll_no_list]  # Convert str elements to int

    def get_roll_list(self):
        
        return self.__roll_no_list

    def binary_search(self, roll_no):
       
        has_attended_training = False

        roll_list = self.get_roll_list()

        beg = 0
        end = len(roll_list) - 1

        while beg <= end:
            mid = int((beg + end) / 2)
            if roll_list[mid] == roll_no:
                has_attended_training = True
                break
            elif roll_list[mid] > roll_no:
                end = (mid - 1)
            else:
                beg = (mid + 1)

        return has_attended_training

    def fibonacci_search(self, roll_no):
       
        roll_list = self.get_roll_list()
        size = len(roll_list)

        # Find the nth term fibonacci number equal to greater the size of the list
        n = 1
        while fibonacci_number(n) < size:
            n += 1

        f1 = fibonacci_number(n - 2)
        f2 = fibonacci_number(n - 3)
        mid = size - f1 + 1

        while roll_no != roll_list[mid]:
            if mid < 0 or roll_no > roll_list[mid]:  # Check in the left part
                if f1 == 1:
                    return False  # Not found
                # Step back to previous fibonacci number
                mid = mid + f2
                f1 = f1 - f2
                f2 = f2 - f1
            else:  # Check in the right part
                if f2 == 0:
                    return False  # Not found
                mid = mid - f2
                temp = f1 - f2
                f1 = f2
                f2 = temp
        return True


def display_menu():
   
    print("\n=========== Menu ==========")
    print("1. Binary Search")
    print("2. Fibonacci Search")
    print("3. Exit")


def accept_user_choice():
   
    while True:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 3:
            return choice
        else:
            print("Invalid choice! Please enter the valid number")


def accept_roll_to_search():
  
    return int(input("Enter roll no. to search: "))


def display_status(found):
   
    if found:
        print("Student has attended the training")
    else:
        print("Student has NOT attended the training")


def main():
    training = Training()

    while True:
        display_menu()
        choice = accept_user_choice()

        if choice == 1:
            display_status(training.binary_search(accept_roll_to_search()))
        elif choice == 2:
            display_status(training.fibonacci_search(accept_roll_to_search()))
        else:
            break


if __name__ == "__main__":
    main()

