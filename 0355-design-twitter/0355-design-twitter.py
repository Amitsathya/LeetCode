class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([-self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []
        self.followMap[userId].add(userId)        
        for followerId in self.followMap[userId]:
            if followerId in self.tweetMap:
                index = len(self.tweetMap[followerId]) - 1
                count, tweet = self.tweetMap[followerId][index]
                heap.append([count, tweet, followerId, index - 1])
        heapq.heapify(heap)
        while heap and len(res) < 10:
            count, tweet, followerId, index = heapq.heappop(heap)
            res.append(tweet)
            if index >= 0:
                count, tweet = self.tweetMap[followerId][index]
                heapq.heappush(heap, [count, tweet, followerId, index - 1])
        return res        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)