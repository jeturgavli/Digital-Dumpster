from pynput import keyboard
from pynput.keyboard import Controller, Key

keyboard_controller = Controller()

def on_press(key):
    try:
        if key == keyboard.Key.f2:
            # Press and release 
            with keyboard_controller.pressed(Key.ctrl):
                keyboard_controller.press('g')
                keyboard_controller.release('g')
            print("Lalalalal Lalalala :P - JETRock")
    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
