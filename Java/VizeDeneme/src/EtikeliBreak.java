public class EtikeliBreak {
	public static void main(String[] args){
		kiril:		
		for(int j=0;j<4;j++){
			for(int i=0;i<5;i++){
				if(j == 2)
					break kiril;
				System.out.println("i= " +i);
			}
			System.out.println("D�ng� sonu");
		}// Etiketsiz break Ekran ��kt�s� : 0,1,2,3,4,5,6,7,8  sayar ve her defas�nda D�ng� sonu yazar.
	}//Etiketli break Ekran ��kt�s�: 
}