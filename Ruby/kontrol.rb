#Encoding: UTF-8
#Kodlayan: kbhknn
puts "Cümledeki Sesli Harf Sayısını Buldurup Yazdırmak"
print "Lütfen Cümlenizi Giriniz: "
a = gets.chomp
b = a.scan(/[aeiouAEIOU]/)
if b.length == 0
	puts "Girilen cümlede sesli harf bulunmamaktadır."
else
	puts "Girilen Cümlede #{b.length} adet sesli harf bulunmaktadır.\nSesli Harfler Sırasıyla: #{b}"
end
