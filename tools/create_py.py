import os
import json

def create_python_script(problem_number: int):
    file_path = f"{problem_number}.py"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(
                "import sys\n\n"
                "# Your code here\n\n"
                'if __name__ == "__main__":\n'
                "    # Your code here\n"
                "    pass\n"
            )
        print(f"Python script {file_path} has been created.")
    else:
        print(f"Python script {file_path} already exists.")


def create_c_script(problem_number: int):
    file_path = f"{problem_number}.c"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(
                "#include <stdio.h>\n\n"
                "int main()\n"
                "{\n"
                "    // Your code here\n"
                "    return 0;\n"
                "}\n"
            )
        print(f"C script {file_path} has been created.")
    else:
        print(f"C script {file_path} already exists.")


def create_rust_script(problem_number: int):
    file_path = f"{problem_number}.rs"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(
                "use std::io;\n\n" "fn main()\n" "{\n" "    // Your code here\n" "}\n"
            )
        
        crate = {
            "root_module": file_path,
            "edition": "2021",
            "deps": []
        }
        with open("rust-project.json", "r") as rust_project:
            rust_project_json: dict = json.load(rust_project)
            crates: list = rust_project_json["crates"]
            crates.append(crate)
            with open("rust-project.json", "w") as rust_project:
                json.dump(rust_project_json, rust_project, indent=4)
            
        print(f"Rust script {file_path} has been created.")

    else:
        print(f"Rust script {file_path} already exists.")


if __name__ == "__main__":
    try:
        problem_number = input("Enter the problem number: ")
        selected_language = input("Choose a language (Python/C/Rust): ").lower()

        match selected_language:
            case "python":
                create_python_script(int(problem_number))
            case "c":
                create_c_script(int(problem_number))
            case "rust":
                create_rust_script(int(problem_number))
            case _:
                print("Invalid language. Please choose either Python or C.")

    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
