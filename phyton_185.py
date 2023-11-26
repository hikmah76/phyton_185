import sqlite3
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('data_nilai.db')
cursor = conn.cursor()

# Hapus tabel jika sudah ada
cursor.execute('''DROP TABLE IF EXISTS nilai_siswa''')

# Membuat tabel nilai_siswa
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY,
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        matematika INTEGER,
        kimia INTEGER,
        ekonomi INTEGER,
        geografi INTEGER,
        sosiologi INTEGER,
        seni INTEGER,
        bahasa_indonesia INTEGER,
        bahasa_inggris INTEGER,
        prediksi_fakultas TEXT
    )
''')
conn.commit()

# Fungsi untuk menentukan prediksi fakultas berdasarkan nilai
def prediksi_fakultas(biologi, fisika, inggris, matematika, kimia, ekonomi, geografi, sosiologi, seni, bahasa_indonesia, bahasa_inggris):
    total_nilai = biologi + fisika + inggris + matematika + kimia + ekonomi + geografi + sosiologi + seni + bahasa_indonesia + bahasa_inggris
    rata_rata = total_nilai / 11

    if rata_rata >= 90:
        return 'Kedokteran'
    elif rata_rata >= 80:
        return 'Teknik'
    elif rata_rata >= 70:
        return 'Bahasa'
    else:
        return 'Tidak dapat memprediksi'

# Fungsi untuk menampilkan hasil prediksi fakultas
def tampilkan_hasil_prediksi():
    try:
        nilai_biologi = int(entry_vars['biologi'].get())
        nilai_fisika = int(entry_vars['fisika'].get())
        nilai_inggris = int(entry_vars['inggris'].get())
        nilai_matematika = int(entry_vars['matematika'].get())
        nilai_kimia = int(entry_vars['kimia'].get())
        nilai_ekonomi = int(entry_vars['ekonomi'].get())
        nilai_geografi = int(entry_vars['geografi'].get())
        nilai_sosiologi = int(entry_vars['sosiologi'].get())
        nilai_seni = int(entry_vars['seni'].get())
        nilai_bahasa_indonesia = int(entry_vars['bahasa_indonesia'].get())
        nilai_bahasa_inggris = int(entry_vars['bahasa_inggris'].get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai dalam bentuk angka.")
        return
    
    # Menggunakan fungsi prediksi_fakultas untuk mendapatkan prediksi sebagai string
    prediksi = prediksi_fakultas(
        nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia,
        nilai_ekonomi, nilai_geografi, nilai_sosiologi, nilai_seni,
        nilai_bahasa_indonesia, nilai_bahasa_inggris
    )

    # Menampilkan hasil prediksi
    if "Kedokteran" in prediksi:
        hasil_prediksi = "Jika nilai Biologi paling tinggi, maka hasil prediksi = Kedokteran"
    elif "Teknik" in prediksi:
        hasil_prediksi = "Jika nilai Fisika paling tinggi, maka hasil prediksi = Teknik"
    elif "Ekonomi" in prediksi:
        hasil_prediksi = "Jika nilai Ekonomi paling tinggi, maka hasil prediksi = Ekonomi"
    else:
        hasil_prediksi = "Tidak dapat memprediksi"

    messagebox.showinfo("Info", f"Hasil Prediksi Fakultas:\n{hasil_prediksi}")

# Fungsi untuk menambahkan nilai ke database
def submit_nilai():
    nama_siswa = entry_nama.get()
    
    try:
        nilai_biologi = int(entry_vars['biologi'].get())
        nilai_fisika = int(entry_vars['fisika'].get())
        nilai_inggris = int(entry_vars['inggris'].get())
        nilai_matematika = int(entry_vars['matematika'].get())
        nilai_kimia = int(entry_vars['kimia'].get())
        nilai_ekonomi = int(entry_vars['ekonomi'].get())
        nilai_geografi = int(entry_vars['geografi'].get())
        nilai_sosiologi = int(entry_vars['sosiologi'].get())
        nilai_seni = int(entry_vars['seni'].get())
        nilai_bahasa_indonesia = int(entry_vars['bahasa_indonesia'].get())
        nilai_bahasa_inggris = int(entry_vars['bahasa_inggris'].get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai dalam bentuk angka.")
        return
    
    # Menggunakan fungsi prediksi_fakultas untuk mendapatkan prediksi sebagai string
    prediksi = prediksi_fakultas(
        nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia,
        nilai_ekonomi, nilai_geografi, nilai_sosiologi, nilai_seni,
        nilai_bahasa_indonesia, nilai_bahasa_inggris
    )

    # Menambahkan nilai ke database
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, matematika, kimia, ekonomi, 
                                 geografi, sosiologi, seni, bahasa_indonesia, bahasa_inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia,
          nilai_ekonomi, nilai_geografi, nilai_sosiologi, nilai_seni, nilai_bahasa_indonesia, nilai_bahasa_inggris, prediksi))
    
    conn.commit()

    # Menampilkan hasil prediksi
    if "Kedokteran" in prediksi:
        hasil_prediksi = "Jika nilai Biologi paling tinggi, maka hasil prediksi = Kedokteran"
    elif "Teknik" in prediksi:
        hasil_prediksi = "Jika nilai Fisika paling tinggi, maka hasil prediksi = Teknik"
    elif "Ekonomi" in prediksi:
                hasil_prediksi = "Jika nilai Ekonomi paling tinggi, maka hasil prediksi = Ekonomi"
    else:
        hasil_prediksi = "Tidak dapat memprediksi"

    messagebox.showinfo("Info", f"Data siswa berhasil ditambahkan.\n{hasil_prediksi}")

# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Form Nilai Siswa")

# Entry for Nama Siswa
label_nama = Label(root, text="Nama Siswa:")
label_nama.grid(row=0, column=0)
entry_nama = Entry(root)
entry_nama.grid(row=0, column=1)

# Label and Entry widgets for each subject
subjects = [
    "Biologi", "Fisika", "Inggris", "Matematika", "Kimia", "Ekonomi",
    "Geografi", "Sosiologi", "Seni", "Bahasa Indonesia", "Bahasa Inggris"
]

# Dictionary to store entry variables
entry_vars = {}

# Create labels and entry widgets dynamically
for i, subject in enumerate(subjects):
    label = Label(root, text=f"Nilai {subject}:")
    label.grid(row=i + 1, column=0)

    entry_var = tk.IntVar()
    entry = Entry(root, textvariable=entry_var)
    entry.grid(row=i + 1, column=1)

    entry_vars[subject.lower().replace(" ", "_")] = entry_var

# Button to submit data
button_submit = Button(root, text="Submit", command=submit_nilai)
button_submit.grid(row=len(subjects) + 2, column=0, columnspan=2)

# Button to show prediction
button_prediksi = Button(root, text="Tampilkan Prediksi", command=tampilkan_hasil_prediksi)
button_prediksi.grid(row=len(subjects) + 3, column=0, columnspan=2)

root.mainloop()

# Menutup koneksi ke database setelah GUI ditutup
conn.close()
