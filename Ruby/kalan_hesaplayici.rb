# encoding: UTF-8
# Kodlayan kbhknn
puts "Kalan Hesaplayıcıya Hoş Geldiniz"
print "Sayınızın Bölünen Kısmını Giriniz: "
s1 = gets.chomp.to_f
if s1 ==0 
	puts "Bölünen kısmını 0 girdiniz. Kalan Otomatikmen 0'dır"
else
	print "Sayınızın Bölen Kısmını Giriniz: "
	s2 = gets.chomp.to_f
	while s2 == 0 #Kullanıcı Bölen Kısmını 0 girerse yeni değer girmesi için döngü oluşturdum.
		print "Bölen Kısmı #{s2} olamaz! Lütfen Yeni Bölen Değerini Giriniz: "
		s2 = gets.chomp.to_f
	end
	bolumkalan = s1%s2
	if bolumkalan == 0
		puts "#{s1} sayısı #{s2} sayının tam Katıdır. Kalan: #{bolumkalan.to_i}"
	else
		puts "#{s1} , #{s2} ile bölümünden Kalan: #{bolumkalan}"
	end
end
