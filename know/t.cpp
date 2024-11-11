#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct process
{
    string name;
    int arrivalTime;
    int burstTime;
    bool state = false;
    process()
    {
    }
    process(string name, int arrivalTime, int burstTime, bool state)
    {
        this->name = name;
        this->arrivalTime = arrivalTime;
        this->burstTime = burstTime;
        this->state = state;
    }
};

void solve()
{

    int n;
    cin >> n;
    vector<process> v;
    for (int i = 0; i < n; i++)
    {
        process p;
        cin >> p.name >> p.arrivalTime >> p.burstTime;
        v.push_back(p);
    }

    sort(v.begin(), v.end(), [](const process &a, const process &b)
         {
        if(a.arrivalTime==b.arrivalTime){
            return a.burstTime<b.burstTime;
        }
        return a.arrivalTime<b.arrivalTime; });

    int timer = 0, completion = 0;
    while (completion < n)
    {

        int tmp = completion;
        for (int i = 0; i < n; i++)
        {
            if (v[i].arrivalTime <= timer && !v[i].state)
            {

                v[i].state = true;
                cout << v[i].name << " " << timer << endl;
                timer += v[i].burstTime;
                completion++;
                break;
            }
        }

        if (tmp == completion)
        {
            for (int i = 0; i < n; i++)
            {
                if (v[i].arrivalTime > timer && !v[i].state)
                {
                    timer = v[i].arrivalTime;
                    break;
                }
            }
        }
    }
}

int main()
{
    solve();
}