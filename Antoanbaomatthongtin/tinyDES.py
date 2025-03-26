hoanh = ['0000','0001','0010','0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
tung = ['00','01','10','11']

box = [
    ["1110", "0100", "1101", "0001", "0010", "1111", "1011", "1000", "0011", "1010", "0110", "1100", "0101", "1001", "0000", "0111"],
    ["0000", "1111", "0111", "0100", "1110", "0010", "1101", "0001", "1010", "0110", "1100", "1011", "1001", "0101", "0011", "1000"],
    ["0100", "0001", "1110", "1000", "1101", "0110", "0010", "1011", "1111", "1100", "1001", "0111", "0011", "1010", "0101", "0000"],
    ["1111", "1100", "1000", "0010", "0100", "1001", "0001", "0111", "0105", "1011", "0011", "1110", "1010", "0000", "0110", "1101"]
]

while True:
    banro = input("Nhập bản rõ ( chuỗi 8 bit ) : ")
    if len(banro) == 8 and all(char in '01' for char in banro):
        break
    else:
        print("Chuỗi không hợp lệ, vui lòng nhập lại.")
Left = banro[:4]
Right = banro[4:]

while True:
    khoa = input("Nhập khóa ( chuỗi 8 bit ) : ")
    if len(khoa) == 8 and all(char in '01' for char in khoa):
        break
    else:
        print("Chuỗi không hợp lệ, vui lòng nhập lại.")

KLeft = khoa[:4]
KRight = khoa[4:]

Expand = Right[2] + Right[3] + Right[1] + Right[2] + Right[1] + Right[0]


i = 1
while i<=3:
    tempLeft = Left
    Left = Right
    Expand = Right[2] + Right[3] + Right[1] + Right[2] + Right[1] + Right[0]
    if (i==1 or i==3):
        KLeft = KLeft[1:] + KLeft[0]
        KRight = KRight[1:] + KRight[0]
    else:
        j = 1
        while j<=2:
            KLeft = KLeft[1:] + KLeft[0]
            KRight = KRight[1:] + KRight[0]
            j = j+1
    Compress = KLeft + KRight
    khoaK = Compress[5] + Compress[1] + Compress[3] + Compress[2] + Compress[7] + Compress[0]
    xor_Expand_khoaK = ''.join([str(int(a) ^ int(b)) for a, b in zip(Expand, khoaK)])
    S_box = box[tung.index(xor_Expand_khoaK[0]+xor_Expand_khoaK[5])][hoanh.index(xor_Expand_khoaK[1:5])]
    P_box = S_box[2] + S_box[0] + S_box[3] + S_box[1]
    Right = ''.join([str(int(a) ^ int(b)) for a, b in zip(tempLeft, P_box)])
    print(Expand)
    print(KLeft)
    print(KRight)
    print(khoaK)
    print(xor_Expand_khoaK)
    print(S_box)
    print(P_box)
    print(Right)
    i = i + 1 
    print ("\n")
banma = Left + Right
decimal = int(banma, 2)
hexa = hex(decimal)

print (f"\nBản rõ là : {banro}")
print (f"Khóa là : {khoa}")
print (f"=> Bản mã là : {banma} (hệ thập lục phân: {hexa[2:].upper()})")