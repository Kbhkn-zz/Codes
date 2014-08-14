#Encoding: UTF-8
#Kodlayan: kbhkn
puts "Girilen Sayıların Kuvvetini Hesaplayan Program"
def kuvvet
	print "Elemanları aralarına virgül koyarak giriniz: "
	dizi = gets.chomp
	print "Kaçıncı kuvveti alınacaksa giriniz: "
	kuvvet = gets.chomp.to_f
	dizi = dizi.split(",")
	dizi2 = Array.new
	dizi.each do |e|
		dizi2 << e.to_i
	end
	gecici_dizi = Array.new
	dizi2.each do |e|
		gecici_dizi << e**kuvvet
	end
	dizi = gecici_dizi
	print "#{dizi}\n"
end
 
if __FILE__ == $0
	kuvvet
end
