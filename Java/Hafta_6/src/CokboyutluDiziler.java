
public class CokboyutluDiziler {

	public static void main(String[] args) {
		int ikiboyut[][] = new int[3][];
		ikiboyut[0] = new int[2];
		ikiboyut[1] = new int[1];
		ikiboyut[2] = new int[3];
		ikiboyut[0][0] = 89;
		ikiboyut[0][1] = 32;
		ikiboyut[1][0] = 5;
		//ikiboyut[1][1] = 35; HATALIDIR çünkü 1.boyutunda 1 elemanlý yarattýk.
		ikiboyut[2][0] = 60;
		ikiboyut[2][1] = 78;
		ikiboyut[2][2] = 49;
		System.out.println(ikiboyut[2].length);
		//System.out.println(ikiboyut[1][0]);
	}
	
}