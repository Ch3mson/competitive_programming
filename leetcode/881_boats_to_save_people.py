class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # n people
        # limit:
            # if weight >= limit, 
            # dictionary?
        
        people.sort()
        l = 0
        r = len(people) - 1
        output = 0

        while l <= r:
            if people[r] >= limit:
                r -= 1
            elif people[l] + people[r] > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            output += 1
        return output