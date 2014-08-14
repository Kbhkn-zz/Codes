#Encoding: UTF-8
#Kodlayan: kbhknn
 
class Diktortgen
	def initialize(uzunluk, genislik)
		@uzunluk = uzunluk
		@genislik = genislik
	end
 
	def cevre
		2 * (@uzunluk + @genislik)
	end
 
	def alan
		@uzunluk * @genislik
	end
 
	def kosegen
		(@uzunluk**2 + @genislik**2)**0.5
	end
end
 
def main
	print "Dikdörtgeninizin uzun kenarını giriniz: "
	uzun = gets.chomp.to_f
	print "Dikdörtgeninizin kısa kenarını giriniz: "	
	kisa = gets.chomp.to_f
	d = Diktortgen.new(uzun,kisa)
	puts "Dikdortgeninizin çevresi = #{d.cevre}"
	puts "Dikdortgeninizin alanı = #{d.alan}"
	puts "Dikdortgeninizin köşegen uzunluğu = #{d.kosegen}"
end
 
 
if __FILE__ == $0
  main
end
