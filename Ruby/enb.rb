
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
#Kodlayan: Kbhkn
puts "Dizinin Enbüyük Elemanını Bulan Program"
def enb
	print "Aralarına virgül koyarak sayıları giriniz: "
	dizi = gets.chomp
	dizi = dizi.split(",")
	gecici_dizi = Array.new
	dizi.each do |e|
		gecici_dizi << e.to_i
	end
	enb = gecici_dizi[0]
	gecici_dizi[1..gecici_dizi.length-1].each do |e|
		if e > enb
			enb = e
		end
	end
	puts "Girdiğiniz sayıların en büyüğü: #{enb}"
end
if __FILE__ == $0
	enb
end
