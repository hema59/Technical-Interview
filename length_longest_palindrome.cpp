/*
to find the length of the longest palindrome

example:
input: madamtussuds
output: 5

O(n): n.long(n)
*/

int solution(string input){
int max=0,i=0,j=0,k=0;
int str_len=input.size()-1;
bool mem[str_len][str_len];
memset(mem,0,size_of(mem)); //sets all values to 0

//set true for individual character
for(i=0;i<str_len;++i)
  mem[i][i]=true;
 
 //check for string length 2
for(i=0;i<str_len;i+=2){
  if(str[i]==str[i+1])
    {
    mem[i][i+1]=true;
    max=2;
    }
  }

//check for the rest of the 
for(k=3;k<str_len;++k){
  for(i=0;i<str_len;++i){
    j=i+k-1;
    if(mem[i+1][j-1] && str[i]==str[j]){
      if(max<k) max=k;
      }
    }
  }
return max;
}
