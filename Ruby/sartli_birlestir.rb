#encoding: UTF-8
#Kodlayan: Kbhkn
def birlestir(dizi_bir,dizi_iki)
  birlestir = Array.new
  dizi_bir.each do |x|
    dizi_iki.each do |y|
      if x == y
        dizi_iki.delete(y)
      end
    end
  end
  dizi_bir.each do |x|
    birlestir << x
  end
  dizi_iki.each do |y|
    birlestir << y
  end
  puts "#{birlestir}"
end
if __FILE__ == $0
  birlestir
end
