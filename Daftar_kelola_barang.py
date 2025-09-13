
print(f"""
#############################################################################################
#     Nama         = Antonio marc laureno silaban                                           #
#     NIM          = 2509116040                                                             #     
#     Kelas        = Sistem Iformasi A                                                      #
#     Mini Project = Sistem pengelolaan barang-barang kamar laki-laki remaja                #
#############################################################################################

""")
print("~" * 200)




List_barang = ["Baju", "Celana", "Sepatu", "Kasur", "Ransel", "Meja", "Kursi"]
Barang = """
Baju    = 0
Celana  = 1
Sepatu  = 2
Kasur   = 3
Ransel  = 4
Meja    = 5
Kursi   = 6
"""

print(Barang)
print("""
Barang awal ada 7 berformat dari 0-6

Berikut Perintah yang bisa anda gunakan""")
List_Perintah = """
Masukkan barang                     = 1
Sisipkan barang                     = 2
Mengganti barang                    = 3
Mengganti 2 barang sekaligus        = 4
Membuang barang berdasarkan nama    = 5
Membuang barang berdasarkan urutan  = 6
"""
print(List_Perintah)

print("~" * 200)

Perintah = int(input("Apa yang ingin kamu lakukan? "))


if Perintah == 1:
        Tindakan = input("barang apa yang ingin anda tambahkan: ")
        List_barang.append(Tindakan)
        print(f"anda telah menambahkan {Tindakan}")
elif Perintah == 2:
        Tindakan_2 = int(input("pada urutan keberapa anda ingin menyisipkan barang: "))
        Tindakan_22 = input("masukkan nama barang yang ingin anda sisipkan: ")
        List_barang.insert(Tindakan_2, Tindakan_22)
        print(f"anda telah menyisipkan barang pada urutan {Tindakan_2} yaitu {Tindakan_22}")
elif Perintah == 3:
        Tindakan_3 = int(input("urutan keberapa barang yang ingin anda ganti: "))
        Tindakan_33 = input("masukkan nama barang untuk menggantikannya: ")
        List_barang[Tindakan_3] = Tindakan_33
        print(f"anda telah menganti barang pada urutan {Tindakan_3} dengan {Tindakan_33}")
elif Perintah == 4:
        Tindakan_4 = int(input("urutan keberapa barang pertama yang ingin anda ganti: "))
        Tindakan_4_kedua = int(input("urutan keberapa barang kedua yang ingin anda ganti: "))
        Tindakan_44 = input("masukkan nama barang pertama untuk menggantikannya: ")
        Tindakan_44_kedua = input("masukkan nama barang kedua untuk menggantikannya: ")
        List_barang[Tindakan_4:Tindakan_4_kedua] = [Tindakan_44,Tindakan_44_kedua]
        print(f"anda telah mengganti barang pada urutan {Tindakan_4} dan {Tindakan_4_kedua} dengan")
        print(f"{Tindakan_44} dan {Tindakan_44_kedua}")
elif Perintah == 5:
        Tindakan_5 = input("Barang apa yang ingin anda buang? ")
        List_barang.remove(Tindakan_5)
        print(f"anda telah membuang {Tindakan_5}")
elif Perintah == 6:
        Tindakan_5 = int(input("Pada urutan keberapa barang yang ingin anda buang? "))
        del List_barang[Tindakan_5]
        print(f"anda telah membuang {Tindakan_5}")
else:
        print("Permintaan anda tidak kami pahami")

        print("Barang tidak mengalami perubahan")

print(List_barang)

print("~" * 200)