# from function import get_todos, write_todos
import function
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add,show,edit,completed or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = function.get_todos()

        todos.append(todo + "\n" )

        function.write_todos(todos)

    elif user_action.startswith("show"):

        todos = function.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            numbering = f"{index + 1}-{item}"
            print(numbering)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = function.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            function.write_todos(todos)
        except ValueError:
            print("Your command is invalid.")
            continue

    elif user_action.startswith("completed"):
        try:

            number = int(input(user_action[11:]))

            todos = function.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            function.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("The is no item of that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is invalid, kindly enter again: ")
print("Bye :) ")
