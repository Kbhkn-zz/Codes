import java.util.Scanner;
	
class Depo1{
	public static void main(String args[]){
		kutu k1 = new kutu();
		kutu k2 = new kutu();
		String k�r�lgan;
		
		Scanner input = new Scanner(System.in);
		System.out.print("1.Kutunun boyunu giriniz: ");
		k1.x=input.nextDouble();
		
		System.out.print("1.Kutunun enini giriniz: ");
		k1.y=input.nextDouble();
		
		System.out.print("1.Kutunun y�ksekli�ini giriniz: ");
		k1.z=input.nextDouble();
		
		System.out.print("1.Kutu K�r�lgan m� true/false: ");
		k1.kirilir=input.nextBoolean();
		if(k1.kirilir == true)
			k�r�lgan = "k�r�lgan e�ya i�erir";
		else
			k�r�lgan = "k�r�lgan e�ya i�ermez";
		
		System.out.print("1.Kutu i�in taban kodu giriniz: ");
		k1.taban_kodu=input.nextInt();
		
		k2.x=5.0; k2.y=10.0; k2.z=7.5;
		
		System.out.print("\n1.Kutunun hacmi: " + (k1.x*k1.y*k1.z) + "\n");
		if(k1.taban_kodu == 0)
			System.out.print("1.Kutunun alt k�sma gelecek y�zey numaras� : Farketmez");
		else
			System.out.print("1.Kutunun alt k�sma gelecek y�zey numaras� : " + (k1.taban_kodu));
		System.out.print("\n1.Kutu " + (k�r�lgan));
		System.out.print("\n2.Kutunun hacmi: " + (k2.x*k2.y*k2.z) + "\n");
	}
}