import sqlite3
conn = sqlite3.connect('')# Add the name of your database inside the quotes
cursor = conn.cursor()
### Add SQL to define your table inside the quotes below
cursor.execute('''
                ''')
conn.commit()
conn.close()
# Add the name of your database in the quotes below
print("Database '' created successfully.")