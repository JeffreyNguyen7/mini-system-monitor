import psutil

def main():
    print("Welcome to task manager")
    mem_list = []
    
    for process in psutil.process_iter():
        try:
            mem_object = process.memory_info()
            mem_percent = round(process.memory_percent(), 2)
            mem_info = round( mem_object.rss / 1000000, 2)
            
            mem_list.append([process.pid, process.name(), mem_percent])
            
            
        except(psutil.AccessDenied, psutil.NoSuchProcess):
            continue

    mem_list = sorted(mem_list, key = lambda process: process[2], reverse= True) 

    for entry in mem_list[:10]:

        print(f"PID: {entry[0]} | Name: {entry[1]} | Percent Memory Usage: {entry[2]}%")

 
if __name__ == "__main__":
    main()
