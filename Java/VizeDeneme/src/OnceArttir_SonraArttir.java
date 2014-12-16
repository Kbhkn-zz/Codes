
public class OnceArttir_SonraArttir {

	public static void main(String[] args) {
		int sayi1 = 5;
		int sayi2 = 5;
		int OA = ++sayi1;
		int SA = sayi2++;
		System.out.println("Sayi1 degeri: " +sayi1);
		System.out.println("Sayi2 degeri: " +sayi2);
		System.out.println("Önce arttir degeri: " +OA);
		System.out.println("Sonra arttir degeri: " +SA);
		int OE = --sayi1;
		int SE = sayi2--;
		System.out.println("Sayi1 degeri: " +sayi1);
		System.out.println("Sayi2 degeri: " +sayi2);
		System.out.println("Önce eksilt degeri: " +OE);
		System.out.println("Sonra eksilt degeri: " +SE);

	}

}
