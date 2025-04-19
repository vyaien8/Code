from heapq import *
class Solution:
    def isNStraightHand(self, hand: [int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        dic = {}
        for i in hand:
            dic[i] = dic.get(i, 0) + 1
        minH = list(dic.keys())
        heapify(minH)
        while minH:
            curMin = minH[0]
            for i in range(curMin, curMin + groupSize):
                if i not in dic:
                    return False
                dic[i] -= 1
                if dic[i] == 0:
                    if i != minH[0]: # if current min not the value pop
                        return False # which means in next loop, we can not create a consecutive group
                    heappop(minH)
        return True

                