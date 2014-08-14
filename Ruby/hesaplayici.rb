#Encoding: UTF-8
#Kodlayan: kbhknn
puts "Donem \t Sonu Hesaplamasi"
print "Ara sinav notunuzu giriniz: "
as = gets.chomp
print "Donem Sonu Notunuzu Griniz: "
ds = gets.chomp
ort = as.to_i*0.4 + ds.to_i*0.6
puts "Ortalamaniz: #{ort}"
