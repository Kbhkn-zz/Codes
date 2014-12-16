from random import randrange
import time
 
def kelime2():
    puan=0      
    list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
    list2=['a','a','a','a','a','a','a','a','a']
    list3=['a','a','a','a','a','a','a','a','a']
    list4=['a','a','a','a','a','a','a','a','a']
    list5=['a','a','a','a','a','a','a','a','a']
    list6=['a','a','a','a','a','a','a','a','a']
    list7=['a','a','a','a','a','a','a','a','a']
    list8=['a','a','a','a','a','a','a','a','a']
    list9=['a','a','a','a','a','a','a','a','a']
    list10=['a','a','a','a','a','a','a','a','a']
    klist=[['k','a','l'],['k','e','l'],['g','e','l'],['g','i','t'],['k','a','l','p'],['a','r','a','b','a'],['p','r','o','g','r','a','m']]
    yanlissayisi=0
    while 0<len(klist) and yanlissayisi<3:
        i=0
        while i<len(list2):
            x=randrange(25)
            list2[i]=list1[x]
            i=i+1
        i=0
        while i<len(list3):
            x=randrange(25)
            list3[i]=list1[x]
            i=i+1
        i=0
        while i<len(list4):
            x=randrange(25)
            list4[i]=list1[x]
            i=i+1
        i=0
        while i<len(list5):
            x=randrange(25)
            list5[i]=list1[x]
            i=i+1
        i=0
        while i<len(list6):
            x=randrange(25)
            list6[i]=list1[x]
            i=i+1
        i=0
        while i<len(list7):
            x=randrange(25)
            list7[i]=list1[x]
            i=i+1
        i=0
        while i<len(list8):
            x=randrange(25)
            list8[i]=list1[x]
            i=i+1
        i=0
        while i<len(list9):
            x=randrange(25)
            list9[i]=list1[x]
            i=i+1
        i=0
        while i<len(list10):
            x=randrange(25)
            list10[i]=list1[x]
            i=i+1
        tlist=[list2,list3,list4,list5,list6,list7,list8,list9,list10]
        yatay=0
        dikey=1
        secim=randrange(2)
        if secim==0:
            k=randrange(len(tlist))
            th=tlist[k]
            l=randrange(len(klist))
            kelime=klist[l]
            bas= randrange((len(th))-len(kelime))
            j=0
            while j<len(kelime):
                th[bas]=kelime[j]
                j=j+1
                bas=bas+1
        else:
            l=randrange(len(klist))
            kelime=klist[l]
            basliste=randrange((len(tlist))- (len(kelime)))
            th=tlist[basliste]
            bas=randrange(len(th))
            j=0
            while j<len(kelime):
                th[bas]=kelime[j]
                basliste=basliste+1
                th=tlist[basliste]
                j=j+1
        list2=' '.join(list2)
        list3=' '.join(list3)
        list4=' '.join(list4)
        list5=' '.join(list5)
        list6=' '.join(list6)
        list7=' '.join(list7)
        list8=' '.join(list8)
        list9=' '.join(list9)
        list10=' '.join(list10)
        print (list2)
        print (list3)
        print (list4)
        print (list5)
        print (list6)
        print (list7)
        print (list8)
        print (list9)
        print (list10)
        print ('tahmin et:\n')
        time.sleep(10)
        tahminim=str(input('zaman doldu \n harflerin arasına bir bosluk birakarak\n tahmininizi giriniz:\n'))
        time.sleep(1)
        tahminim=tahminim.split(' ')
        if kelime==tahminim:
            if len(kelime)==2:
                puan=puan+20
            elif len(kelime)==3:
                puan=puan+30
            elif len(kelime)==4:
                puan=puan+40
            elif len(kelime)==5:
                puan=puan+50
            elif len(kelime)==6:
                puan=puan+60
            elif len(kelime)==7:
                puan=puan+70
            else:
                puan=puan+50
            print ('cevap dogru'),(puan)
            del klist[l]
        else:
            print ('cevap yanlıs')
            yanlissayisi=yanlissayisi+1
        list2=list2.split(' ')
        list3=list3.split(' ')
        list4=list4.split(' ')
        list5=list5.split(' ')
        list6=list6.split(' ')
        list7=list7.split(' ')
        list8=list8.split(' ')
        list9=list9.split(' ')
        list10=list10.split(' ')
    if yanlissayisi==3:
        print ('kaybettiniz')
    else:
        print ('toplam puan:'),(puan)
kelime2()