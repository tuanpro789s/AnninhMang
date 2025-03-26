def mahoavigenere(dulieubandau, khoa):
    dulieumahoa = ""
    khoa = khoa.upper()  
    chi_so = 0  
    for kytu in dulieubandau:
        if kytu.isalpha():
            dich = ord('A') if kytu.isupper() else ord('a')
            khoa_hientai = ord(khoa[chi_so % len(khoa)]) - ord('A')
            dulieumahoa += chr((ord(kytu) - dich + khoa_hientai) % 26 + dich)
            chi_so += 1 
        else:
            dulieumahoa += kytu
    return dulieumahoa

def giaimavigenere(dulieumahoa, khoa):
    dulieugiai = ""
    khoa = khoa.upper()
    chi_so = 0
    for kytu in dulieumahoa:
        if kytu.isalpha():
            dich = ord('A') if kytu.isupper() else ord('a')
            khoa_hientai = ord(khoa[chi_so % len(khoa)]) - ord('A')
            dulieugiai += chr((ord(kytu) - dich - khoa_hientai + 26) % 26 + dich)
            chi_so += 1
        else:
            dulieugiai += kytu
    return dulieugiai

print("Chọn một tùy chọn:")
print("1: Mã hóa")
print("2: Giải mã với khóa")
lua_chon = input("Nhập số tùy chọn của bạn: ")
if lua_chon == "1":
    dulieubandau = input("Mời bạn nhập dữ liệu cần mã hóa: ")
    khoa = input("Nhập khóa (chuỗi ký tự): ")
    dulieumahoa = mahoavigenere(dulieubandau, khoa)
    print("Dữ liệu đã được mã hóa là:", dulieumahoa)
elif lua_chon == "2":
    dulieumahoa = input("Mời bạn nhập dữ liệu đã mã hóa: ")
    khoa = input("Nhập khóa (chuỗi ký tự): ")
    dulieugiai = giaimavigenere(dulieumahoa, khoa)
    print("Dữ liệu đã được giải mã là:", dulieugiai)
else:
    print(" Vui lòng thử lại số khác (1;3)")