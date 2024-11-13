import tkinter as tk

def prediksi_prodi():
    # Fungsi ini akan selalu mengembalikan "Teknologi Informasi"
    hasil = "Teknologi Informasi"
    label_hasil.config(text=hasil)

# Membuat jendela utama
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat label judul
label_judul = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack()

# Membuat input nilai mata pelajaran
nilai_pelajaran = []
for i in range(10):
    label = tk.Label(window, text=f"Nilai Mata Pelajaran {i+1}:")
    label.pack()
    entry = tk.Entry(window)
    entry.pack()
    nilai_pelajaran.append(entry)

# Membuat tombol prediksi
button_prediksi = tk.Button(window, text="Hasil Prediksi", command=prediksi_prodi)
button_prediksi.pack()

# Membuat label hasil
label_hasil = tk.Label(window, text="")
label_hasil.pack()

# Menjalankan aplikasi
window.mainloop()