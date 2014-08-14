#Encoding: UTF-8
#Kodlayan: kbhknn
puts "En Büyük Ortak Bölen Hesaplayıcıya Hoşgeldiniz"
def gcb
	print "İlk sayıyı giriniz: "
	a = gets.chomp.to_i
	while a < 1
		print "Girilen değer 0 veya negatif olamaz!\nLütfen ilk sayıyı yeniden giriniz: "
		a = gets.chomp.to_i
	end
	print "İkinci sayıyı giriniz: "
	b = gets.chomp.to_i
	while b < 1
		print "Girilen değer 0 veya negatif olamaz!\nLütfen ikinci sayıyı yeniden giriniz: "
		b = gets.chomp.to_i
	end
	x = a
	y = b
	while y != 0
		r = x%y
		x = y
		y = r
	end
	puts "#{a} ile #{b} sayılarının OBEB'i: #{x}"
end
if __FILE__ == $0
	gcb
end
