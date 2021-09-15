def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def devide(x, y):
    return x / y

while True:
    print("<-------------------Kalkulator Python Lur----------------------->")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    pilihan_op = input("Masukkan pilihan(1/2/3/4): ")

    if pilihan_op in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan Angka Pertama: "))
        angka2 = float(input("Masukkan Angka Pertama: "))

        if pilihan_op == '1':
            print(angka1, "+", angka2, '=', add(angka1, angka2))
        elif pilihan_op == '2':
            print(angka1, "-", angka2, '=', substract(angka1, angka2))
        elif pilihan_op == '3':
            print(angka1, "*", angka2, '=', multiply(angka1, angka2))
        elif pilihan_op == '4':
            print(angka1, "/", angka2, '=', devide(angka1, angka2))
        
        lanjut_ga = input("Ingin melakukan operasi lainnya? (ya/ngga): ")
        if lanjut_ga == 'ngga':
            break
    
    else:
        print("Input salah gan..")
        