from heapq import *
class Twitter:

    def __init__(self):
        self.count = 0
        self.follower = {}
        self.post = {}
    def postTweet(self, userId: int, tweetId: int):
        self.count -= 1
        if userId not in self.follower:
            self.follower[userId] = {userId}
        if userId not in self.post:
            self.post[userId] = set()
        self.post[userId].add((self.count, tweetId))
    def getNewsFeed(self, userId: int):
        posts = []
        if userId in self.follower:
            for fid in self.follower[userId]:
                if fid in self.post: 
                    posts += self.post[fid]
        res = []
        heapify(posts)
        while posts and len(res) < 10:
            res.append(heappop(posts)[1])
        return res
    def follow(self, followerId: int, followeeId: int):
        if followerId not in self.follower:
            self.follower[followerId] = {followerId}
        self.follower[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int):
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)