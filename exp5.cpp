#include <iostream>
#include <string>
using namespace std;

class employee{
    static int count;
    private:
    string name;
    int salary, insurance = 2000;
    public:
    void set(){
            cout << "Enter your name, salary of employye no " << count;
    cin >> name >> salary;
    count++;
    }
    void calcandshow();{
    cout << "Name: " << name << "\n Cash in hand= " << salary - insurance << endl;
}
};
int employee :: count;
int main(){
    class employee e[50];
    for (int i=0;i<3;i++){
        e[i].set();
    }
    for (int i=0;i<3;i++){
        e[i].calcandshow();
    }
return 0;
}