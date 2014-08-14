#Encoding: UTF-8
#Kodlayan: Kbhkn
def mutlak_deger
	puts "Dizinin Mutlak Değer Hesaplayıcısı"
	print "Sayılarınızı aralarına virgül koyarak giriniz: "
	dizi = gets.chomp
	dizi = dizi.split(",")
	gecici_dizi = Array.new
	dizi.each do |e|
		gecici_dizi << e.to_f
	end
	dizi = gecici_dizi
	gecici_dizi_iki = Array.new
	dizi.each do |e|
		if e >= 0 then gecici_dizi_iki << e end
		if e < 0 then gecici_dizi_iki << e*(-1) end
	end
	dizi = gecici_dizi_iki
	print "#{dizi}\n"
end
if __FILE__==$0
	mutlak_deger
end
