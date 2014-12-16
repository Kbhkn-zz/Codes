
public class test {

	public static void main(String[] args) {
		int sayi = 15;
		String s1 = String.valueOf(sayi); //Yöntem 1
		String s2 = sayi + "";			  //Yöntem 2
		String s3 = Integer.toString(sayi);
		String x = "20";
		int sayi1 = Integer.valueOf(x);
		int sayi2 = Integer.parseInt(x);		
		System.out.println("sayi degeri: " +sayi);
		System.out.println("s1 degeri: " +s1);
		System.out.println("s2 degeri: " +s2);
		System.out.println("s3 degeri: " +s3);
		System.out.println("x degeri: " +x);
		System.out.println("sayi1 degeri: " +sayi1);
		System.out.println("sayi2 degeri: " +sayi2);		
	}

}
