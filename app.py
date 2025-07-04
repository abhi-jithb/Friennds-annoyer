import tkinter as tk
from tkinter import messagebox
import pywhatkit as kit
import time

def send_messages():
    phone = number_entry.get()
    message = message_entry.get("1.0", tk.END).strip()
    try:
        count = int(count_entry.get())
        delay = int(delay_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Count and Delay must be numbers.")
        return

    if not phone or not message or count <= 0 or delay < 0:
        messagebox.showerror("Input Error", "Please fill all fields correctly.")
        return

    for i in range(count):
        try:
            print(f"Sending [{i+1}/{count}]: {message}")
            kit.sendwhatmsg_instantly(
                phone_no=phone,
                message=message,
                wait_time=10,
                tab_close=True
            )
            time.sleep(delay)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
            break

    messagebox.showinfo("Done", f"Sent {count} message(s) to {phone}.")

# GUI Setup
root = tk.Tk()
root.title("WhatsApp Prank App")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Friend's Number (with +91):").pack()
number_entry = tk.Entry(root, width=30)
number_entry.pack()

tk.Label(root, text="Message to Send:").pack()
message_entry = tk.Text(root, height=4, width=30)
message_entry.pack()

tk.Label(root, text="Number of Times:").pack()
count_entry = tk.Entry(root, width=10)
count_entry.pack()

tk.Label(root, text="Delay Between Messages (sec):").pack()
delay_entry = tk.Entry(root, width=10)
delay_entry.pack()

tk.Button(root, text="Start Prank", bg="green", fg="white", command=send_messages).pack(pady=10)

tk.Label(root, text="Note: WhatsApp Web must be open and logged in.").pack(pady=10)

root.mainloop()

