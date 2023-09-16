#include <iostream>

using namespace std;

class Mobile{
    public:
        string Brand;
        string Model;
        int year;
};
int main(){

    Mobile myobj;
    myobj.Brand = "Samsung";
    myobj.Model = "M31";
    myobj.year = 2020;

    cout<<"Brand: "<<myobj.Brand<<endl;
    cout<<"Model: "<<myobj.Model<<endl;
    cout<<"year: "<<myobj.year<<endl;

    return 0;


}
