#Encoding: UTF-8
#Kodlayan: Kbhkn
puts "Tek İndis Seç"
def tek_indis
	print "Sayılarınızı aralarına virgül koyarak giriniz: "
	dizi = gets.chomp
	dizi = dizi.split(",")
	gecici_dizi = Array.new
	dizi.each do |e|
		gecici_dizi << e.to_f
	end
	dizi = gecici_dizi
	tek_indis = Array.new
	dizi.each_with_index do |e,i|
		if i%2 == 1 then tek_indis << e	end
	end
	dizi = tek_indis
	puts "#{dizi}"
end
if __FILE__ == $0
	tek_indis
end
