import os

# Run a simple bash command (list files in current directory)
print("Running command using os.system('ls'):")
os.system("ls") # On Windows, you can use "dir"

import subprocess

# Run a bash command and capture output
print("\nRunning command using subprocess.run():")
result = subprocess.run(["ls", "-l"], capture_output=True, text=True) # use ["dir"] on Windows

# Print the command's output
print("Output:")
print(result.stdout)

# Print any errors (if they occurred)
if result.stderr:
    print("Errors:")
    print(result.stderr)