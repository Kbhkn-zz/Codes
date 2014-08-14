#Encoding: UTF-8
#Kodlayan: kbhknn
def sirala(a,b,c)
  if a > b then a,b = b,a end 
  if b > c then b,c = c,b end 
  if a > b then a,b = b,a end 
  puts "Girilen sayıların sıralanmış hali: #{a}, #{b}, #{c}"
end
def uygula
  print "1. sayıyı giriniz: "
  a = gets.chomp.to_f
  print "2. sayıyı giriniz: "
  b = gets.chomp.to_f
  print "3. sayıyı giriniz: "
  c = gets.chomp.to_f
  sirala(a,b,c)
end
if __FILE__ == $0
  uygula
end
