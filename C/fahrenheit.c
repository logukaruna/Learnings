#include<stdio.h>
int main(){
    float F, C;
    
    printf("\nEnter the temperture of the city in Fahrenheit ");
    scanf("%f",&F);
    C = (F - 32) * 5/9;
    printf("\nThe temperture of the city in celsius is %0.2f",C);
    return 0;
}