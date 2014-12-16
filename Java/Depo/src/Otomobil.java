class Otomobil
{
    public String  marka;
    public short silindirHacmi  ;
    public int  vergiHesapla(short sHacmi)
    {
         int  vergi = 0;
         sHacmi = silindirHacmi;
         if (sHacmi <= 1300) vergi = 405 ;
    else
         if (sHacmi <= 1600) vergi = 648 ;
    else
         if (sHacmi <= 1800) vergi = 1140 ;
    else
         if (sHacmi <= 2000) vergi = 1793 ;
    else
         if (sHacmi <= 2500) vergi = 2690 ;
    else
         if (sHacmi <= 3000) vergi = 3750 ;
    else
         if (sHacmi <= 3500) vergi = 5711 ;
    else
         if (sHacmi <= 4000) vergi = 8976 ;
    else
         if (sHacmi > 4000) vergi = 14689 ;
    return vergi;
    }
}
 
class Uygulama
{
    public static void main(String[] args)
    {
        Otomobil oto_1 = new  Otomobil();
         oto_1.marka = "Ford" ;
         oto_1.silindirHacmi = 2000 ;
         System.out.println(oto_1.vergiHesapla(oto_1.silindirHacmi));
    }
}