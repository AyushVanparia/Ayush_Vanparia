import subprocess
try:
    completed = subprocess.run(["python", "test.py"],
                               capture_output=True, text=True, check=True)
    print("args", completed.args)
    print("returncode :", completed.returncode)
    print("stderr :", completed.stderr)
    print("stdout :", completed.stdout)
except subprocess.subprocess.CalledProcessError as ex:
    print(ex)
