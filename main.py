import psutil
import time


## Things to work on, make sure that we fix the error handling for both inputs, also figure out how to make the repromted data retrival not just use the same info.
## Also work on making a better terminal usage than can swtich to GUI. tuesday
def main():

    print("Welcome to task manager")
    while True:   
        mem_cpu_list = []
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
            
                    cpu_percent = round(process.cpu_percent(), 2) 	
                    mem_percent = round(process.memory_percent(), 2)
                    mem_cpu_list.append([process.pid, process.name(), mem_percent, cpu_percent])
                    
                except(psutil.AccessDenied, psutil.NoSuchProcess):
                    continue

        
        part_query_selection = input("Would you like to top 10 MEM or CPU? ")

        if part_query_selection.lower().strip() == "m":
            mem_cpu_list = sorted(mem_cpu_list, key = lambda process: process[2], reverse= True) 
            print(" -----  Usage (Sorted Memory usage, DESCENDING) ----- ")
            for entry in mem_cpu_list[:10]:
                print(f"PID: {entry[0]:<7} \t | Name: {entry[1]:<25.22} | Percent Memory Usage: {entry[2]:>5.1f}% \t | Percent CPU Usage: {entry[3]:>5.1f}%")

        elif part_query_selection.lower().strip() == "c":
            mem_cpu_list = sorted(mem_cpu_list, key = lambda process: process[3], reverse= True) 
            print(" -----  Usage (Sorted by CPU usage, DESCENDING) ----- ")
            for entry in mem_cpu_list[:10]:
                print(f"PID: {entry[0]:<7} \t | Name: {entry[1]:<25.22} | Percent Memory Usage: {entry[2]:>5.1f}% \t | Percent CPU Usage: {entry[3]:>5.1f}%")

        else:
            print("Something went wrong")

        rerun = input("Would you like to rerun the program? ")
        if rerun[0].lower() == 'n':
            break
        elif rerun[0].lower() == 'y':
            continue

                
 
if __name__ == "__main__":
    main()
