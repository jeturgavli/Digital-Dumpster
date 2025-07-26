import keyboard
from pynput.mouse import Controller, Button

# Mouse controller
mouse = Controller()

# Control flag
script_running = False
hotkey = None

def press_shortcut():
    if script_running:
        mouse.click(Button.left, 1)  # Left click once
        print("🖱️ Mouse clicked.")

def start_script():
    global script_running, hotkey
    if not script_running:
        script_running = True
        hotkey = keyboard.add_hotkey('F2', press_shortcut)
        print("🚀 Script started. Press F2 to click the mouse.")
    else:
        print("⚠️ Script is already running.")

def stop_script():
    global script_running, hotkey
    if script_running:
        keyboard.remove_hotkey(hotkey)
        script_running = False
        hotkey = None
        print("🛑 Script stopped.")
    else:
        print("⚠️ Script is not running yet.")

def menu():
    while True:
        print("\n📜 MENU")
        print("1. Start Script")
        print("2. Stop Script")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_script()
        elif choice == '2':
            stop_script()
        elif choice == '3':
            stop_script()
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the menu
menu()
