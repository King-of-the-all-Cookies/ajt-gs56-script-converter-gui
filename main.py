# gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from main1 import encode, decode  # Importing encode and decode functions
import traceback


class GS56App:
    def __init__(self, master):
        self.master = master
        master.title("GS56 Encoder/Decoder")

        self.label = tk.Label(master, text="Choose a file to encode or decode:")
        self.label.pack(pady=10)

        self.file_path = tk.StringVar()
        self.file_entry = tk.Entry(master, textvariable=self.file_path, width=50)
        self.file_entry.pack(pady=5)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)

        self.encode_button = tk.Button(master, text="Encode", command=self.encode_file)
        self.encode_button.pack(pady=5)

        self.decode_button = tk.Button(master, text="Decode", command=self.decode_file)
        self.decode_button.pack(pady=5)

    def browse_file(self):
        filename = filedialog.askopenfilename(title="Select a file",
                                              filetypes=(("All Files", "*.*"),))
        if filename:
            self.file_path.set(filename)

    def encode_file(self):
        try:
            file_path = self.file_path.get()
            if not file_path:
                raise ValueError("No file selected.")
            with open(file_path, 'rb') as f:
                encode(f)
            messagebox.showinfo("Success", "File encoded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error encoding file:\n{traceback.format_exc()}")

    def decode_file(self):
        try:
            file_path = self.file_path.get()
            if not file_path:
                raise ValueError("No file selected.")
            with open(file_path, 'rb') as f:
                decode(f)
            messagebox.showinfo("Success", "File decoded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error decoding file:\n{traceback.format_exc()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GS56App(root)
    root.mainloop()