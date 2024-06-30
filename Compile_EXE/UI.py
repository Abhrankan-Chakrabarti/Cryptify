import os
import tkinter as tk
from tkinter import filedialog, messagebox
from sys import argv
from PIL import Image, ImageTk

def choose_path(a):
    root = tk.Tk()
    root.withdraw()
    password1 = ""
    password2 = ""
    if a == 1 or a == 2:
        filepath = filedialog.askopenfilename()
        password_window = tk.Toplevel(root)
        password_window.geometry("300x200")
        password_window.title("Password")
        password_window.iconbitmap("logo.ico")
        password_window.resizable(False, False)
        
        # Load the image and create a label with the image
        image = Image.open("password_chooser_bg.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(password_window, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Define the hover color
        hover_color = "#C81C68"

        # Create the password and confirm password fields with rounded corners
        password_entry1 = tk.Entry(password_window, show="*", font=("Sora", 10), highlightthickness=0, bd=0, borderwidth=0)
        password_entry1.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.1)

        password_entry2 = tk.Entry(password_window, show="*", font=("Sora", 10), highlightthickness=0, bd=0, borderwidth=0)
        password_entry2.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.1)

        # Create the submit button with rounded corners
        submit_button = tk.Button(password_window, text="Submit", fg="white", bg="#6A0B2E", font=("Sora", 14),
                                highlightthickness=0, bd=0, borderwidth=0,
                                padx=20, pady=10, command=lambda: password_confirm())
        submit_button.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.2)
        submit_button.bind("<Enter>", lambda event: submit_button.config(bg=hover_color))
        submit_button.bind("<Leave>", lambda event: submit_button.config(bg="#6A0B2E"))
        
        def password_confirm():
            nonlocal password1, password2
            password1 = password_entry1.get()
            password2 = password_entry2.get()
            if password1 == password2:
                password_window.destroy()
                root.quit()
            else:
                messagebox.showerror("Error", "Passwords do not match.")
    elif a == 3:
        folderpath = filedialog.askdirectory()
        password_window = tk.Toplevel(root)
        password_window.geometry("300x200")
        password_window.title("Password")
        password_window.iconbitmap("logo.ico")
        password_window.resizable(False, False)
        
        # Load the image and create a label with the image
        image = Image.open("password_chooser_bg.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(password_window, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Define the hover color
        hover_color = "#C81C68"

        # Create the password and confirm password fields with rounded corners
        password_entry1 = tk.Entry(password_window, show="*", font=("Sora", 10), highlightthickness=0, bd=0, borderwidth=0)
        password_entry1.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.1)

        password_entry2 = tk.Entry(password_window, show="*", font=("Sora", 10), highlightthickness=0, bd=0, borderwidth=0)
        password_entry2.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.1)

        # Create the submit button with rounded corners
        submit_button = tk.Button(password_window, text="Submit", fg="white", bg="#6A0B2E", font=("Sora", 14),
                                highlightthickness=0, bd=0, borderwidth=0,
                                padx=20, pady=10, command=lambda: password_confirm())
        submit_button.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.2)
        submit_button.bind("<Enter>", lambda event: submit_button.config(bg=hover_color))
        submit_button.bind("<Leave>", lambda event: submit_button.config(bg="#6A0B2E"))
        
        def password_confirm():
            nonlocal password1, password2
            password1 = password_entry1.get()
            password2 = password_entry2.get()
            if password1 == password2:
                password_window.destroy()
                root.quit()
            else:
                messagebox.showerror("Error", "Passwords do not match.")
    elif a == 4:
        filepath = filedialog.askopenfilename()
        password_window = tk.Toplevel(root)
        password_window.geometry("300x200")
        password_window.title("Password")
        password_window.iconbitmap("logo.ico")
        password_window.resizable(False, False)
        
        # Load the image and create a label with the image
        image = Image.open("password_chooser_bg.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(password_window, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Define the hover color
        hover_color = "#C81C68"

        # Create the password and confirm password fields with rounded corners
        password_entry1 = tk.Entry(password_window, show="*", font=("Sora", 10), highlightthickness=0, bd=0, borderwidth=0)
        password_entry1.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.1)

        password_entry2 = tk.Entry(password_window, show="*", font=("Sora", 10), highlightthickness=0, bd=0, borderwidth=0)
        password_entry2.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.1)

        # Create the submit button with rounded corners
        submit_button = tk.Button(password_window, text="Submit", fg="white", bg="#6A0B2E", font=("Sora", 14),
                                highlightthickness=0, bd=0, borderwidth=0,
                                padx=20, pady=10, command=lambda: password_confirm())
        submit_button.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.2)
        submit_button.bind("<Enter>", lambda event: submit_button.config(bg=hover_color))
        submit_button.bind("<Leave>", lambda event: submit_button.config(bg="#6A0B2E"))
        
        def password_confirm():
            nonlocal password1, password2
            password1 = password_entry1.get()
            password2 = password_entry2.get()
            if password1 == password2:
                password_window.destroy()
                root.quit()
            else:
                messagebox.showerror("Error", "Passwords do not match.")
    elif a == 5 or a == 6:
        drives = ["%s:" % d for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists("%s:" % d)]
        if not drives:
            messagebox.showerror("Error", "No drives found.")
        else:
            drive_window = tk.Toplevel(root)
            drive_window.title("Choose Drive")

            drive_window.geometry("300x200")
            drive_window.iconbitmap("logo.ico")
            drive_window.resizable(False, False)

            # Place empty button for padding
            tk.Button(drive_window).grid(row=0, column=1)
            tk.Button(drive_window).grid(row=1, column=1)
            tk.Button(drive_window).grid(row=2, column=1)

            # Load the image and create a label with the image
            image = Image.open("bg2.png")
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(drive_window, image=photo)
            label.place(x=0, y=0, relwidth=1, relheight=1)

            # Hover effect
            def on_enter(event):
                event.widget.config(bg=hover_color)

            def on_leave(event):
                event.widget.config(bg="#6A0B2E")

            # Define the hover color
            hover_color = "#C81C68"
            selected_drive = None
            for i, drive in enumerate(drives):
                if i < 5:
                    btn = tk.Button(drive_window, text=drive, fg="white", bg="#6A0B2E", font=("Sora", 14),
                                    highlightthickness=0, bd=0, borderwidth=0, padx=20, pady=10, command=lambda x=drive: drive_selected(x))
                    btn.grid(row=3, column=i)
                else:
                    btn = tk.Button(drive_window, text=drive, fg="white", bg="#6A0B2E", font=("Sora", 14),
                                highlightthickness=0, bd=0, borderwidth=0, padx=20, pady=10, command=lambda x=drive: drive_selected(x))
                    btn.grid(row=4, column=i - 5)
                btn.bind("<Enter>", on_enter)
                btn.bind("<Leave>", on_leave)

            def drive_selected(drive):
                nonlocal selected_drive
                selected_drive = drive
                drive_window.destroy()
                root.quit()
    elif a == 7 or a == 8:
        filepath = "None"
        password_window = tk.Toplevel(root)
        password_window.geometry("300x200")
        password_window.title("Password")
        password_window.iconbitmap("logo.ico")
        password_window.resizable(False, False)
        
        # Load the image and create a label with the image
        image = Image.open("password_chooser_bg.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(password_window, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Define the hover color
        hover_color = "#C81C68"

        # Create the password and confirm password fields with rounded corners
        password_entry1 = tk.Entry(password_window, show="*", font=("Sora", 10), highlightthickness=0, bd=0, borderwidth=0)
        password_entry1.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.1)

        password_entry2 = tk.Entry(password_window, show="*", font=("Sora", 10), highlightthickness=0, bd=0, borderwidth=0)
        password_entry2.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.1)

        # Create the submit button with rounded corners
        submit_button = tk.Button(password_window, text="Submit", fg="white", bg="#6A0B2E", font=("Sora", 14),
                                highlightthickness=0, bd=0, borderwidth=0,
                                padx=20, pady=10, command=lambda: password_confirm())
        submit_button.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.2)
        submit_button.bind("<Enter>", lambda event: submit_button.config(bg=hover_color))
        submit_button.bind("<Leave>", lambda event: submit_button.config(bg="#6A0B2E"))
        
        def password_confirm():
            nonlocal password1, password2
            password1 = password_entry1.get()
            password2 = password_entry2.get()
            if password1 == password2:
                password_window.destroy()
                root.quit()
            else:
                messagebox.showerror("Error", "Passwords do not match.")

    root.mainloop()
    return a, filepath if a == 1 or a == 2 or a == 4 or a == 7 or a == 8 else folderpath if a == 3 else selected_drive[0:1], 'None' if a == 5 or a == 6 else password1

result = choose_path(int(argv[1]))
path = result[1].replace(' ','$')

os.system('start main.exe '+ str(result[0]) + ' '+ path.replace("/","\\") + ' '+ result[2])