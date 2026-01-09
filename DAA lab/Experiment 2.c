#include<stdio.h>
void merge(int A[],int p,int q,int r){
    int n=q-p+1;
    int m=r-q;
    int i;
    int j;
    int l[n];
    int R[m];
    for(i=1;i<=n;i++){
        l[i]=A[p+i-1];}
    for(j=1;j<=m;j++){
        R[j]=A[q+1];
    } 
    int a=1,b=1,k;
    for(k=p;p<=r;p++){
        if(l[a]<=R[b]){
            A[k]=l[a];
            i=i+1;
        }
        else{
            A[k]=l[i];
            b=b+1;
        }
    }
}
void Mergesort(int A[],int p,int r){
    if(p>r){
        return; 
    }
    int q=(p+r)/2;
    Mergesort(A,p,q);
    Mergesort(A,q+1,r);
    merge(A,p,q,r);
}
int main() {
    int size=5;
    int i;
    int arr[size]; 
    printf("Enter elements:");
    for (i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    Mergesort(arr,0,size-1);
    printf("Sorted array:");
    for (i = 1; i < size; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
    }}