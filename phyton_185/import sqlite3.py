import sqlite3
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('data_nilai.db')
cursor = conn.cursor()

# Membuat tabel nilai_siswa jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY,
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )
''')
conn.commit()

# Fungsi untuk menentukan prediksi fakultas berdasarkan nilai
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return 'Kedokteran'
    elif fisika > biologi and fisika > inggris:
        return 'Teknik'
    elif inggris > biologi and inggris > fisika:
        return 'Bahasa'
    else:
        return 'Tidak dapat memprediksi'

# Fungsi untuk menambahkan nilai ke database
def submit_nilai():
    nama_siswa = entry_nama.get()
    
    try:
        nilai_biologi = int(entry_biologi.get())
        nilai_fisika = int(entry_fisika.get())
        nilai_inggris = int(entry_inggris.get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai biologi, fisika, dan inggris dalam bentuk angka.")
        return
    
    # Menggunakan fungsi prediksi_fakultas untuk mendapatkan prediksi sebagai string
    prediksi = prediksi_fakultas(nilai_biologi, nilai_fisika, nilai_inggris)

    # Menambahkan nilai ke database
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi))
    
    conn.commit()

    messagebox.showinfo("Info", "Data siswa berhasil ditambahkan.")

# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Form Nilai Siswa")

label_nama = Label(root, text="Nama Siswa:")
label_nama.grid(row=0, column=0)
entry_nama = Entry(root)
entry_nama.grid(row=0, column=1)

label_biologi = Label(root, text="Nilai Biologi:")
label_biologi.grid(row=1, column=0)
entry_biologi = Entry(root)
entry_biologi.grid(row=1, column=1)

label_fisika = Label(root, text="Nilai Fisika:")
label_fisika.grid(row=2, column=0)
entry_fisika = Entry(root)
entry_fisika.grid(row=2, column=1)

label_inggris = Label(root, text="Nilai Inggris:")
label_inggris.grid(row=3, column=0)
entry_inggris = Entry(root)
entry_inggris.grid(row=3, column=1)

button_submit = Button(root, text="Submit", command=submit_nilai)
button_submit.grid(row=4, column=0, columnspan=2)

root.mainloop()

# Menutup koneksi ke database setelah GUI ditutup
conn.close()
