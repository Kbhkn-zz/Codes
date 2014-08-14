#Encoding: UTF-8
#Kodlayan: kbhknn
puts ""
puts "Ortalama Hesaplayiciya Hosgeldiniz"
puts ""
print "Arasinav 1 Notunuzu Giriniz: "
as1 = gets.chomp
print "Arasinav 2 Notunuzu Giriniz: "
as2 = gets.chomp
print "Donem Sonu Notunuzu Giriniz: "
as3 = gets.chomp
t = as1.to_i*0.15 + as2.to_i*0.20+as3.to_i*0.65
puts "Degerlerini girdiginiz AS1, AS2 ve DS notlariniza gore ortalamaniz hesaplaniyor"
puts ""
puts "Donem Sonu Notunuz= #{t}"
