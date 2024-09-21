import os

def create_python_script(problem_number: int):
    file_path = f"{problem_number}.py"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(
                f"import sys\n\n"
                f"# Your code here\n\n"
                f"if __name__ == \"__main__\":\n"
                f"    # Your code here\n"
                f"    pass\n"
            )
        print(f"Python script {file_path} has been created.")


if __name__ == "__main__":
    try:
        problem_number = input("Enter the problem number: ")
        create_python_script(int(problem_number))
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)