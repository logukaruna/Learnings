#include<stdio.h>
#include<string.h>
int main(){
    char a[10],b[10];
    int c;
    printf("\nEnter the  string or word which to be checked whether it is a palidrome or not : ");
    gets(a);
    strcpy(b,a);
    printf("\nThe Reverse of given string is %s",strrev(a));
    printf("\n%s",b);
    c = strcmp(b,a);
    printf("\n%d",c);
    if(c==0){
        printf("\nThe Given string is a palindrome");
    }else{
        printf("\nThe Given string is not a palindrome");
    }

    

    return 0;
}