public class ParDondurReturn {
	public static double ToplamYap(double a, double b){
		double sonuc = a+b;
		return sonuc; //Deðer döndürür.
	}	
	public static void main(String[] args){
		System.out.println("Return deneme yapalim");
		System.out.println(ToplamYap(5,9));
	}
}
