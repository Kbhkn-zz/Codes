public class ParametreliMetot { //Sýnýf ismi
	public static int ortala(int a, int b){ //Parametreli metot a ve b local deðiþkenler 
		int t =0;
		t = (a+b)/2;
		System.out.println(t);
		return t;
	}

	public static void main(String[] args) { // main isimli ana metot.
		System.out.println("4 ile 6 ortalamasý: ");
		ortala(4,6); // Metot çaðrýmý
	}
} // class sonu ayýracý