import tkinter as tk

def submit_action():
    print("Submitted!")
    for child in user_info_frame.winfo_children():
        if isinstance(child, tk.Entry):
            print(child.get())

window = tk.Tk()
window.title("Data Entry Form")

frame = tk.Frame(window)
frame.pack(padx=300, pady=300)

user_info_frame = tk.LabelFrame(frame, text="User Information", padx=100, pady=100)
user_info_frame.pack(padx=10, pady=10, fill="both", expand=True)


labels = ["Name", "Email", "Age"]
for i, text in enumerate(labels):
    label = tk.Label(user_info_frame, text=text)
    label.grid(row=i, column=0, sticky="e", padx=5, pady=5)
    entry = tk.Entry(user_info_frame)
    entry.grid(row=i, column=1, padx=5, pady=5)


submit_btn = tk.Button(user_info_frame, text="Submit", command=submit_action)
submit_btn.grid(row=len(labels), columnspan=2, pady=10)

window.mainloop()
