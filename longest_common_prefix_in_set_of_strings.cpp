/*
To find the length of the common prefix in a given set of strings

Solution 1: using Binary Search
Solution 2: Divide and conquer method
Solution 3: Sorting
Solution 4: Tries

Example:

input: {{nutcracker},{nutcase},{nuts},{nutty},{nutririon}}
output: 3
*/

#include<string.h>

string findShortestString(string *input, int numberofStrings){
//returns the shortest string in the given set of strings
string mini=input[0]; 
for(int i=1;i<numberofStrings;++i) {
  if(input[i].length()==0) return "";
  if(input[i].lenght()<mini.length()) mini=input[i];
  }
  return mini;
}

int Solution1(strings *input, int numberofStrings){
/*flow: find the shortest string -> use BS to for the characters of the shortest string in the given set of strings
->everytime you get true then increase the length
O(n)=N*log(n) where N is the number of strings, and n is the number of characters in the shortest string
*/
string minString=findShortestString(string *input, int numberofStrings);
int count=0,left=0,right=minString.length()-1;
string prefix;
while(left<right){
  int mid=(left+right)/2;
  if(isPresent(input,minString[mid])) {
    left=mid+1;
    prefix=prefix+input[0].substring(left,mid-left+1);
    count++;
    }
    else
     right=mid-1;
  }

return count;
}
