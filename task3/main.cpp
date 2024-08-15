#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    long long arr[n];
    for (int i = 0; i<n; i++)
    {
        cin >> arr[i];
    }
    cout << *max_element(arr, arr + n);

}
