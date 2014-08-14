# encoding: utf-8
# Kodlayan kbhknn	
 
puts "Dönem Sonu Not Hesaplamayıcıya Hoş Geldiniz"
puts ""
while true
print "Arasınav Notunuzu Giriniz: "
a = gets.chomp
	if a.to_i >= 0 && a.to_i <= 100
print "Dönem Sonu Notunuzu Giriniz:"
b = gets.chomp
if b.to_i >= 0 && b.to_i <= 100
break
	else a.to_i < 0 && a.to_i > 100
print "Girdiğiniz değerler 0-100 arası olmalıdır.İşlem Başa Döndürüldü\n"   
end
	else b.to_i < 0 && b.to_i > 100
print "Girdiğiniz değerler 0-100 arası olmalıdır.İşlem Başa Döndürüldü\n"
	end
end
c=(a.to_i*0.40)+ (b.to_i*0.60)
puts ""
if c >= 60
	puts "Dönem Sonu Ortalamanız: '#{c}' Tebrikler Bu Ortalama İle Sınıfı Geçtiniz."
else
	puts "Dönem Sonu Ortalamanız: '#{c}' Ortalamanız 60'dan küçük olduğundan dolayı kaldınız."
	puts ""
end
