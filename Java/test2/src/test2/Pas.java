package test2;

class Harf {
	char c;
}

public class Pas {
	static void f(Harf h) {
		h.c = 'z';
	}
	
	public static void main(String[] args) {
		Harf x = new Harf(); //Harf nesnesini olu�turuyor.
		x.c = 'a';			 // Harf nesnesinin c alan�na de�er atand�.
		System.out.println("1: x.c: " + x.c);
		
		f(x); //dikkat
		
		System.out.println("2: x.c: " + x.c);
	}
}
