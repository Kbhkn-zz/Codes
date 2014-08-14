#Encoding: UTF-8
#Kodlayan: Kbhkn
puts "Girilen Sayıları Toplama Programı"
def topla
	print "Sayılarınızı arasına virgül koyarak giriniz: "
	dizi = gets.chomp
	dizi = dizi.split(",")
	gecici_dizi = Array.new
	dizi.each do |e|
		gecici_dizi << e.to_i
	end
	dizi = gecici_dizi
	toplam = 0
	dizi.each do |e|
		toplam += e
	end
	print "Girilen sayıların toplamı: #{toplam}\n"
end
if __FILE__ == $0
	topla
end
