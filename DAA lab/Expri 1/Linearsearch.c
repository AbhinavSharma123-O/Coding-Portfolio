#include <stdio.h>
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i;}
    return -1;}
int main() {
    int n, key, pos;
    int arr[50];
    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter elements: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    printf("Enter element to search: ");
    scanf("%d", &key);
    pos = linearSearch(arr, n, key);
    if (pos != -1){
        printf("Element found at position %d ", pos + 1);}
    else{
        printf("Element not found ");}
    printf("\nAbhinav Sharma\n2401020441");
    return 0;}
