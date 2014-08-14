
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
23
24
25
26
#Encoding: UTF-8
#Kodlayan: kbhkn
puts "Aritmetik Ortalama Bulucu"
def aritmetik_ortalama
	print "Sayıları aralarına virgül koyarak giriniz: "
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
	if dizi.length == 0
		puts "Boş dizinin aritmetik ortalaması hesaplanamaz!"
	else		
		ao = toplam/(dizi.length.to_f)
		puts "Dizinin toplamı: #{toplam}, Aritmetik ortalaması: #{ao}"
	end
end
if __FILE__ ==$0
	aritmetik_ortalama
end
