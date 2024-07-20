# Creating a list of tasks
tasks = ["Complete report", "Send emails", "Attend meeting", "Prepare presentation", "Follow up with clients"]

# Creating an iterator
task_iterator = iter(tasks)
#print(task_iterator.__next__())
print (next(task_iterator))
# Iterating through the tasks using a loop
print("Tasks for the day:")
try:
    while True:
        next_task = next(task_iterator)
        print("- " + next_task)
except StopIteration:
    pass

# Output:
# Tasks for the day:
# - Complete report
# - Send emails
# - Attend meeting
# - Prepare presentation
# - Follow up with clients
