import sqlite3

def create_connection(player_info):
    try:
        conn = sqlite3.connect("O:\\backup\\practice_code\\db\\practice_code.db")
        c = conn.cursor()

        c.execute('''INSERT INTO Player_Info (FirstName, LastName, Position, BattingOrder) VALUES (?, ?, ?, ?)''',
                  (player_info[0], player_info[1], player_info[2], player_info[3]))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError as e:
            print('sqlite error: ', e.args[0])


