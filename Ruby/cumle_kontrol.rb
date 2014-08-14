#Encoding: UTF-8
#Kodlayan: kbhknn
puts "Cümleniz 'E/e' ile Başlıyor Mu?"
print "Cümlenizi Giriniz: "
cumle = gets.chomp
if cumle =~ /^[Ee]/
        puts "Cümleniz 'E/e' ile başlıyor."
else
        puts "Hayır Cümleniz 'E/e' ile başlamıyor."
end
