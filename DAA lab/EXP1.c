#include <stdio.h>
void Linearsearch(int arr[], int size, int desire) {
    int f = 0;
    int i;
    for (i = 0; i < size; i++) {
        if (arr[i] == desire) {
            printf("%d has been found on location %d\n", desire, i);
            f = 1;
            break; 
        }
    }
    if (f == 0) {
        printf("%d not found\n", desire);
    }
}
void Binarysearch(int arr[], int size, int desire) {
    int i, j, temp;
    for (i = 0; i < size - 1; i++) {
        for (j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    int low = 0;
    int high = size - 1;
    int f = 0;
    int mid;
    while (low <= high) {
        mid = (low + high) / 2;
        if (arr[mid] == desire) {
            printf("%d found in sorted array\n", desire, mid);
            f = 1;
            break;
        } 
        else if (desire < arr[mid]) {
            high = mid - 1;
        } 
        else {
            low = mid + 1;
        }
    }
    if (f == 0) {
        printf("%d not found\n", desire);
    }
}
int main() {
    int size, desire;
    int i;
    printf("Enter the size of the array: ");
    if (scanf("%d", &size) != 1) return 1; 
    int arr[size]; 
    printf("Enter elements: ");
    for (i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    printf("Enter value to search: ");
    scanf("%d", &desire);
    Linearsearch(arr, size, desire);
    Binarysearch(arr, size, desire);
    return 0;
}