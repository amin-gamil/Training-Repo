#include <iostream>
#include <string>
using namespace std;
int main()
{
    string hero;
    getline(cin, hero);
    if (hero.length()<=100)
    {
        cout << "Hello, " << hero << "!\n";
    }

}
