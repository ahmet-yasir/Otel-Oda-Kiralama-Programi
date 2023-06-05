from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

def kontrol():             # Entry'lere uygun değerler girimesini kontol eden fonksiyon
    try:
        if entry_ad.get()=="" or entry_soyad.get()=="" or entry_eposta.get()=="" or entry_yetiskinsayisi.get()=="" or entry_cocuksayisi.get()=="" or entry_tatilsuresi.get()=="":
            messagebox.showwarning("Uyarı!","Alanlar boş bırakılamaz!")
        else:
            yetiskin = int(entry_yetiskinsayisi.get())
            cocuk=int(entry_cocuksayisi.get())
            tatilsuresi=int(entry_tatilsuresi.get())
            if yetiskin<0 or cocuk<0 or tatilsuresi<0:
                messagebox.showwarning("Uyarı!","Hatalı Bilgi Girişi!")
            else:
                return True
    except ValueError:
        messagebox.showwarning("Uyarı!", "Geçersiz Bilgi Girişi!")
        return False


def total():                           # Total buton fonksiyonu
    toplam = 0
    if kontrol()==True:
        tatilyeri=group.get()
        if cbox.get()=="FAMILY":          # Oda türü kontrolü
            if tatilyeri=="Bodrum":       # Fiyatlar için tatil yeri kontrolü 
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*10
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*5
                s="Toplam Tutar:"+str(toplam)+" TL"
                messagebox.showinfo("Toplam Tutar",s)
            elif tatilyeri=="Marmaris":
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*2
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*1
                s="Toplam Tutar:"+str(toplam)+" TL"
                messagebox.showinfo("Toplam Tutar",s)
            elif tatilyeri=="Çeşme":
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*6
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*3
                s = "Toplam Tutar:" + str(toplam) + " TL"
                messagebox.showinfo("Toplam Tutar", s)
            else:
                messagebox.showerror("Hata!", "Lütfen tatil yerini işaretleyiniz.")
                return False
        elif cbox.get()=="DELUXE":
            if tatilyeri=="Bodrum":
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*12
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*6
                s = "Toplam Tutar:" + str(toplam) + " TL"
                messagebox.showinfo("Toplam Tutar", s)
            elif tatilyeri=="Marmaris":
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*4
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*2
                s = "Toplam Tutar:" + str(toplam) + " TL"
                messagebox.showinfo("Toplam Tutar", s)
            elif tatilyeri=="Çeşme":
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*8
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*4
                s = "Toplam Tutar:" + str(toplam) + " TL"
                messagebox.showinfo("Toplam Tutar", s)
            else:
                messagebox.showerror("Hata!", "Lütfen yerini işaretleyiniz.")
                return False
        elif cbox.get()=="KING SUIT":
            if tatilyeri=="Bodrum":
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*14
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*7
                s = "Toplam Tutar:" + str(toplam) + " TL"
                messagebox.showinfo("Toplam Tutar", s)
            elif tatilyeri=="Marmaris":
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*6
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*3
                s = "Toplam Tutar:" + str(toplam) + " TL"
                messagebox.showinfo("Toplam Tutar", s)
            elif tatilyeri=="Çeşme":
                toplam+=int(entry_yetiskinsayisi.get())*int(entry_tatilsuresi.get())*10
                toplam+=int(entry_cocuksayisi.get())*int(entry_tatilsuresi.get())*5
                s = "Toplam Tutar:" + str(toplam) + " TL"
                messagebox.showinfo("Toplam Tutar", s)
            else:
                messagebox.showerror("Hata!", "Lütfen yerini işaretleyiniz.")
                return False
        return True
    else:
        return False

def reservation():           # Reservation buton fonksiyonu
    if total()==True:
        messagebox.showinfo("Bilgilendirme!","Rezervasyon işlemi başarıyla tamamlandı.")

def reset():                 # Reset buton fonksiyonu
    entry_ad.delete(0,"end")
    entry_soyad.delete(0,"end")
    entry_yetiskinsayisi.delete(0,"end")
    entry_eposta.delete(0,"end")
    entry_cocuksayisi.delete(0,"end")
    entry_tatilsuresi.delete(0,"end")
    group.set(None)
    cbox.current(0)

pencere=Tk()                     # Kullanıcı arayüzü tasarımı
pencere.geometry("315x330")
pencere.title("Oda Rezervasyon Sistemi")
l_ad=Label(pencere)
l_ad.config(text="Ad")
l_ad.place(x=50,y=50)
l_soyad=Label(pencere)
l_soyad.config(text="Soyad")
l_soyad.place(x=50,y=75)
l_eposta=Label(pencere)
l_eposta.config(text="E-posta")
l_eposta.place(x=50,y=100)
l_yetiskinsayisi=Label(pencere)
l_yetiskinsayisi.config(text="Yetişkin Sayısı")
l_yetiskinsayisi.place(x=50,y=125)
l_cocuksayisi=Label(pencere)
l_cocuksayisi.config(text="Çocuk Sayısı")
l_cocuksayisi.place(x=50,y=150)
l_tatilsuresi=Label(pencere)
l_tatilsuresi.config(text="Tatil Süresi")
l_tatilsuresi.place(x=50,y=175)
l_odaturu=Label(pencere)
l_odaturu.config(text="Oda Türü")
l_odaturu.place(x=50,y=200)
entry_ad=Entry(pencere)
entry_ad.place(x=130,y=50)
entry_soyad=Entry(pencere)
entry_soyad.place(x=130,y=75)
entry_eposta=Entry(pencere)
entry_eposta.place(x=130,y=100)
entry_yetiskinsayisi=Entry(pencere)
entry_yetiskinsayisi.place(x=130,y=125)
entry_cocuksayisi=Entry(pencere)
entry_cocuksayisi.place(x=130,y=150)
entry_tatilsuresi=Entry(pencere)
entry_tatilsuresi.place(x=130,y=175)
cbox=Combobox(pencere)
cbox['values']=("FAMILY", "DELUXE", "KING SUIT")
cbox.place(x=130,y=200)
cbox.config(width=17,state="readonly")
cbox.current(0)
group = StringVar()
Radiobutton(pencere, text="Bodrum", variable=group, value="Bodrum").place(x=50,y=230)
Radiobutton(pencere, text="Marmaris", variable=group, value="Marmaris").place(x=120,y=230)
Radiobutton(pencere, text="Çeşme", variable=group, value="Çeşme").place(x=200,y=230)
b_total=Button(pencere)
b_total.config(text="Total",width=5,command=total)
b_total.place(x=62,y=265)
b_reservation=Button(pencere)
b_reservation.config(text="Reservation",width=11,command=reservation)
b_reservation.place(x=101,y=265)
b_reset=Button(pencere)
b_reset.config(text="Reset",width=5,command=reset)
b_reset.place(x=176,y=265)
b_exit=Button(pencere)
b_exit.config(text="Exit",width=4,command=quit)
b_exit.place(x=215,y=265)
mainloop()

def quit():
    quit()
