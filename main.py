""""
from agents.test_case_generator import generate_test_cases
from utils.file_writer import save_to_file

if __name__ == "__main__":
    requirement = input("Enter requirement: ")

    result = generate_test_cases(requirement)

    print("\nGenerated Test Cases:\n")
    print(result)

    save_to_file(result)  """

from agents.test_case_generator import generate_test_cases
from agents.playwright_generator import generate_playwright_script
from utils.file_writer import save_to_file

if __name__ == "__main__":
    print("Select option:")
    print("1. Generate Manual Test Cases")
    print("2. Generate Playwright Automation Script")

    choice = input("Enter choice (1/2): ")
    requirement = input("Enter requirement: ")

    if choice == "1":
        result = generate_test_cases(requirement)
        filename = "output/test_cases.txt"

    elif choice == "2":
         result = generate_playwright_script(requirement)
         filename = "output/playwright_script.ts"

    else:
        print("Invalid choice")
        exit()

    print("\nGenerated Output:\n")
    print(result)
    save_to_file(result, filename)