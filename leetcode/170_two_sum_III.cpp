class TwoSum {
public:

    map<int, int> mp;

    TwoSum() {
        this->mp = mp;
    }
    
    void add(int number) {
        mp[number]++;
    }
    
    bool find(int value) {
        for (auto i : mp) {
            long long compliment = static_cast<long long>(value) - i.first;
            if (compliment != i.first) {
                if (mp.find(compliment) != mp.end()) {
                    return true;
                }
            } else {
                if (i.second > 1) {
                    return true;
                }
            }
        }

        return false;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
