#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n] = {};
    for (int i = 0; i<n; i++)
    {
        cin >> arr[i];
    }
    int target ;
    int flag = -1;
    cin >> target;
    for(int i = 0; i < n; i++)
    {
        if(arr[i] == target)
        {
            flag = i;
            break;
        }
    }
    cout << flag;
}
