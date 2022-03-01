#include <stdio.h>
int main() {

   char str[1000];

   printf( "Enter the Ciphertext: ");
   scanf("%s", str);

   printf( "\nMy Plaintext guess is: %s\n", str);

   return 0;
}