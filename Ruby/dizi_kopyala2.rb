#Kodlayan: kbhknn
def dizi_kopyala(kaynak)
	hedef = Array.new
	for x in kaynak.select {|x| x < 4}
		hedef.push x
	end
	return hedef
end
