#include <stdio.h>

int main(){
    int Tamil,English,Maths,Science,Social,Total;
    float Precentage;
    printf("Enter Tamil Marks: ");
    scanf("%d",&Tamil);
    printf("\nEnter English Marks: ");
    scanf("%d",&English);
    printf("\nEnter Maths Marks: ");
    scanf("%d",&Maths);
    printf("\nEnter Science Marks: ");
    scanf("%d",&Science);
    printf("\nEnter Social Marks: ");
    scanf("%d",&Social);
    Total = Tamil+English+Maths+Science+Social;
    printf("\nTotal Marks out of 500 is %d",Total);
    Precentage = ((float)Total/500)*100;
    printf("\n\nPrecentage of %d is %f",Total,Precentage);


    return 0;

}