class Harf {
		char c;
}
public class Pas {
	static void f(Harf h) { // Harf tipine dikkat edelim ��nk� char olarak tan�mlanm�� ve �yle de�er alm��.
		h.c = 'z';
	}
	public static void main(String[] args) {
		Harf x = new Harf(); //Harf nesnesini olu�turuyor.
		x.c = 'a';			 // Harf nesnesinin c alan�na de�er atand�.
		System.out.println("1: x.c: " + x.c);
		f(x);
		System.out.println("2: x.c: " + x.c); // Cevap 'z' olur.
	}
}	