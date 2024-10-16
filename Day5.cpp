#include <iostream>
using namespace std;

int main(){
    int ip;
    cout<<"Enter a number to check parity : " <<endl;
    cin>> ip;

    if (ip % 2 == 0){
    cout<<"Given number is an even number"<<endl;
    }

    else{
    cout<<"Given number is an odd number "<<endl;
    }
}
