#include <stdio.h>

/* Bubble Sort Function */
void bubbleSort(int arr[], int n) {
    int temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }}}}
int binarySearchRec(int arr[], int low, int high, int key) {
    if (low > high)
        return -1;
    int mid = (low + high) / 2;
    if (arr[mid] == key)
        return mid;
    else if (key < arr[mid])
        return binarySearchRec(arr, low, mid - 1, key);
    else
        return binarySearchRec(arr, mid + 1, high, key);}
int main() {
    int n, key, pos;
    int arr[50];
    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter elements:\n");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    bubbleSort(arr, n);
    printf("Sorted array:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\nEnter element to search: ");
    scanf("%d", &key);
    pos = binarySearchRec(arr, 0, n - 1, key);
    if (pos != -1)
        printf("\nElement found at position %d", pos + 1);
    else{
        printf("Element not found\n");
    printf("\nAbhinav Sharma\n2401020441");
    return 0;}} 
