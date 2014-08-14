#!/usr/bin/ruby -w
#Encoding: UTF-8
#Kodlayan: Kbhkn

puts "İngilizce alfabeleri kullanarak cümlenizi giriniz"
cumle = gets.chomp.downcase
cumle = cumle.split("")
cumle_iki = ""
alfabe=('a'..'z').to_a
cumle.each_with_index do |e,i|
	alfabe.each_with_index do |x,y|
		if e ==x
			if y < 13 then cumle_iki << alfabe[y+13]  end
			if y > 12 then cumle_iki << alfabe[y-13]  end
		end
	end
end
puts "Rot13 hali: #{cumle_iki}"
