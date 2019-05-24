/*
to insert an element into a sorted list

example:
input list: 3-5-7-10-20
new element: 6

output: 3-5-6-7-10-20

O(n)=log(n)
*/
struct node{
int value;
node *next;
node(x){
  value=x;
  next=NULL;
  }
};
void solution(node *list,int element){
node newNode=new node(element);
node *current=list;
while(current!=NULL) {
  if(current->next->value>element) { 
   newNode->next=current->next;
   current->next=newNode;
   } 
   else 
   current=current->next;
  }
}

