#Encoding: UTF-8
#Kodlayan: Kbhkn
puts "Dizinin Ağırlıklı Toplamını Hesaplayıcı"
def agirlikli_toplam
	print "Sayılarınızı aralarına virgül koyarak giriniz: "
	dizi = gets.chomp
	dizi = dizi.split(",")
	gecici_dizi = Array.new
	dizi.each do |e|
		gecici_dizi << e.to_f
	end
	dizi = gecici_dizi
	toplam = 0
	dizi.each_with_index do |e,i|
		toplam += e*i
	end
	puts "Verilen dizinin ağırlıklı toplamı: #{toplam}"
end
if __FILE__ == $0
	agirlikli_toplam
end
