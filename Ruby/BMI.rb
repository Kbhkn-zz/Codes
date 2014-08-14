# encoding: UTF-8
# Kodlayan kbhknn
puts "Vücut Kitle Endeksi Hesaplayıcıya Hoş Geldiniz"
puts ""
print "Lütfen İsminizi Giriniz: "
isim = gets.chomp
print "Boyunuzu Metre Cinsinden Giriniz(Örnek 1.80,1.44): "
boy = gets.chomp.to_f
print "Kilonuzu Kilogram Cinsinden Giriniz: "
kilo = gets.chomp.to_f
print "Girdilerinize Göre Sonucunuz Hesaplanyor...\n"
a = boy.to_f * boy.to_f
vki = kilo / a
case vki.to_f
	when 40..999 then puts "Sayın #{isim}, BMI Sonucunuz: #{vki.to_f} ,İleri Derecede Obezsiniz..."
	when 30..39 then puts "Sayın #{isim}, BMI Sonucunuz: #{vki.to_f} ,Fazla Kilolu[Obezsiniz]..."
	when 25..29 then puts "Sayın #{isim}, BMI Sonucunuz: #{vki.to_f} ,Kilolusunuz..."
	when 18..24 then puts "Sayın #{isim}, BMI Sonucunuz: #{vki.to_f} ,Optimal Değerdesiniz..."
	when 0..17 then puts "Sayın #{isim}, BMI Sonucunuz: #{vki.to_f} ,Zayıfsınız.."
	else puts "Sonuç Negatif Çıkamaz! Lütfen Bilgilerinizi kontrol ederek tekrar giriniz.."
end
