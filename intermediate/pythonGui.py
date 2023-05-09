import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
os.system("cls")

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Gerry")

# variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG= tk.StringVar()

def tombol_click():
    pesan = f"halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="gerry",message=pesan)

# frame input
input_frame = ttk.Frame(window)
# penempatan grid,pack,place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen
# 1 label nama depan
nama_depan_label = ttk.Label(input_frame,text="nama depan")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2 entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# 3 label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="nama belakang")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4 entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5 tombol
button = ttk.Button(input_frame,text="Masukan",command=tombol_click)
button.pack(fill="x",expand=True,padx=10,pady=10)

# main loop window
window.mainloop()