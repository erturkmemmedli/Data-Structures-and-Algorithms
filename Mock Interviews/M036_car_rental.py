# Mock interview with Adil Adilli (Salesforce)

'''
Given N cars and a list of rental requests (each with pickupTime, returnTime, and id), 
assign cars to maximize utilization while using the minimum number of cars possible. 

Each car can serve multiple requests as long as they don't overlap in time. 
For example, if Request A returns at time 5 and Request B picks up at time 5, the same car can serve both requests.


N = 3
requests = [
  {id: 1, pickup: 0, return: 5},
  {id: 2, pickup: 2, return: 7},
  {id: 3, pickup: 5, return: 9}
]


[
  {requestId: 1, carId: 0},
  {requestId: 2, carId: 1},
  {requestId: 3, carId: 0}
]

TC: O(nlogn)
SC: O(n)

'''

from heapq import heappush, heappop

def assign_car(n: int, requests: list[dict[str, int]]) -> list[dict[str, int]]:
  	requests.sort(key=lambda x: x['pickup'])
    heap = []
    car_id = 0
    output = []
    
    for request_id, pickup_time, return_time in requests:
      
        if heap and heap[0][0] <= pickup_time:
          	_, c_id = heappop(heap)
            output.append({'requestId': request_id, 'carId': c_id})
            heappush(heap, [return_time, c_id])
            
        elif len(heap) == n: 
          	output.append({'requestId': request_id, 'carId': -1})
            
        else:
            heappush(heap, [return_time, car_id])
            output.append({'requestId': request_id, 'carId': car_id})
            car_id += 1

    return output
