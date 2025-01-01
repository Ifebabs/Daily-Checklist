# Daily Checklist Generator

from datetime import datetime, timedelta

def get_user_tasks():
    tasks = []
    while True:
        task = input("Enter a task for your daily to-do list (or type 'done' to finish): ")
        if task.lower() == 'done':
            break
        tasks.append(f"- [ ] {task}")
    return tasks

def generate_yearly_checklist(tasks):
    if not tasks:
        return "No tasks given."
    
    start_date = datetime(2025, 1, 1)
    checklist = []
    
    for i in range(365):
        current_date = start_date + timedelta(days=i)
        day = current_date.day
        month = current_date.strftime('%b')
        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        
        checklist.append(f"{month} {day}{suffix}:")
        checklist.extend(tasks)
        checklist.append("")
    
    return "\n".join(checklist)

def main():
    print("Let's create your daily to-do list!")
    tasks = get_user_tasks()
    
    with open('yearly_checklist.md', 'w') as f:
        f.write(generate_yearly_checklist(tasks))
    
    print("Checklist has been created and saved to 'yearly_checklist.md'")

if __name__ == "__main__":
    main()