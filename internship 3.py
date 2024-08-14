import tkinter as tk
from tkinter import messagebox, scrolledtext
import lyricsgenius

# Replace 'your_genius_api_token' with your actual Genius API token
genius = lyricsgenius.Genius("your_genius_api_token")

# Function to fetch lyrics
def fetch_lyrics():
    song_title = title_entry.get()
    artist_name = artist_entry.get()
    
    if not song_title or not artist_name:
        messagebox.showerror("Error", "Please enter both song title and artist name")
        return
    
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics_display.config(state=tk.NORMAL)
            lyrics_display.delete(1.0, tk.END)
            lyrics_display.insert(tk.END, song.lyrics)
            lyrics_display.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Lyrics not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("Lyrics Extractor")
root.geometry("500x600")

# Create labels and entry widgets for song title and artist name
title_label = tk.Label(root, text="Song Title")
title_label.pack(pady=5)
title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=5)

artist_label = tk.Label(root, text="Artist Name")
artist_label.pack(pady=5)
artist_entry = tk.Entry(root, width=50)
artist_entry.pack(pady=5)

# Create a button to fetch lyrics
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.pack(pady=10)

# Create a scrolled text widget to display the lyrics
lyrics_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=60, height=25)
lyrics_display.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
