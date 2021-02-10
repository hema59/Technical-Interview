/*
To find the length of the common prefix in a given set of strings

Solution 1: using Binary Search
Solution 2: Divide and conquer method
Solution 3: Sorting
Solution 4: Tries

Example:

input: {"nutcracker","nutcase","nuts","nutty","nutririon"} / "feature","feats","feat","featoh"
output: 3
*/

#include<string.h>

string findShortestString(string input[], int numberofStrings){
//returns the shortest string in the given set of strings
string mini=input[0]; 
for(int i=1;i<numberofStrings;++i) {
  if(input[i].length()==0) return "";
  if(input[i].lenght()<mini.length()) mini=input[i];
  }
  return mini;
}
bool isPresent(string input[],int numberofStrings, char x,int index){
//checks is x is present at index position for all the strings
for(int i=0i<numberofStrings;++i){
 if(input[i][index]!=x)
    return false;
  }
return true;
}

int Solution1(strings input[], int numberofStrings){
/*flow: find the shortest string -> use BS to for the characters of the shortest string in the given set of strings
->everytime you get true then increase the length
O(n)=N*log(n) where N is the number of strings, and n is the number of characters in the shortest string
*/
string minString=findShortestString(string *input, int numberofStrings);
int left=0,right=minString.length()-1;
string prefix;
while(left<right){
  int mid=(left+right)/2;
  if(isPresent(input,numberofStrings,minString[mid],mid)) {
    prefix=prefix+input[0].substring(left,mid-left+1);
      left=mid+1;
    }
    else
     right=mid-1;
  }
cout<<"\ncommon prefix is: "<<prefix;
return prefix.length();
}
string helper2commonUntil(string x,string y){
string temp;
for(int i=0,j=0;i<x.length()-1 && j<y.length()-1;++i,++j){
if(x[i]==y[j])
   temp.push_back(x[i]);
  else
    break;
}
 return temp;
}

string helper2commonUntil(string x,string y){
string temp;
for(int i=0,j=0;i<x.length() && j<y.length();++i,++j){
 if(x[i]==y[j])
    temp.push_back(x[i]);
  else
    break;
 }
return temp;
}
string helper2(string input[],int numberofStrings,int begin,int end){
if(begin==end)
    return input[begin];
 if(begin<=end)
  {
    int mid=(begin+end)/2;
    string str1=helper2(input,numberofStrings,begin,mid);
    string str2=helper2(input,numberofStrings,mid+1,end);
    return helper2commonUntil(str1,str2);
  }
}
int Solution2(string input[],int numberofStrings){
/*
using divide and conquer: compare two strings at a time, find their common prefix and then repeat process for all strings;
O(M.N) time complexity we'll be performing comparisons on M charaters for N strings
(N log N) space
*/
int begin=0,end=numberofStrings-1;
string result=helper2(input,numberofStrings,begin,end);
return result.length();
 }
}
