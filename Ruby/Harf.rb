
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
27
28
29
30
31
32
# encoding: utf-8
# Kodlayan kbhknn
puts ""
puts "Dönem Sonu Not Hesaplamayıcıya Hoş Geldiniz"
while true
print "Arasınav Notunuzu Giriniz: "
as=gets.chomp
	if as.to_i >= 0 && as.to_i < 101
print "Dönem Sonu Notunuzu Giriniz: " 
ds=gets.chomp
	if ds.to_i >= 0 && ds.to_i <= 100
	break     
	else as.to_i < 0 && as.to_i > 100
print "Girdiğiniz değerler 0-100 arası olmalıdır.İşlem Başa döndürülüyor\n"   
	end
else ds.to_i < 0 && ds.to_i > 100
print "Girdiğiniz değerler 0-100 arası olmalıdır.İşlem Başa döndürülüyor\n"
	end
end
ortalama=(as.to_i*0.40)+ (ds.to_i*0.60)
 
case ortalama.to_f
	when 90..100 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: AA\n"
	when 85..89 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: BA\n"
	when 80..84 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: BB\n"
	when 75..79 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: CB\n"
	when 70..74 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: CC\n"
	when 65..69 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: DC\n"
	when 60..64 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: DD\n"
	when 50..59 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: FD\n"
	when 0..49 then print "Ortalamanız: #{ortalama.to_f}, Harfli ifade: FF\n"
end
