1)
a) Aritmetik ortalama hesaplatma
def aritmetik_ortalama(dizi)
	toplam = 0
	dizi.each do |e|
		toplam += e
	end
	ao = toplam.to_f/(dizi.length)
	puts "Aritmetik ortala: #{ao}"
end
 
b) Tekindis ekrana basma
def tek_indis(dizi)
    dizi.each_with_index do |e,i|
       if i%2 == 1
	   puts e
       end
    end
end
 
2) String yapma
def string_yap(dizi)	
  string = Array.new
  dizi.each do |e|
    if e.class == Array
       e = e.join("")
    end
    string << e
  end
  string = string.join("")
  return string
end
 
3) 
a) Birleştirme
def birlestir(dizi_bir,dizi_iki)
   birlestir = Array.new
   birlestir = dizi_bir
   dizi_iki.each do |e|
     birlestir << e
   end
   return birlestir
end
 
b ) kesisim
def kesisim(dizi_bir,dizi_iki)
   kesisim = Array.new
   for x in dizi_bir
     for y in dizi_iki
        if x == y
           kesisim << x
        end
     end
  end
  return kesisim
end
c) fark bulma
 
def fark(a,b)
   fark = Array.new
   kesisim = Array.new
   for x in a
     for y in b
       if x == y
          kesisim << x
       end  
     end  
   end  
   for x in a
     for y in kesisim
       if x != y
         fark << x
       end  
     end  
   end  
   if fark.empty?
      puts "Kumenın Farkı: #{a}"
   else
      puts "Kumenin Farkı: #{fark}"
   end
end
 
4) 
a) Kendine en yakın tam sayı yuvarlama
def en_yakin(sayı)
   if sayı - 0.5 >= sayi.to_i
      return sayı.to_i +1
   else
      return sayı.to_i
   end
end
 
b) Kendisinden kücük tam sayı yuvarlama
def kucuk(sayı)
   return sayı.to_i
end
 
c) Kendisinden büyük tam sayıya yuvarlama
def buyuk(sayı)
   buyuk = sayı + 1
   return buyuk.to_i
end
