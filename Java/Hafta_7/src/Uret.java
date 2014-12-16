public class Uret{
	public static void main(String[] args){
		Araba ar1 = new Araba(4);
		Araba ar2 = new Araba(4,5);
		Araba ar3 = new Araba();
		System.out.printf("%d %d\n", ar1.kapi_sayisi , ar2.kapi_sayisi);
		System.out.printf("%d", ar3.kapi_sayisi);
	}
}