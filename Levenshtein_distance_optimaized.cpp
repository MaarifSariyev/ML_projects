#include <iostream>
#include <vector>
using namespace std;

int levenshteinDistanceOptimized(const string &s1, const string &s2) {
    int m = s1.length(), n = s2.length();
    vector<int> prev(n + 1), curr(n + 1);

    for (int j = 0; j <= n; j++) prev[j] = j; // Initialize base case

    for (int i = 1; i <= m; i++) {
        curr[0] = i;
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1])
                curr[j] = prev[j - 1];
            else
                curr[j] = 1 + min({prev[j], curr[j - 1], prev[j - 1]});
        }
        prev = curr; // Move to the next row
    }

    return prev[n];
}

int main() {
    string str1, str2;
    cout << "Enter first string: ";
    cin >> str1;
    cout << "Enter second string: ";
    cin >> str2;

    cout << "Levenshtein Distance: " << levenshteinDistanceOptimized(str1, str2) << endl;

    return 0;
}
