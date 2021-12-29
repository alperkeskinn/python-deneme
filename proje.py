while True:
    vize = input('Vize Notunuz : ')
    final = input('Final Notunuz : ')
    ortalama = (float(vize) * 0.3) + (float(final) * 0.7)
    print("Ortalama :{0} ".format(ortalama))
    if ortalama < 50:
        print("FF")
        print("Kaldiniz.... (yazik)")
    elif ortalama < 60:
        print("CC")
        print("Gectiniz!")
    elif ortalama < 70:
        print("CB")
        print("Gectiniz!")
    elif ortalama < 80:
        print("BB")
        print("Gectiniz!")
    elif ortalama < 90:
        print("AB")
        print("Gectiniz!")
    elif ortalama >= 90:
        print("AA")
        print("Gectiniz!")