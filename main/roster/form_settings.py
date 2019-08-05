import tkinter as tk
from tkinter import messagebox
from main.db_connect import insert_player_info

fields = 'First Name', 'Last Name', 'Position', 'Batting Order'

def fetch(entries):
    player_info = []
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()

        print('%s: "%s"' % (field, text))

        # If it's an empty string set it to None for database purposes
        if not text.strip():
            text = None

        if field == 'Batting Order':
            try:
                text = int(text)
            except ValueError:
                print("Must enter integer value")
                messagebox.showerror("Error", "Must enter integer value in Batting Order")

        player_info.append(text)

    clear_entries(entries)
    return player_info

def clear_entries(entries):
    for entry in entries:
        entry[1].delete(0, 'end')

def insert_values(e):
    player_info = fetch(e)
    insert_player_info(player_info)

def makeform(root, fields):
    entries = []

    header_row = tk.Frame(root)
    header_label = tk.Label(header_row, width=30, text="Enter Player Information", fg="blue", font=("Arial", 12))
    header_label.pack(side=tk.LEFT)
    header_row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=3)

    for field in fields:
        row = tk.Frame(root)
        label = tk.Label(row, width=12, text=field, anchor='w')
        entry = tk.Entry(row, width=30)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=3)
        label.pack(side=tk.LEFT)
        entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        entries.append((field, entry))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Player Info')

    ents = makeform(root, fields)
    root.bind((lambda event, e=ents: fetch(e)))

    b1 = tk.Button(root, text='Submit', command=(lambda e=ents: insert_values(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)

    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()

