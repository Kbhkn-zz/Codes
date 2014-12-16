
public class Kestirme {
	
	public static boolean hesaplaBir (int a) {
		
		System.out.println("Hesaplabir'e girildi.");
		return a>1;
	}
	
	public static boolean hesaplaIki (int a) {
		
		System.out.println("HesaplaIki'e girildi.");
		return a>2;
	}
	
	public static void main(String[] args){
		System.out.println("Baþlangýç");
		System.out.println("hesaplaBir(0) && hesaplaIki(3)");
		
		if(hesaplaBir(0) && hesaplaIki(3))
			System.out.println("1 -true ");
		else
			System.out.println("1 -false");
		
		System.out.println("---------------");
		System.out.println("hesaplaBir(0) || hesaplaIki(3)");
		
		if(hesaplaBir(0) || hesaplaIki(3))
			System.out.println("2 -true");
		else
			System.out.println("2 -false");
	}
}
