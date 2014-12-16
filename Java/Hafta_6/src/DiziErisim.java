public class DiziErisim {
	public static void main(String[] args) {
		double[] d = {1.2,3.4,7.8,2.1};
		for(int i=0;i<d.length;i++){
			System.out.println("d["+i+"]=" + d[i]);
			//System.out.println("d[" +i+ "]" + d[78]); DERLER AMA ÇALIÞTIRNCA HATA VERÝR.
			d[60] = 2;// DERLER AMA ÇALIÞTIRINCA HATA VERÝR.
		}
	}
}
