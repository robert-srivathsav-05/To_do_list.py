print("--------------To_do_List--------------")
do_list=[]
done_list=[]

def add_tasks():
    while True:
        task=(input("Enter the task to add to your list\n(Enter 'Enough()' to stop adding tasks.):")).title()
        if task=="Enough()":
            break
        elif task.isspace() or len(task)==0:
            print("Enter proper tasks to add to the list.")
        else:
            do_list.append(task)
            
def marked_tasks():
    if len(done_list)==0:
        print("You haven't did any tasks! first add the tasks.")
    else:
        print("The tasks you completed from the list are:")
        for number,Task in enumerate(done_list):
            number+=1
            print(f"{number}.{Task}")            
          
def all_tasks():
    if len(do_list)==0:
        print("You haven't added any tasks to the list!")
    else:
        print("The tasks you have in the to_do_list are:")
        for number,task in enumerate(do_list):
            number+=1
            print(f"{number}.{task}")
      
def completed_tasks():
    if len(do_list)==0:
        print("You haven't added any tasks!")
    else:    
        all_tasks()
        while True:
            completed_task=(input("Enter the task number to mark it as completed.(enter 'Enough()' to end!):")).title()
            if completed_task.isdigit():
                completed_task=int(completed_task)-1
                if completed_task>=0 and completed_task<=len(do_list)-1:
                    if do_list[completed_task] not in done_list:
                            done_list.append(do_list[completed_task])
                            do_list.remove(do_list[completed_task])
                            all_tasks()
                    else:
                        print("Your task has already marked as completed!")
                else:
                    print("Enter the proper task number!")
            elif completed_task=="Enough()":
                marked_tasks()
                break
            else:
                print("Enter a proper number to mark completed or Enough() to end!\nYou entered a wrong input!")

def remove_do_tasks():
    if len(do_list)==0:
        print("Sorry,you can't remove any tasks right now! Add tasks to remove.")
    else:
        while True:
            if len(do_list)==0:
                print("You have deleted all the tasks successfully!")
                break
            else:
                all_tasks()
                remove_task=(input("Enter the task you want to delete from the do list\n(Enter 'Enough()' to exit the removing.):")).title()
                if remove_task.isdigit():
                    remove_task=int(remove_task)-1
                    if remove_task>=0 and remove_task<=len(do_list)-1:
                        do_list.remove(do_list[remove_task])
                    else:
                        print("Enter only the element index within the range!")
                elif remove_task=='Enough()':
                    print("Your updated do list tasks are:")
                    all_tasks()
                    break
                else:
                    print("Enter only numbers! No other inputs!")
                           

def swap_tasks():
    if len(do_list)>1:
        while True:
            all_tasks()
            print("Enter any one of the task input as 'Enough()' to stop swapping.")
            swap_task_1=(input("Enter the task index you want to swap:")).title()
            if swap_task_1!="Enough()":
                swap_task_2=(input("Enter the task index you want to swap with:")).title()
                if swap_task_2!="Enough()":
                    if swap_task_1.isdigit() and swap_task_2.isdigit():
                        swap_task_1=int(swap_task_1)-1
                        swap_task_2=int(swap_task_2)-1
                        if (swap_task_1>=0 and swap_task_1<=len(do_list)-1) and (swap_task_2>=0 and swap_task_2<=len(do_list)-1):
                            do_list[swap_task_1],do_list[swap_task_2]=do_list[swap_task_2],do_list[swap_task_1]
                        else:
                            print("You should enter the index value within the range!")
                    else:
                        print("Enter only numbers")
                else:
                    break        
            else:
                break
    else:
        print("You dont have enough elements to swap🤭🤭!")
            

def clear_tasks():
    while True:
        if len(do_list)!=0 or len(done_list)!=0:
            clear_option=(input("Enter the list you want to delete all the tasks:\n1.do list\n2.done list\n'Both' for clearing two lists\nEnter 'Enough()' to stop:")).title()
            if clear_option=="1":
                if len(do_list)!=0:
                    do_list.clear()
                    print("You have cleared all the tasks in do list successfully!")
                else:
                    print("You already have no elements in the do_list!")
            elif clear_option=="2":
                if len(done_list)!=0:
                    done_list.clear()
                    print("You have cleared all the tasks in done list successfully!")
                else:
                    print("You already cleared all the tasks in done_list!")    
            elif clear_option=="Both":
                if len(do_list)!=0 and len(done_list)!=0:
                    do_list.clear()
                    done_list.clear()
                    print("You have cleared all the tasks in do and done lists!")
                    break
                else:
                    print(f"You can only choose one option!\n Because the no.of tasks in the do_list are {len(do_list)}.\nBecause the no.of tasks in the done_list are {len(done_list)}")
            elif clear_option=="Enough()":
                break 
            else:
                print("Choose from only given options!")
        else:
            print("You have both lists empty!")
            break
                
while True:
    operation=(input("Enter the operation you want to perform:\n1.Add Tasks.\n2.Mark Completed Tasks.\n3.Review the list.\n4.Delete the tasks.\n5.Swap tasks.\n6.Clear tasks\n('Enter 'Exit()' to stop.'):")).title()
    if operation=='1':
        add_tasks()
        all_tasks()
        print("\n")
    elif operation=='2':
        completed_tasks()
    elif operation=='3':
        all_tasks()
        marked_tasks()
    elif operation=='4':
        remove_do_tasks()
    elif operation=='5':
        swap_tasks()
    elif operation=='6':
        clear_tasks()
    elif operation=='Exit()':
        break
    else:
        print("Enter only from given options!")
    
