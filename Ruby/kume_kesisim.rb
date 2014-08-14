#Encoding: UTF-8
#Kodlayan: Kbhkn
puts "Verilen İki Kümenin Kesişimini Hesaplama"
def kesisim
  puts "1.Kümenin elemanlarını aralarına virgül koyarak giriniz: "
  dizi_bir = gets.chomp
  puts "2.Kümenin elemanlarını aralarına virgül koyarak giriniz: "
  dizi_iki = gets.chomp
  dizi_bir = dizi_bir.split(",")
  dizi_iki = dizi_iki.split(",")
  dizi_bir_gecici = Array.new
  dizi_iki_gecici = Array.new
  dizi_bir.each do |e|
    dizi_bir_gecici << e.to_f
  end
  dizi_iki.each do |e|
    dizi_iki_gecici << e.to_f
  end
  dizi_bir = dizi_bir_gecici
  dizi_iki = dizi_iki_gecici
  kesisim = Array.new
  for x in dizi_bir
    for y in dizi_iki
      if x == y
          kesisim << x
      end
    end
  end
  puts "Verilen iki kümenin kesişimleri: #{kesisim} 'dir."
end
if __FILE__ == $0
  kesisim
end
