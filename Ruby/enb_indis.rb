#Encoding: UTF-8
#Kodlayan: Kbhkn
puts "Dizinin Enbüyük Elemanını Bulan Ve Yerini Söyle"
def enb_indis
	print "Sayılarınızı aralarına virgül koyarak giriniz: "
	dizi = gets.chomp
	dizi = dizi.split(",")
	gecici_dizi = Array.new
	dizi.each do |e|
		gecici_dizi << e.to_f
	end
	dizi = gecici_dizi
	enb = dizi[0]
	indis = 0
	dizi[1..dizi.length-1].each_with_index do |e,i|
		if e > enb
			enb = e
			indis = i+1
		end
	end
	puts "Dizinin en büyük elemanı: #{enb}, indisi #{indis}"
end
if __FILE__ == $0
	enb_indis
end
