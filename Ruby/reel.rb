# encoding: utf-8
# Kodlayan: kbhknn
puts "Gerçel Sayı Hesaplayıcısına Hoş Geldiniz"
puts ""
print "Lütfen istediğiniz sayının tam kısmını giriniz: "
tam = gets.chomp.to_i
print "Lütfen istediğiniz sayının ondalık kımını giriniz: "
ondalik = gets.chomp.to_i
puts "Girdilerinize göre gerçel sayınız hesaplanıyor.."
sayi = "#{tam}"+"."+"#{ondalik}"
reelsayi = sayi.to_f
test = reelsayi**2
puts "Reel Sayınız: #{reelsayi}, Test Amaçlı Sayınızın Karesi Alındı: #{test}"
