public class Radar {

	public static void main(String[] args){
		int hiz = 1300;
		if(hiz > 90){
			System.out.println("Radara yakaland�n�z ve ");
			if(hiz > 90 && hiz < 120)
				System.out.println("cezan�z 120 TL");
			else if(hiz > 119 && hiz < 150)
				System.out.println("cezan�z 140 TL");
			else
				System.out.println("cezan�z 300 TL");
			}
		else
			System.out.println("H�z�n�z normal");
	}
}