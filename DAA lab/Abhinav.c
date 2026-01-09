#include <stdio.h>
int main() {
    int age;
    // The \n is CRITICAL. It forces the text to appear before the program pauses.
    printf("Please enter your age:\n"); 
    scanf("%d", &age);
    printf("You are %d years old.\n", age);
    return 0;
}