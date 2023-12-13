import sqlite3
import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("Library Book Catalog")

# Function to add a book to the catalog
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    year = year_entry.get()
    
    # Connect to the database and create the 'books' table if it doesn't exist
    conn = sqlite3.connect('library_catalog.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            isbn TEXT,
            year INTEGER
        )
    ''')

    # Insert the book into the 'books' table
    cursor.execute('INSERT INTO books (title, author, isbn, year) VALUES (?, ?, ?, ?)', (title, author, isbn, year))
    conn.commit()
    
    # Clear the entry fields
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

# Create labels and entry fields for book information
title_label = tk.Label(app, text="Title:")
title_label.grid(row=0, column=0, padx=10, pady=10)
title_entry = tk.Entry(app)
title_entry.grid(row=0, column=1, padx=10, pady=10)

author_label = tk.Label(app, text="Author:")
author_label.grid(row=1, column=0, padx=10, pady=10)
author_entry = tk.Entry(app)
author_entry.grid(row=1, column=1, padx=10, pady=10)

isbn_label = tk.Label(app, text="ISBN:")
isbn_label.grid(row=2, column=0, padx=10, pady=10)
isbn_entry = tk.Entry(app)
isbn_entry.grid(row=2, column=1, padx=10, pady=10)

year_label = tk.Label(app, text="Year:")
year_label.grid(row=3, column=0, padx=10, pady=10)
year_entry = tk.Entry(app)
year_entry.grid(row=3, column=1, padx=10, pady=10)

# Create a button to add a book
add_button = tk.Button(app, text="Add Book", command=add_book)
add_button.grid(row=4, columnspan=2, padx=10, pady=10)

# Connect to the database
conn = sqlite3.connect('library_catalog.db')
cursor = conn.cursor()

# Start the Tkinter main loop
app.mainloop()

# Close the database connection when the GUI is closed
conn.close()
