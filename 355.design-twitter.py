#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#

# @lc code=start
class Twitter(object):

    def __init__(self):
        self.tweet_stack = []
        self.follow_dict = {}

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweet_stack.append([userId, tweetId])

        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        disp_user = [userId]
        # print(self.follow_dict)
        if userId in self.follow_dict:
            for user in self.follow_dict[userId]:
                disp_user.append(user)
        tweet_list = []
        for i in range(len(self.tweet_stack)-1, -1, -1):
            if self.tweet_stack[i][0] in disp_user:
                tweet_list.append(self.tweet_stack[i][1])
            if len(tweet_list) >= 10:
                break
        return tweet_list
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        print("follow")
        print(self.follow_dict)
        if followerId not in self.follow_dict or len(self.follow_dict[followerId]) == 0:
            self.follow_dict[followerId] = [followeeId]
        else:
            old_list = self.follow_dict[followerId]
            if followeeId not in old_list:
                old_list.append(followeeId)
            self.follow_dict[followerId] = old_list
        print(self.follow_dict)


    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.follow_dict:
            self.follow_dict[followerId] = []
        else:
            new_list = self.follow_dict[followerId].remove(followeeId)
            if not new_list:
                self.follow_dict[followerId] = []
            else:
                self.follow_dict[followerId] = new_list


        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

