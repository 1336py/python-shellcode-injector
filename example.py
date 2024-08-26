from injector import Injector

# Simple tkinter window to inject into the process
code = """
import tkinter as tk

window = tk.Tk()

window.title("https://discord.gg/XMzm26Z9SV")

label = tk.Label(window, text="Python is so ud")
label.pack(padx=20, pady=20)

window.mainloop()

"""


if __name__ == "__main__":
    process_name = "Notepad.exe"  # Injecting into notepad for this example
    injector = Injector(process_name)
    
    injector.inject(code)
