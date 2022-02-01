#include <iostream>
#include <string>
using namespace std;
class food{
public:
    string name;
    string color;
    int amount;
public:
    void set(void);
    void show(void);
};

void food :: set(void){
    cout << "Enter name, color and amount of fruit\n";
    cin >> name >> color >> amount;
}

void food :: show(void){
    cout << "Name: " << name << "\ncolor: " << color << "\namount: " << name;
}

int main(){
    food f[50];
    food* p = &f[1];
    for (int i=0;i<3;i++){
        f[i].set();
    }
    cout << *(p->name);
    return 0;
}