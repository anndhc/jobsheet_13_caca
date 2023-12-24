

def hitung_kuadrat(angka):
    """Fungsi ini menghitung kuadrat dari suatu angka."""
    return angka ** 2


def tampilkan_pesan(nama):
    """Fungsi ini menampilkan pesan sapaan."""
    pesan = f"Halo, {nama}! Selamat datang di program sederhana."
    print(pesan)


if __name__ == "__main__":
    # Menggunakan fungsi-fungsi yang telah didefinisikan
    angka_input = float(input("Masukkan angka: "))
    hasil_kuadrat = hitung_kuadrat(angka_input)
    tampilkan_pesan("Pengguna")
    print(f"Kuadrat dari {angka_input} adalah {hasil_kuadrat}.")
