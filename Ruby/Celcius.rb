#Encoding: UTF-8
#Kodlayan: kbhknn
class Celcius
	def initialize(derece)
		@derece = derece
	end
	
	def donustur
		(@derece * 1.8) + 32
	end
end
 
def main
	print "Celcius değerini giriniz: "
	c = gets.chomp.to_f
	a= Celcius.new(c)
	puts "Fahrenheit olarak = #{a.donustur}"
end
 
if __FILE__ == $0
	main
end
