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
    else:
        print(f"Python script {file_path} already exists.")

def create_c_script(problem_number: int):
    file_path = f"{problem_number}.c"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(
                f"#include <stdio.h>\n\n"
                f"int main()\n"
                "{\n"
                "    // Your code here\n"
                "    return 0;\n"
                "}\n"
            )
        print(f"C script {file_path} has been created.")
    else:
        print(f"C script {file_path} already exists.")

if __name__ == "__main__":
    try:
        problem_number = input("Enter the problem number: ")
        selected_language = input("Choose a language (Python/C): ").lower()

        if selected_language == "python":
            create_python_script(int(problem_number))
        elif selected_language == "c":
            create_c_script(int(problem_number))
        else:
            print("Invalid language. Please choose either Python or C.")
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)