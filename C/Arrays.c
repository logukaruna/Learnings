#include<stdio.h>
int main(){

    int a[100][100], b[100][100], c[100][100];
    int i,j,n,m;

    printf("\nEnter the number of Rows: ");
    scanf("%d",&n);
    printf("\nEnter the number of Columns: ");
    scanf("%d",&m);
    //Getting the value of Array A and storing it to a
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            printf("\nEnter the value of a[%d][%d]", i, j);
            scanf("%d",&a[i][j]);
        }
        
    }
    //Getting the value of Array B and storing it to b
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            printf("\nEnter the value of b[%d][%d]", i, j);
            scanf("%d",&b[i][j]);
        }
        
    }
    //Adding the value of Array A and B then storing it to c
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
           c[i][j] = a[i][j] + b[i][j];
           printf("\t %d", c[i][j]);
        }
        printf("\n");
    }



    return 0;
}