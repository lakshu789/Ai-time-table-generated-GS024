

# ---------- Databasimport tkinter as tk
# from tkinter import messagebox
# import sqlite3e Setup ----------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL UNIQUE,password TEXT NOT NULL
""")
conn.commit()

# ---------- Register Sample User ----------
# Run once to create a default user: username = admin, password = 1234
try:
    cursor.execute("INSERT INTO users(username, password) VALUES (?, ?)", ("admin", "1234"))
    conn.commit()
except:
    pass  # If user already exists, ignore

# ---------- Login Function ----------
def login():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login Success", f"Welcome {username}!")
        root.destroy()
        # Here you can call timetable app window
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ---------- Main GUI ----------
root = tk.Tk()
root.title("AI Timetable Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()

# ---------- Close Database ----------
conn.close()

