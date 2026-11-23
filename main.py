import psutil
import time

def main():
    print("Welcome to task manager")
    mem_list = []
    cpu_list = []
    process_list = []
    
    for process in psutil.process_iter():
        try:
            process.cpu_percent(interval=None)
            process_list.append(process)
        except(psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    time.sleep(1)

    

    for process in process_list:
        try:
         #  mem_object = process.memory_info()
         #  mem_info = round( mem_object.rss / 1000000, 2)
            cpu_percent = round(process.cpu_percent(), 2)
            cpu_list.append([process.pid, process.name(), cpu_percent])
         	
            mem_percent = round(process.memory_percent(), 2)
            mem_list.append([process.pid, process.name(), mem_percent])
            
        except(psutil.AccessDenied, psutil.NoSuchProcess):
            continue

    mem_list = sorted(mem_list, key = lambda process: process[2], reverse= True) 
    cpu_list = sorted(cpu_list, key = lambda process: process[2], reverse= True) 

    for entry in mem_list[:10]:
        print(f"PID: {entry[0]} | Name: {entry[1]} | Percent Memory Usage: {entry[2]}%")

    print("\n")

    for entry in cpu_list[:10]:
        print(f"PID: {entry[0]} | Name: {entry[1]} | Percent CPU Usage: {entry[2]}%")
 
if __name__ == "__main__":
    main()
