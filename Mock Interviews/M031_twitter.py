# Mock interview with Adil Adilli (Salesforce)

'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.

void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.

List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.

void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.

void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

'''

# follower_map
# tweet_map
# followee_map

# {
#   1: {2, 3, 4, 5}
# }

# {
#   1: [(a,1), (b,1)]  #(c,2), (d,2), ()]
#   2: [(c,2), (d,2)]
#   5: [(e,5), (f,5)]
# }

# log(m)

postTweet -> O(nlog(m))
getNewsFeed -> O(mlog(m))
follow -> O(nlog(m)
unfollow -> O(1)

from heapq import heappush, heappop

class Twitter:
  
  def __init__(self):
    self.follower_map = {}
    self.followee_map = {}
    self.tweet_map = {}
    self.timestamp = 0
    
    
  def post_tweet(user_id: int, tweet_id: int) -> None:
    heappush(self.tweet_map[user_id], (-self.timestamp, tweet_id, user_id)) # wrong, didn't check if existing in dict
    
    for followee_id in self.followee_map:
      heappush(self.tweet_map[followee_id], (-self.timestamp, tweet_id, user_id))
      
    self.timestamp += 1
    
    
	def getNewsFeed(user_id: int) -> list[int]:
    result_set = []
    
    while self.tweet_map[user_id]:
      time, tweet_id, u_id = heappop(self.tweet_map[user_id])
      
      if user_id != u_id and u_id not in self.follower_id[user_id]:
        continue
      
      if result_set[-1][1] == tweet_id:
        continue
      
      result.append([time, tweet_id, u_id])
      
      if len(result) == 10:
        break
        
    for data in result_set:
      heappush(self.tweet_map[user_id], data)
    
    return [tweet_id for _, tweet_id, _ in result_set]

  
	def follow(follower_id: int, followee_id: int) -> None:
    if follower_id not self.follower_map:
      self.follower_map[follower_id] = set()
    self.follower_map[follower_id].add(followee_id)
  	
    if followee_id not in self.followee_map:
      self.followee_map[followee_id] = set()
    self.followee_map[followee_id].add(follower_id)
    
    # duplicate check burda olmaliydi
    for tweet in self.tweet_map[followee_id]:
    	heappush(self.tweet_map[follower_id], tweet)
    

	def unfollow(follower_id: int, followee_id: int) -> None:
    self.follower_map[follower_id].discard(followee_id)
    self.followee_map[followee_id].discard(follower_id)
    # unfollowing burada heap-den remove etseydi daha yaxsi olardi
