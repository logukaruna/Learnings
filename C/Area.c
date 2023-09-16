#include<stdio.h>
int main(){
    float Length, Breadth, Radius, Rect_Area, Peri_Rect, Area_circ, Circum_Cir;

    printf("\nEnter the Length and Breadth of the Reactangle ");
    scanf("%f %f",&Length, &Breadth);
    printf("\nEnter the radius of the circle ");
    scanf("%f", &Radius);
    Rect_Area = Length * Breadth;
    Peri_Rect = 2*(Length + Breadth);
    Area_circ = 3.14 * Radius * Radius;
    Circum_Cir = 2 * 3.14 * Radius;
    printf("\nThe Area of Rectangle is %0.2f", Rect_Area);
    printf("\nThe Perimeter of the Rectangle is %0.2f", Peri_Rect);
    printf("\nThe Area of Circle is %0.2f", Area_circ);
    printf("\nThe Circumfrance of the Circle is %0.2f", Circum_Cir);
    return 0;

}