import storage
while True:
    try:
        selection = int(input("""Enter selection:
    1. Display the todo list
    2. add a task
    3. delete a task
    4. mark as done
    5. exit
    """))
        if selection == 1:
            print("Here is the todo list.")
            storage.show_list()

        elif selection==2:
            title = input("Enter the title: ")
            date = input("Enter due date(dd/mm): ")
            priority =int(input("Enter priority(1-3): "))
            storage.add_task(title,date,priority)
        
        elif selection==3:
            title = input("Enter the title: ")
            storage.delete_task(title)
        
        elif selection==4:
            title = input("Enter the title: ")
            storage.mark_done(title)
        elif selection == 5:
            print("Thank you.")
            break
    except Exception as e:
        print(e)