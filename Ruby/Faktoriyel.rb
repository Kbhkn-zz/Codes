
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
#Encoding: UTF-8
#Kodlayan: kbhknn
puts "Faktoriyel Hesaplayıcısına Hoşgeldiniz"
print "Hesaplanmasını istediğiniz sayıyı giriniz: "
n = gets.chomp.to_i #Kullanıcıdan hesaplanacak faktoriyelin değerini alıyoruz.
if n < 0 # Kullanıcı Negatif sayı girerse Faktoriyel hesaplamadan direk aşağıdaki çıktıyı bize verir.
	puts "Negatif sayıların faktoriyeli hesaplanamaz!"
elsif n >= 0
	toplam = 1 #Öncelikle sistemde toplam adında Fixnum yaratıyoruz.
	while n > 1 #Döngüyü Başlatıyoruz
		toplam = toplam * n # Toplamı n ile çarparak her defasında toplamı arttırıyoruz.
		n = n - 1 # Girilen sayi'yi  her defasında 1 azaltarak sonlu döngü yaratıyoruz.
	end
puts "Faktoriyel Sonucu: #{toplam}"
else
puts "Bilinmeyen bir hata ile karşılaşıldı."
end
