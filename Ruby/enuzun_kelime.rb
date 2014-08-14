#Encoding: UTF-8
#Kodlayan: Kbhkn

print "Cümlenizi giriniz: "
metin = gets.chomp
metin = metin.split(" ")
enb = metin[0]
esit = Array.new
metin.each do |i|
    if enb.length < i.length
	enb = i
    end
end
metin.each do |x|
    if enb.length == x.length
	esit << x
    end
end
if esit.length > 1
    puts "Cümledeki en uzun kelimeler = #{esit}"
else
    puts "Cümledeki en uzun kelime = #{enb}"
end
