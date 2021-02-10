/*
Find longest substring of non-repeating characters

example:
input: ABADERSB

output: 4 
Because the longest non-repeating substring is ADERSB
*/
int solution(string input){
 unordered_map<int,char> hashset;
 unordered_map<int,char>::iterator i;
 
 int i=0,string_length=string.lenght();
 int j=0,count=0,max=0;
 while(i<string_length){
  i=hashset.find(input[i]);
  if(i==hashset.end())  //if input[i] doesn't exist in the hash table
    {
     hashset.insert(make_pair<int&,char>(j++,input[i++]));
     count++;
     }
     else
     {
     if(count>max) max=count;
     hashset.clear();
     count=1,j=0;
     }
  }
  return max;
 }
