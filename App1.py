import Functions
import time

now = time.strftime("Date: %d-%b-%y      Time: %H:%M:S \n")
print(now)

while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()
    user_action = user_action.capitalize()

    # Note  that in keyword will check string inside of a string
    if user_action.startswith("Add"):

        # string slicing takes string after 4 characters
        user_input = user_action[4:]

        todo_List = Functions.get_todos()

        if len(todo_List) <= 0:
            todo_List.append(user_input + '\n')
        else:
            todo_List.append(user_input)

        Functions.set_todos(todo_List)

    elif user_action.startswith("Show"):

        todo_List = Functions.get_todos()

       # for item in todo_List:
       #     item = item.strip('\n')
        #    new_todo_list.append(item)

        # List Comprehension
        # new_todo_list = [item.strip('\n') for item in todo_List]

        for index,element in enumerate(todo_List):
            element = element.strip('\n')
            print(index + 1, "-", element)

    elif user_action.startswith("Edit"):
        try:
            # string slicing takes string after 5 characters
            number = int(user_action[5:])
            number -= 1

            todo_List = Functions.get_todos()

            if number >= len(todo_List):
                print("Invalid Number Please Enter A Valid Number")
                continue

            new_todo = input("Enter new ToDO: ")

            if(len(todo_List) == 0):
                todo_List[number] = (new_todo)
            else:
                todo_List[number] = (new_todo) + "\n"

            Functions.set_todos(todo_List)
        except ValueError:
            print("Invalid Command Please Enter The Number.")
            continue

    elif user_action.startswith("Complete"):

        try:

            # string slicing takes string after 9 characters
            number = int(user_action[9:])

            todo_List = Functions.get_todos()

            if number > len(todo_List):
                print("Invalid Number Please Enter A Valid Number")
                continue

            item_to_remove = todo_List[number - 1].strip('\n')
            todo_List.pop(number - 1)

            Functions.set_todos(todo_List)

            print(f"{item_to_remove} is removed from the List")


        except ValueError:
            print("Invalid Command Please Enter The Number.")
            continue

    elif user_action.startswith("Exit"):
        break
    else:
        print("Invalid Input")

print("Come on you can do it !!!")