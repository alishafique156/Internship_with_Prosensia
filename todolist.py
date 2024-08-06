def display_menu():
  print("Welcome to  Todo List Application!")
  print("Choose an option:")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. View Tasks")
  print("4. Exit")

def add_task(tasks):
  task = input("Enter the task you want to add: ")
  tasks.append(task)
  print(f"Task '{task}' added.")

def remove_task(tasks):
  task_num = int(input("Enter the task number to remove: "))
  if 0 < task_num <= len(tasks):
      removed_task = tasks.pop(task_num - 1)
      print(f"Task '{removed_task}' removed.")
  else:
      print("Invalid task number.")

def view_tasks(tasks):
  if not tasks:
      print("Your Todo List is empty.")
  else:
      print("Your Todo List:")
      for i, task in enumerate(tasks, start=1):
          print(f"{i}. {task}")

def main():
  tasks = []
  while True:
      display_menu()
      choice = input("> ")
      if choice == '1':
          add_task(tasks)
      elif choice == '2':
          remove_task(tasks)
      elif choice == '3':
          view_tasks(tasks)
      elif choice == '4':
          print("Exiting the application. Goodbye!")
          break
      else:
          print("Invalid option. Please try again.")

if __name__ == "__main__":
  main()
