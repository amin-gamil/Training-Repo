#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int i = 1;
    while(i<=n&&n<=100)
    {
        cout << string(i, '*') << "\n";
        i++;
    }
    cout << "\n";
}
