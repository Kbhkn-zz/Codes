#Encoding: UTF-8
#Kodlayan: kbhknn
puts "Cümlenizdeki Sesli Harflerin Tümünü * yapmak"
print "Cümlenizi giriniz: "
cumle = gets
yeni = cumle.gsub(/[aeiouAEIOU]/, '*')
puts yeni
