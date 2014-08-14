#Encoding: UTF-8
#Kodlayan: Kbhkn
puts "Geometrik Ortalama Bulucu"
def geometrik_ortalama
	print "Sayılarınızı aralarına virgül koyarak giriniz: "
	dizi = gets.chomp
	dizi = dizi.split(",")
	gecici_dizi = Array.new
	dizi.each do |e|
		gecici_dizi << e.to_i
	end
	dizi = gecici_dizi
	carpim = 1
	dizi.each do |e|
		carpim *= e
	end
	if dizi.length == 0
		puts "Boş dizinin geometrik ortalaması hesaplanamaz!"
	else
		go = (carpim)**(1.0/(dizi.length))
		puts "Sayıların çarpımı: #{carpim}, Geometrik ortalaması: #{go}"
	end
end
if __FILE__ == $0
	geometrik_ortalama
end
