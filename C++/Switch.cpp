#include <iostream>
using namespace std;

int main(){
    int choice;
    cout<<"Select Application \n1)Temperature Converter\n2)Eligibilty Checker  - Voter \n3)Eligibilty Checker  - Insurance"<<endl;
    cout<<"Enter your Choice: ";
    cin>>choice;
    switch(choice){
    case 1:
        int Celsius, Fahernheit;
        cout<<"Enter Temperature in Celsius:";
        cin>>Celsius;
        Fahernheit = (Celsius * 9/5) + 32;
        cout<<"\nThe Given Temperature in Fahernheit is "<<Fahernheit;
        break;
    case 2:
        int age;
        cout<<"Enter your age:";
        cin>>age;
        if(age>=18){
            cout<<"You are eligible to vote"<<endl;
        }
        else{
            cout<<"You are not eligible to vote"<<endl;
        }
        break;
    case 3:
        char gender, married;
        cout<<"Are you married:(Married - Y, Unmarried - N):";
        cin>>married;

        if(married == 'Y' || married == 'y'){
            cout<<"You are eligible for the insurance";
        }
        else if(married == 'N' || married == 'n'){
            cout<<"\nEnter your Gender:(Male - M or Female - F)";
            cin>>gender;
            cout<<"\nEnter your age:";
            cin>>age;
            // if(((gender == 'M' || gender == 'm') && age > 30)){
            //     cout<<"you are eligible for the insurance";
            // }
            // else if(((gender == 'F' || gender == 'f') && age > 25)){
            //      cout<<"you are eligible for the insurance";
            // }
            // else{
            //     cout<<"you are noteligible for the insurance";
            // }
            if(((gender == 'M' || gender == 'm') && age > 30) || ((gender == 'F' || gender == 'f') && age > 25) ){
                cout<<"you are eligible for the insurance";
            }
            else{
                cout<<"you are not eligible for the insurance \nor \nInvalid Gender input";
            }
        }
        else{
            cout<<"Invalid Martial input ";
        }
        break;
    default:
        cout<<"Invalid input";    


    }
    return 0;
}