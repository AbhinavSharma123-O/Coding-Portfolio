#include <stdio.h>
void swap(int arr[], int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
void minHeapify(int arr[], int n, int i)
{
    int root = i;
    int left = 2*i + 1;
    int right = 2*i + 2;
    if (left < n && arr[left] < arr[root])
        root = left;
    if (right < n && arr[right] < arr[root])
        root = right;
    if (root != i)
    {
        swap(arr, i, root);
        minHeapify(arr, n, root);
    }
}
void maxHeapify(int arr[], int n, int i)
{
    int root = i;
    int left = 2*i + 1;
    int right = 2*i + 2;

    if (left < n && arr[left] > arr[root])
        root = left;

    if (right < n && arr[right] > arr[root])
        root = right;

    if (root != i)
    {
        swap(arr, i, root);
        maxHeapify(arr, n, root);
    }
}
int main()
{
    int n;
    scanf("%d", &n);
    int minHeap[n], maxHeap[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &minHeap[i]);
        maxHeap[i] = minHeap[i];
    }
    for (int i = n/2 - 1; i >= 0; i--)
        minHeapify(minHeap, n, i);
    for (int i = n/2 - 1; i >= 0; i--)
        maxHeapify(maxHeap, n, i);
    for (int i = 0; i < n; i++)
        printf("%d ", minHeap[i]);
    printf("\n");
    for (int i = 0; i < n; i++)
        printf("%d ", maxHeap[i]);
    return 0;
}