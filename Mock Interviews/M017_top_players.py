# Mock Interview with Tural Farhadov (MongoDB)

'''
Alice-50
# alice-50
Bob-65
Alice-40
Bob-70
# Alice-90b
.....

# upper-lower case in names?
# valid data?
# didn’t ask for return type

n of entries.

Top 50 players out of those entries.
Sorted by their highest score
'''

def find_top_players(players_data):
  player_map = {}
	
	for  player in player_data:
		name, score = player.split('-')
    
    if name not in player_map:
			player_map[name] = -float('inf')
		player_map[name] = max(player_map[name], score)
	
	top_players = sorted( [(val, key) for key, val in player_map.items()], reverse=True)
	
	return [name + '-' + str(cal)  for val, name in top_players[:50]]

Class TopPlayers:
	def init(self):
		self.player_map = {}
		self.top_players_heap = []
	
	def player_input(player):
    if name not in player_map:
			player_map[name] = -float('inf')
		self.player_map[name] = max(self.player_map[name], score)
		
		if len(self.top_players_heap) < 50:
			# lock
			heappush(self.top_players_heap, (score, name)
		  # unlock
		else:
			if score > self.top_players_heap[0][0]:
        # lock
				heappop(self.top_players_heap)
				heappush(self.top_players_heap, (score, name))
				# unlock

		return sorted( [name + '-' + str(score) for score, name in self.top_players_heap], reverse=True)

# edit: hashmap size can also be adjusted at 50 along with heap operations
'''
[
	Alice - 40
	Bob - 50
	C - 60
]

C - 70

1st - O(nlogn)
2nd - O(n*logK)
3rd - O(50*n)

O(50*n) = P*50n   O(nlogn) = K*nlogn

2 ^ 50

P*50n < K*nlogn

Hashmap O(1) - amortized 
'''
