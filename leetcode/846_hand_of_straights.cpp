class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize != 0) {
            return false;
        }

        // check if split into group size, can they be all consecutive?
        // count occurrences of numbers in the hand, via hash map
        map<int,int> occurrences; // num: count
        for (const int& num : hand) {
            occurrences[num]++;
        }

        // loop through hash map, and count up to groupSize while decrementing. If next number is == 0, return false
        // {8 : 1, 7 : 1, 6 : 1, ....}

        // 1:2, 2:2, 3:2 --> 1:1 2:1 3:1 --> 1:0 2:0 3:0

        // loop through map
        for (const auto& pair : occurrences) {
            // starting from smallest, if it appears more than once
            while (pair.second > 0) {
                int begin = pair.first;
                int length = 0;
                while (length < groupSize) {
                    if (occurrences[begin + length] > 0) {
                        occurrences[begin + length]--;
                    } else {
                        return false;
                    }
                    length++;
                }
            }
        }

        return true;

    }
};
