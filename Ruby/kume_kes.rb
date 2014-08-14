#Encoding: UTF-8
#Kodlayan: Kbhkn
def kume_kesisim(dizi_bir = [1,2,8,3,9,777,0],dizi_iki = [66,1,74,3,0,555,9])
	kesisim = Array.new
	for x in dizi_bir
		for y in dizi_iki
			if x == y
				kesisim << x
			end
		end
	end
	puts "Kümelerin kesisimi: #{kesisim} 'dir"
end
if __FILE__ == $0
	kume_kesisim
end
