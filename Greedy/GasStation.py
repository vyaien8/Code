class Solution:
    # Say you start at 'a' and get stuck at 'b'. Then you will still get stuck at 'b' no matter which station between 'a' and 'b' you start at.
    #Why? Because starting at a station 'a' gives you all the gas at that station. 
    # And on your journey from 'a' to 'b', each time you travel to the next station your gas might reduce but never below zero (until you reach b ). 
    # So for every station 'c' between 'a' and 'b', you will have gas>=0 when you reach there, even before refilling. 
    # Total gas you will have when you leave station 'c' (after refilling) will be, gas[c] plus whatever gas you already had, 
    # which makes the total gas greater than or equal to gas[c]. 
    # So if you cannot reach station 'b' when you start at 'c' with total gas >= gas[c], then you also can't reach station 'b' with total gas = gas[c].
    def canCompleteCircuit(self, gas: [int], cost: [int]):
        if sum(gas) < sum(cost): # if the gas we have less then the cost to go over the circuit
            return -1
        total = 0 
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i]) # the gas left after each position
            if total < 0: # if it less than 0, which mean we can't finish the circuit with that start index
                total = 0
                res = i + 1 # base on the idea above
        return res