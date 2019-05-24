/* to merge k sorted arrays and return the final array
example:
array1: 2,3,5,7
array2: -4,0,5
array3: 1,4,7,9,100

merged_array: -4,0,1,2,3,4,5,5,7,7,9,100

NOTE: solved by merging two arrays at a time, with O(k)= N*log(k), where N is the number of elements in kth array
*/

vector<int>merge(vector<int>a, vector<int>b){
int j=0,i=0,length_a=a.size()-1,length_b=b.size()-1;
vector<int> temp; 
temp.clear();
while(temp.size()<(length_a+length_b)) {
  if(a[i]<b[j])
    temp.push_back(a[i++]);
    else
    temp.push_back(b[j++]);
  }
  return temp;
}
vector<int> merge_sorted_arrays(vector<vector<int>> arrayList){
  vector<int>result=arrayList[0];   //pointing to the first array
  for(int i=1;i<arrayList.size()-1;++i){
      result=merge(result,arrayList[i]);
       }
 return result;
}
