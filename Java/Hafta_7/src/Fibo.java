public class Fibo{
	static int fibonacci(int sayi){
		if (sayi < 2)
			return sayi;
		else
			return(fibonacci(sayi-1) + fibonacci(sayi-2));
	}
	public static void main(String[] args){
		System.out.println(fibonacci(10));
	}
}