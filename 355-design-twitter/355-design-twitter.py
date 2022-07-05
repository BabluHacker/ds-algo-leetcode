class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list) # userId => [[time, tweetId]]
        self.followmap = defaultdict(set) # followerId => [followeeId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetmap[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []   
        hashMap = []
        self.followmap[userId].add(userId)
        for followee in self.followmap[userId]:
            if followee in self.tweetmap:
                index = len(self.tweetmap[followee]) - 1
                time, tweetId = self.tweetmap[followee][index]
                hashMap.append([time, tweetId, followee, index-1])
        heapq.heapify(hashMap)
        while hashMap and len(res) < 10:
            time, tweetId, userId, index = heapq.heappop(hashMap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetmap[userId][index]
                heapq.heappush(hashMap, [time, tweetId, userId, index-1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap:
            self.followmap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)