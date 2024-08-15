#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n,m;
    cin >> n;
    cin >> m;
    int x = n*m;
    int arr_just[x],arr_vill[x];
    for (int i = 0; i<x; i++)
    {
        cin >> arr_just[i];
    }
    for (int i = 0; i<x; i++)
    {
        cin >> arr_vill[i];
    }
    int score_just = 0, score_vill = 0;
    for (int i = 0; i<x; i++)
    {
        if (arr_just[i]>arr_vill[i])
        {
            score_just++;
        }
        if (arr_just[i]<arr_vill[i])
        {
            score_vill++;
        }
    }
    if (score_just==score_vill)
    {
        cout << "Tie";
    }
    if (score_just>score_vill)
    {
        cout << "Justice League";
    }
    if (score_just<score_vill)
    {
        cout << "Villains";
    }
}

