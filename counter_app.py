import tkinter as tk
import time
import pyautogui
from tkinter import messagebox

def start_typing():
    try:
        msg = message_entry.get("1.0", tk.END).strip()
        count = int(count_entry.get())
        delay = float(delay_entry.get())

        if not msg or count <= 0:
            raise ValueError("Invalid inputs")

        messagebox.showinfo("Instructions", "Switch to the chat/text window within 5 seconds!")
        time.sleep(5)  # Time to switch to the WhatsApp Web or Notepad or wherever

        for i in range(count):
            pyautogui.typewrite(msg)
            pyautogui.press("enter")
            time.sleep(delay)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Counter Message App")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Enter message to send:").pack()
message_entry = tk.Text(root, height=4, width=40)
message_entry.pack(pady=5)

tk.Label(root, text="Number of times:").pack()
count_entry = tk.Entry(root, width=10)
count_entry.pack()

tk.Label(root, text="Delay between messages (sec):").pack()
delay_entry = tk.Entry(root, width=10)
delay_entry.insert(0, "0.1")
delay_entry.pack()

tk.Button(root, text="Start Sending", bg="blue", fg="white", command=start_typing).pack(pady=20)
tk.Label(root, text="🧠 Tip: Works in WhatsApp Web, Notepad, Discord, etc.").pack()

root.mainloop()
