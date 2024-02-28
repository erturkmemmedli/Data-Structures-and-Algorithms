# Mock interview with Asif Mammadov (Splunk)

Question: Design a rate limiter. 


6 requests per hour 
 
--> R1 at 11:53 Y  
--> R2 at 11:54 Y       
--> R3 at 11:55 Y
--> R4 at 11:56 Y
--> R5 at 11:57 Y
--> R6 at 11:58 Y
--> R7 at 11:59	N
--> R8 at 12:03 Y
--> R9 at 12:04 Y
--> R10 at 12:05 Y
--> R11 at 12:06 Y
--> R12 at 12:07 Y
--> R13 at 12:08 Y

--> R14 at 13:50 


Request(context, type)


class RateLimiter:
	def __init__(self, limit=1 hour, capacity=60 req):
    		self.limit = limit
	        self.capacity = capacity
	        self.window = deque()

	def should_procees_request(request) -> bool:
		time = time.now()
		if not self.window:
			self.window.append(time)
		else:
			while self.window and time - self.window[0] > self.limit: 59>=60 false
				self.window.popleft()
			if self.capacity > len(self.window): 6 > 3 false
				self.window.append(time)
				return True
			else:
				return False



    13:00 - 11:56 > 60 min

    [12:55, 13:00]

# Ask for requirements first, then design API, then implement the code
# RateLimiter can be different type - time-based, ip-based, user-based, account-based, request-based
# For time-based solution, datetime.now() can be used for service receiving request time
# Timedelta can be used to check whether we are inside the given limit.
