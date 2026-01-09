#include <stdio.h>
#include <stdlib.h>

// Global variable to count exchanges
int exchange_count = 0; 

// --- Function for User Input ---
void userinput(int **arr, int *n) {
    printf("Enter the number of elements: ");
    scanf("%d", n); 
    
    *arr = (int*)malloc(*n * sizeof(int));
    if (*arr == NULL) {
        printf("Memory allocation failed!\n");
        exit(1); 
    }
    
    printf("Enter %d integers:\n", *n);
    for (int i = 0; i < *n; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &(*arr)[i]); 
    }
}

// --- Swap Function ---
void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
    exchange_count++; // Count the swap
}

// --- Partition Function ---
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; 
    int i = (low - 1); 
    
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]); 
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1); 
}

// --- Recursive Quick Sort ---
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high); 
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high); 
    }
}

// --- Main Driver ---
int main() {
    int *arr;
    int n; 
    
    // 1. Get Input
    userinput(&arr, &n); 
    
    printf("\nUnsorted Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]); 
    }
    printf("\n");
    
    // 2. Sort
    exchange_count = 0; 
    quickSort(arr, 0, n - 1); 
    
    // 3. Output
    printf("Sorted Array:   ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]); 
    }
    printf("\n");
    printf("Total Exchanges: %d\n", exchange_count); 
    
    printf("\nAbhinav Sharma\n2401020441\n");
    
    free(arr);   
    return 0; 
}