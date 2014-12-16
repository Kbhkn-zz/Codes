
public class yordam2{
	
	public int ToplamaYap(int a, int b){
		int sonuc = a+b;
		System.out.println("sonuc1: " + sonuc);
		return sonuc;
	}
	
	public void ToplamaYap(int a, double b){
		double sonuc = a+b;
		System.out.println("sonuc2: " + sonuc);
	}
	
	public double ToplamaYap(double a, int b){
		double sonuc = a+b;
		System.out.println("sonuc3: " + sonuc);
		return sonuc;
	}
	
	public void ToplamaYap(double a, double b){
		double sonuc = a+b;
		System.out.println("sonuc4: " + sonuc);
	}
	
	public static void main(String[] args){
		yordam2 metod2 = new yordam2();
		
		metod2.ToplamaYap(3,4);
		metod2.ToplamaYap(3,5.5);
		metod2.ToplamaYap(6.8,4);
		metod2.ToplamaYap(9.2, 12.3);
	}
}