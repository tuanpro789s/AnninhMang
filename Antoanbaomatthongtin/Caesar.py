def mahoacaesar(dulieubandau, khoa):
    dulieumahoa = ""
    for kytu in dulieubandau:
        if kytu.isalpha():
            dich = ord("A") if kytu.isupper() else ord("a")
            dulieumahoa += chr((ord(kytu) - dich + khoa) % 26 + dich)
        else:
            dulieumahoa += kytu
    return dulieumahoa

def giaimacaesar(dulieumahoa, khoa):
    return mahoacaesar(dulieumahoa, -khoa)

def phamacaesar(dulieumahoa):
    for khoa in range(26):
        print(f"Khoa {khoa}: {giaimacaesar(dulieumahoa, khoa)}")

print("Chọn một tùy chọn:")
print("1: Mã hóa")
print("2: Giải mã có khóa")
print("3: Phá mã")

lua_chon = input("Nhập số tùy chọn của bạn: ")

if lua_chon == "1":
    dulieubandau = input("Mời bạn nhập dữ liệu cần mã hóa: ")
    khoa = int(input("Nhập số nguyên làm khóa: "))
    dulieumahoa = mahoacaesar(dulieubandau, khoa)
    print("Dữ liệu đã được mã hóa là:", dulieumahoa)

elif lua_chon == "2":
    dulieumahoa = input("Mời bạn nhập dữ liệu đã mã hóa: ")
    khoa = int(input("Nhập số nguyên làm khóa: "))
    dulieugiai = giaimacaesar(dulieumahoa, khoa)
    print("Dữ liệu đã được giải mã là:", dulieugiai)

elif lua_chon == "3":
    dulieumahoa = input("Mời bạn nhập dữ liệu cần phá mã: ")
    print("Dữ liệu có thể giải mã với các khóa sau:")
    phamacaesar(dulieumahoa)
else:
    print(" Vui lòng thử lại số khác (1;3)")
