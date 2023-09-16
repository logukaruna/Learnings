#include <iostream>
using namespace std;

class Students{
    public:
        string name;
        int rollno;
        float Marks[5];
};

void inputDetials(Students& students){

    cout<<"Enter the Name of the Student: ";
    cin>>students.name;
    cout<<"\nEnter the Roll.No of the Student: ";
    cin>>students.rollno;
    int i;
    for(i=0;i<5;i++){
        cout<<"\nEnter Mark of Subject "<<i+1<<":";
        cin>>students.Marks[i];
    }

}
void CalculateGrade(const Students& students){
    float avg, total=0;
    int i;
    for(i=0;i<=5;i++){
        total += students.Marks[i];
    }
    avg = total/5.0;
    cout<<"\nTotal Marks of "<<students.name<<" is "<<total<<"\n";
    cout<<"\nAverage Marks of "<<students.name<<" is "<<avg<<"\n";
    if(avg>=90){
        cout<<"\nThe Grade of "<<students.name<<" is "<<"A";
    }
    else if(avg>=80 && avg<=89){
        cout<<"\nThe Grade of "<<students.name<<" is "<<"B";
    }
    else if(avg>=70 && avg<=79){
        cout<<"\nThe Grade of "<<students.name<<" is "<<"C";
    }
    else if(avg>=60 && avg<=69){
        cout<<"\nThe Grade of "<<students.name<<" is "<<"D";
    }
    else{
        cout<<"\nThe Grade of "<<students.name<<" is "<<"F";
    }

    

}
int main(){
    Students myobj;
    int i, limit;
    cout<<"\nEnter Number of students in your class: ";
    cin>>limit;
    for(i=1;i<=limit;i++){
        inputDetials(myobj);
        CalculateGrade(myobj);

    }
    return 0;
}