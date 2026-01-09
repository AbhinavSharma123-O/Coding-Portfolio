#include <stdio.h>
int linearSearchRec(int arr[], int n, int key, int index) {
    if (index == n)
        return -1;
    if (arr[index] == key)
        return index;
    return linearSearchRec(arr, n, key, index + 1);}
int main() {
    int n, key, pos;
    int arr[50];
    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter elements:\n");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    printf("Enter element to search: ");
    scanf("%d", &key);
    pos = linearSearchRec(arr, n, key, 0);
    if (pos != -1){
        printf("Element found at position %d\n", pos + 1);}
    else{
        printf("Element not found\n");}
    printf("Abhinav Sharma\n2401020441");
    return 0;
}
