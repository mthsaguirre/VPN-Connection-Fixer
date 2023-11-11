import subprocess
import time

commands = [
    'ipconfig/release',
    'ipconfig/flushdns',
    'ipconfig/renew',
    'netsh int ip set dns',
    'netsh winsock reset',
    'shutdown /s'
]

for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Command '{command}' executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")

    time.sleep(1)

print("All commands executed successfully!")