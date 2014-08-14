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
elsif n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%11 == 0 or n%13 == 0 or n%17 == 0 or n%19 == 0 or n%23 or n% 29 == 0
	puts "Bu sayının bölenleri olduğu için asal değildir."
else
	for i in (14..(n**0.5).floor)
		if n%i == 0
			kontrol << i
		end
	end
	if kontrol.empty?
		puts "#{n}' sayısı asal sayıdır!"
	else
		puts "#{n}' sayısı asal sayı değildir!" 
	end
end
