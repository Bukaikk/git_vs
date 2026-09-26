def add_task(tasks, new_task):  
    tasks.append(new_task)  
    return tasks  

def sort_tasks(tasks):  
    return sorted(tasks, key=lambda x: x['priority'])  
    
def main():
    tasks = []  
       
    new_tasks = [  
        {"title": "Написать отчет", "deadline": "2023-10-15", "priority": 3},  
        {"title": "Купить продукты", "deadline": "2023-10-10", "priority": 1},  
        {"title": "Прочитать книгу", "deadline": "2023-10-20", "priority": 2}  
    ]  
      
    for task in new_tasks:  
        tasks = add_task(tasks, task)  
      
    tasks = sort_tasks(tasks)  
        
    for task in tasks:  
        print(f"Задача: {task['title']}, Дедлайн: {task['deadline']}, Приоритет: {task['priority']}")  
  
if __name__ == "__main__":  
    main()  