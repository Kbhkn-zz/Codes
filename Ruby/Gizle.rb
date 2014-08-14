#Encoding: UTF-8
#Kodlayan: kbhknn
class Gizle
	def initialize(metin)
		@metin = metin
	end
	def donustur
		@metin.gsub(/[aeıioöuüAEIİOÖUÜ]/, '*')
	end
end
def baslat
	print "Dönüştürelecek metni giriniz: "
	metin = gets.chomp
	puts "Dönüştürülmüş metin = #{Gizle.new(metin).donustur}"
end
if __FILE__ == $0
	baslat
end
