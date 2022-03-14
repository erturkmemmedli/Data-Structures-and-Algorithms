from collections import deque

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        max_size = self.size
        temp = 0
        
        while self.size >= 0 and self.size <= max_size:
            was_dropped = False
            
            if len(self.finish_time) > 0:
                if self.finish_time[0] <= request.arrived_at:
                    if len(self.finish_time) == 1:
                        temp = self.finish_time[-1]
                    self.finish_time.popleft()
                    self.size += 1
                    
            if self.size == 0:
                break
                
            if len(self.finish_time) > 0:
                started_at = self.finish_time[-1]
                self.finish_time.append(self.finish_time[-1] + request.time_to_process)
                self.size -= 1
                return Response(was_dropped, started_at)
            
            if len(self.finish_time) == 0:
                started_at = request.arrived_at
                self.finish_time.append(temp + request.time_to_process)
                self.size -= 1
                return Response(was_dropped, started_at)
            
        return Response(True, -1)

class Request:
    def __init__(self, arrived_at, time_to_process):
        self.arrived_at = arrived_at
        self.time_to_process = time_to_process

class Response:
    def __init__(self, was_dropped, started_at):
        self.was_dropped = was_dropped
        self.started_at = started_at

def requests(n_requests):
    requests = []
    for i in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    return requests

def responses(buffer, requests):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

def result(responses):
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

if __name__ == '__main__':
    buffer_size, n_requests = map(int, input().split())
    requests = requests(n_requests)
    buffer = Buffer(buffer_size)
    responses = responses(buffer, requests)
    result(responses)
