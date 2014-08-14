#Encoding: UTF-8
#Kodlayan: Kbhkn

print "Kontrol edilecek sayıyı giriniz: "
n = gets.chomp.to_i
kontrol = []
if n <= 2
	if n == 2
	puts "#{n}' sayısı asal sayıdır."
	else
	puts "En küçük asal sayı 2'dir!"
	end
elsif n%2 == 0
	puts "2'den başka çift asal olmadığı için sayınız asal değildir."
else
	for i in (2..(n-1))
		if n%i == 0
			kontrol << i
		end
	end
	if kontrol.empty?
		puts "#{n}' sayısı asal sayıdır!"
	else
		puts "#{n}' sayısı asal sayı değildir! Bölenleri:\n#{kontrol}" 
	end
end
