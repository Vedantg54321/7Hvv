import subprocess
import time
import psutil

# Join :- @HUNTEROGMOD # Define the command to send to the terminal
command = "echo 'Script stopped, restarting...' && python loop.py"

# Join :- @HUNTEROGMOD # Define the script to monitor
script_to_monitor = "loop.py"

# Join :- @HUNTEROGMOD # Get the process ID of the script to monitor
script_pid = None
for proc in psutil.process_iter():
    try:
        if proc.name() == 'python' and any(script_to_monitor in part for part in proc.cmdline()):
            script_pid = proc.pid
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if script_pid is None:
    print(f"Could not find process for {script_to_monitor}")
    exit()

# Join :- @HUNTEROGMOD # Monitor the script
while True:
    try:
        # Join :- @HUNTEROGMOD # Check if the script is still running
        proc = psutil.Process(script_pid)
        if not proc.is_running():
            # Join :- @HUNTEROGMOD # If the script is not running, send the command to the terminal
            subprocess.run(command, shell=True)

            # Join :- @HUNTEROGMOD # Wait for 10 seconds before checking again
            time.sleep(10)

            # Join :- @HUNTEROGMOD # Get the new process ID of the script
            script_pid = None
            for proc in psutil.process_iter():
                try:
                    if proc.name() == 'python' and any(script_to_monitor in part for part in proc.cmdline()):
                        script_pid = proc.pid
                        break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            if script_pid is None:
                print(f"Could not find process for {script_to_monitor}")
                exit()
    except psutil.NoSuchProcess:
        # Join :- @HUNTEROGMOD # If the script process does not exist, send the command to the terminal
        subprocess.run(command, shell=True)

        # Join :- @HUNTEROGMOD # Wait for 10 seconds before checking again
        time.sleep(10)

        # Join :- @HUNTEROGMOD # Get the new process ID of the script
        script_pid = None
        for proc in psutil.process_iter():
            try:
                if proc.name() == 'python' and any(script_to_monitor in part for part in proc.cmdline()):
                    script_pid = proc.pid
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        if script_pid is None:
            print(f"Could not find process for {script_to_monitor}")
            exit()