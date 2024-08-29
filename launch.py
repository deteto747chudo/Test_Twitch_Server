# run_mainsetups.py
import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {script_name}: {e}")

if __name__ == "__main__":
    # Run mainsetup.py
    run_script("mainsetup.py")

    # Run mainsetup2.py
    run_script("mainsetup2.py")
