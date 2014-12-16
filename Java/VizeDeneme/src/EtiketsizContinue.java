public class EtiketsizContinue {
	public static void main(String[] args){
		for(int i=0;i<100;i++){
			if(i==9)
				continue;
			System.out.println("i =" +i); // 0,1,2,3,4,5,6,7,8,10,...,99,100 devam eder 9'u pas geçer.
		}
		System.out.println("Döngü sonu");
	}
}