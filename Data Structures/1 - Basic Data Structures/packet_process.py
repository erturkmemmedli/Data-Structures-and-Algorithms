from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        max_size = self.size
        
        while self.size >= 0 and self.size <= max_size:
            was_dropped = False
            
            if len(self.finish_time) > 0:
                if self.finish_time[0] <= request[0]:
                    self.finish_time.popleft()
                    self.size += 1
                    
            if self.size == 0:
                break
                
            if len(self.finish_time) > 0:
                started_at = self.finish_time[-1]
                self.finish_time.append(self.finish_time[-1] + request[1])
                self.size -= 1
                return Response(was_dropped, started_at)
            
            if len(self.finish_time) == 0:
                started_at = request[0]
                self.finish_time.append(request[1])
                self.size -= 1
                return Response(was_dropped, started_at)
            
        return Response(True, -1)

def main():
    buffer_size, n_requests = map(int, input().split())
    
    requests = []
    responses = []
    
    for i in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
        
    buffer = Buffer(buffer_size)

    for request in requests:
        responses.append(buffer.process(request))
    
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

if __name__ == "__main__":
    main()
