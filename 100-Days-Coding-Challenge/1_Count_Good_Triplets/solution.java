public class solution{
    public static int function(int[] array, int a, int b,int c ){
        int count =0;
        int arrayLength = array.length;

        for (int i=0; i < arrayLength-2; ++i){
            for (int j=i+1; j < arrayLength-1; ++j) {
                int abs1 = Math.abs(array[i]-array[j]);
                if (abs1 > a)
                    break;
                else
                    for (int k=j+1; k <arrayLength;++k){
                        if ( Math.abs(array[j]-array[k]) <= b &&  Math.abs(array[i]-array[k]) <= c)
                            count +=1;
                    }
            }
        }
        return count;
    }
    public static void main( String[] args){
        int[] array = {3,0,1,1,9,7};
        int result = function(array,7,2,3);
        System.out.println( result );
    }
}