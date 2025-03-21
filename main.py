import subprocess

def run_script(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"{script_name} completed successfully.")
    else:
        print(f"Error occurred in {script_name}:\n{result.stderr}")
    print("-" * 40)

def main():
    run_script("spiraleclipSPACINGEQUALPOINT.py")
    run_script("3dmodelwrappy.py")
    run_script("3dcsvplot.py")

if __name__ == "__main__":
    main()
