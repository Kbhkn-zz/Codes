#Encoding: UTF-8
#Kodlayan: kbhknn
class Mathematic
	def initialize(deger,us)
		@deger = deger
		@us = us
	end
	def us_al
		@deger**@us
	end
	def kare_al
		@deger**2
	end
	def pi
		(22.0/7)
	end
end
def main
	print "Hesaplanılacak değeri giriniz: "
	deger = gets.chomp.to_f
	print "Üssü değerini giriniz: "
	us = gets.chomp.to_f
	sonuc = Mathematic.new(deger, us)
	puts "Üssü alınmış hali = #{sonuc.us_al}"
	puts "Karesi = #{sonuc.kare_al}"
	puts "Pi değeri = #{sonuc.pi}"
	puts "Sinüs değeri = #{Math.sin(deger)}"
	puts "Cosinüs değeri = #{Math.cos(deger)}"
	puts "Tan. değeri = #{Math.tan(deger)}"
	puts "Cot. değeri = #{Math.tan(deger)**-1}"
end
if __FILE__ == $0
 	main
end
