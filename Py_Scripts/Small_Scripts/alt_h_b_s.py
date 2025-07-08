import keyboard

# Control flag
script_running = False
hotkey = None

def press_shortcut():
    if script_running:
        keyboard.press('alt')
        keyboard.press_and_release('h')
        keyboard.press_and_release('b')
        keyboard.press_and_release('s')
        keyboard.release('alt')
        print("✅ Alt+H+B+S pressed.")

def start_script():
    global script_running, hotkey
    if not script_running:
        script_running = True
        hotkey = keyboard.add_hotkey('F3', press_shortcut)
        print("🚀 Script started. Press F3 to trigger Alt+H+B+S.")
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
