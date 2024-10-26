from database import Entry, create_connection, setup_database

conn = create_connection()
setup_database(conn)
# ! Define drone temperature
entry = Entry(max_height=25, temperature=25, speed=25, duration=25)
entry.insert(conn)
conn.close()