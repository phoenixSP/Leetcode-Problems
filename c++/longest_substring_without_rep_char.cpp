#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include < algorithm>
using namespace std;

#define NO_OF_CHARS 256

#include <iostream>
#include<vector>
using namespace std;

int lengthOfLongestSubstring(string s) {
	vector<int> dict(256, -1);
	int maxLen = 0, start = -1;
	for (int i = 0; i != s.length(); i++) {
		cout << s[i] << endl;
		cout << dict[s[i]] << endl;
		if (dict[s[i]] > start)
			start = dict[s[i]];
		dict[s[i]] = i;
		maxLen = max(maxLen, i - start);
	}
	return maxLen;
}

int main()
{
	string s = "stringg";
	int c = lengthOfLongestSubstring(s);
	cout << c;

	return 0;
}


