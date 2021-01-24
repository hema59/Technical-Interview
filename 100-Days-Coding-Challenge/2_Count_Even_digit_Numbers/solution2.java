
class solution2{

    public static int countDigit( int n) {
        int c =0;
        while (n>0){
            n=n/10;
            c+=1;
        }
        return c;
    }
    public static int findEvenDigitNumbers( int[] nums){
        int res= 0;
        for(int i=0;i< nums.length;++i){
            if (countDigit(nums[i])%2 == 0)
                res+=1;
        }
        return res;
    }
    public static void main( String[] args){
        int[] array = {12,234,2678,0};
        System.out.println(findEvenDigitNumbers(array));
    }
}