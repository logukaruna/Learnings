#include<stdio.h>
int main(){

    int ch;
    printf("\n1) Voting Eligiblity Checker \n2) Marks and Average\n3) Temperture Converter\n ");
    printf("\n \nEnter Operation/service to be done:");
    scanf("%d",&ch);
    switch(ch){
        case 1:{
            int age;
            printf("\nEnter your age: ");
            scanf("%d",&age);
            age>18?printf("You are eligible for voting."):printf("You are not eligible to voting");
            break;
        }
        case 2:{
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
            break;
        }
        case 3:{
            int ch;
            printf("\n1) Fahrenheit Converter \n2) Celsius Converter ");
            printf("\n \nEnter Operation/service to be done:");
            scanf("%d",&ch);
            switch(ch){
                case 1:{
                    float F, C;
                    printf("\nEnter the temperture in Fahrenheit ");
                    scanf("%f",&F);
                    C = (F - 32) * 5/9;
                    printf("\nThe temperture in celsius is %0.2f",C);
                    break;
                }
                case 2:{
                    float F, C;
                    printf("\nEnter the temperture in celsius ");
                    scanf("%f",&C);
                    F = (C * 9/5) + 32;
                    printf("\nThe temperture in Fahrenheit is %0.2f",F);
                    break;
                }
            }

        }

    }

    return 0;
}