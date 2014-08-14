#Kodlayan: kbhknn
def kopyala(kaynak)
	hedef = []
	kaynak.select {|x| x < 4}.each {|x| hedef << x}
	return hedef
end
