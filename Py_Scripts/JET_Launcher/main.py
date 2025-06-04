import os

def read_file_paths(file_list_path):
    try:
        with open(file_list_path, 'r', encoding='utf-8') as f:
            paths = [line.strip() for line in f if line.strip()]
        return paths
    except FileNotFoundError:
        print("Oops! 'file_list.txt' is missing. Please create it and add your file paths.")
        return []

def display_menu(paths):
    print("\n=== File Blaster Menu ===")
    for idx, path in enumerate(paths, 1):
        print(f"{idx}. {os.path.basename(path)}")
    print("0. Exit")

def main():
    file_list_path = "file_list.txt"
    paths = read_file_paths(file_list_path)

    if not paths:
        return

    while True:
        display_menu(paths)
        try:
            choice = int(input("\nWhich file would you like to launch? (Enter number): "))
            if choice == 0:
                print("Exiting. Hope you had a fast and fabulous experience!")
                break
            elif 1 <= choice <= len(paths):
                file_path = paths[choice - 1]
                if os.path.exists(file_path):
                    print(f"Launching: {file_path}")
                    os.startfile(file_path)
                else:
                    print("Uh-oh! File not found:", file_path)
            else:
                print("Invalid choice! Try again, champ.")
        except ValueError:
            print("Please enter a valid number. No letters, no symbols – just digits!")

if __name__ == "__main__":
    main()
