/* MWC '15 #2 P2 - Towering Towers */

// yeah idk either im pretty sure bruce did this one for me

#include <bits/stdc++.h>
using namespace std;

const int MM = 1e6;
int n, h[MM], ans[MM];

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    cin >> n; // number of towers

    for (int i = 0; i < n; i++) cin >> h[i]; // height of towers
    stack<int> stk; 

    for (int i = 0; i < n; i++) {
        while(!stk.empty() && h[stk.top()] <= h[i]){
            stk.pop();
        }

        if (stk.empty()) ans[i] = i;
        else ans[i] = i - stk.top();
        stk.push(i);
    }
    for(int i = 0; i < n; i++) cout << ans[i] << " ";
}
