public class EtikeliBreak {
	public static void main(String[] args){
		kiril:		
		for(int j=0;j<4;j++){
			for(int i=0;i<5;i++){
				if(j == 2)
					break kiril;
				System.out.println("i= " +i);
			}
			System.out.println("Döngü sonu");
		}// Etiketsiz break Ekran çýktýsý : 0,1,2,3,4,5,6,7,8  sayar ve her defasýnda Döngü sonu yazar.
	}//Etiketli break Ekran Çýktýsý: 
}