
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
#Encoding: UTF-8
#Kodlayan: kbhknn
puts "Girilen Sayıların 2 Katını Hesaplayan Program"
def iki_kati
	print "Elemanları aralarına virgül koyarak giriniz: "
	dizi = gets.chomp
	dizi = dizi.split(",")
	dizi2 = Array.new
	dizi.each do |e|
		dizi2 << e.to_i
	end
	gecici_dizi = Array.new
	dizi2.each do |e|
		gecici_dizi << e*2
	end
	dizi = gecici_dizi
	print "#{dizi}\n"
end
 
if __FILE__ == $0
	iki_kati
end
