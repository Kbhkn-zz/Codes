public class Radar {

	public static void main(String[] args){
		int hiz = 1300;
		if(hiz > 90){
			System.out.println("Radara yakalandýnýz ve ");
			if(hiz > 90 && hiz < 120)
				System.out.println("cezanýz 120 TL");
			else if(hiz > 119 && hiz < 150)
				System.out.println("cezanýz 140 TL");
			else
				System.out.println("cezanýz 300 TL");
			}
		else
			System.out.println("Hýzýnýz normal");
	}
}