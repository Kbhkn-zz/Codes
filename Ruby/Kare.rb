class Kare
	def initialize(uzunluk)
		@uzunluk = uzunluk
	end
 
	def cevre
		4 * (@uzunluk)
	end
 
	def alan
		@uzunluk**2
	end
 
	def kosegen
		(2*(@uzunluk**2))**0.5
	end
end
 
def main
	print "Karenizin kenar uzunlugunu giriniz: "
	b = gets.chomp.to_f
	a = Kare.new(b)
	puts "Karenizin cevresi = #{a.cevre}"
	puts "Karenizin alani = #{a.alan}"
	puts "Karenizin kosegen uzunlugu = #{a.kosegen}"
end
 
if __FILE__ == $0
	main
end
