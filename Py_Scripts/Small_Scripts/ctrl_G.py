from pynput import keyboard
from pynput.keyboard import Controller, Key
import threading

keyboard_controller = Controller()
listener = None  # Global listener variable
listener_thread = None
script_running = False

def on_press(key):
    global script_running
    if not script_running:
        return
    try:
        if key == keyboard.Key.f2:
            with keyboard_controller.pressed(Key.ctrl):
                keyboard_controller.press('g')
                keyboard_controller.release('g')
            print("Lalalalal Lalalala :P - JETRock")
    except Exception as e:
        print(f"Error: {e}")

def start_script():
    global script_running, listener, listener_thread
    if script_running:
        print("⚠️ Script already running.")
        return
    script_running = True
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    print("🚀 Script started. Press F2 to trigger Ctrl+G.")

def stop_script():
    global script_running, listener
    if not script_running:
        print("⚠️ Script is not running.")
        return
    script_running = False
    if listener is not None:
        listener.stop()
        listener = None
    print("🛑 Script stopped.")

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
