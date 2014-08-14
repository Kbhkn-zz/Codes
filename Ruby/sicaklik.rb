#Encoding: UTF-8
#Kodlayan: kbhknn
puts "Sicaklik degerini giriniz: "
t = gets.chomp.to_f
if t < 0
	puts "KATI"
else
	if t < 100
		puts "SIVI"
	else
		puts "GAZ"
	end
end
