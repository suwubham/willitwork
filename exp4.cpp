#include <iostream>
#include <string>
using namespace std;

class Cars
{
private:
    string color, name;

public:
    void set(void);
    void show(void);
};

void Cars :: set(void)
{
    cout << "Enter name of car\n";
    cin >> name;
    cout << "Enter color of car\n";
    cin >> color;
}

void Cars :: show(void){
    cout << name << " is " << color << " in color.";
}

int main()
{
    Cars car1;
    car1.set();
    car1.show();

    return 0;
}