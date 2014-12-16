class Harf {
		char c;
}
public class Pas {
	static void f(Harf h) { // Harf tipine dikkat edelim çünkü char olarak tanýmlanmýþ ve öyle deðer almýþ.
		h.c = 'z';
	}
	public static void main(String[] args) {
		Harf x = new Harf(); //Harf nesnesini oluþturuyor.
		x.c = 'a';			 // Harf nesnesinin c alanýna deðer atandý.
		System.out.println("1: x.c: " + x.c);
		f(x);
		System.out.println("2: x.c: " + x.c); // Cevap 'z' olur.
	}
}	