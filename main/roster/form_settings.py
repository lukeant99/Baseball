import tkinter as tk
from main.db_connect import create_connection

fields = 'First Name', 'Last Name', 'Position', 'Batting Order'

def fetch(entries):
    player_info = []
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text))
        if not text.strip():
            text = None
        player_info.append(text)
    return player_info

def insert_values(e):
    player_info = fetch(e)
    create_connection(player_info)

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind((lambda event, e=ents: fetch(e)))

    b1 = tk.Button(root, text='Submit', command=(lambda e=ents: insert_values(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)

    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()

