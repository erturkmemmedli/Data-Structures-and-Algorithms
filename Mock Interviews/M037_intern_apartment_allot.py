# Mock interview with Adil Adilli (Salesforce)

'''
You are given a list of interns and a list of available apartments. Each apartment has a specific number of bedrooms. 
Every assigned intern must get their own bedroom (i.e., an apartment with \(N\) bedrooms can host at most \(N\) interns).
Each intern has a preference: they either want to live with housemates in a multi-bedroom apartment, 
or they want to live alone in a single-bedroom apartment.
'''

interns: -> want: T, not_wants: F
apartments: -> num_of_bed
  
{
  matched_with_preference: {apt:intern},
  matched_with_not_preference: list[int],
  unallocated: list[int]
}

1 - seperate multi and single rooms
2 - assign multi rooms as much as possible
3 - assign single rooms as much as possible
4 - remaining ones assignment

tc: O(max(A, I))
sc: O(max(A, I))
  

class Apartment:
    def __init__(self, apt_number: int, num_rooms: int):
        self.apt_number = apt_number
        self.num_rooms = num_rooms

class Person:
    def __init__(self, name: str, wants_housemates: bool):
        self.name = name
        self.wants_housemates = wants_housemates


def assign_persons_to_apts(persons: list[Person], apartments: list[Apartmern]) -> dict:
  	single_rooms = []
    mulitple_rooms = []
    
    for apartment in apartments:
      	if apartment.apt_number == 1:
          	single_rooms.append(apartment)
        else:
          	mulitple_rooms.append(apartment)
            
    multiple_rooms.sort(key=lambda x: -x.num_rooms)
            
    single_wanter = []
    multiple_wanter = []
    
    for person in persons:
      	if person.wants_housemates:
          	multiple_wanter.append(person)
        else:
          	single_wanter.append(person)
    
    count_of_assigned_multiple_wanters = len(multiple_wanter)
    current_multi_apt_count = 0
    
    output = {
        'matched_with_preference': defaultdict(list),
        'matched_with_not_preference': [],
        'unallocated': []
    }
    
    multi_apt_index = 0
    multi_room_index = 0
    
    # multi to multi
    while multi_apt_index < len(multiple_rooms) and multi_room_index < len(multi_wanter):
      	while multiple_rooms[multi_apt_index].num_rooms > 0 and multi_room_index < len(multi_wanter):
          	multiple_rooms[multi_apt_index].num_rooms -= 1
            output['matched_with_preference'].append({
              'apt_id': multiple_rooms[multi_apt_index].apt_number, 
              'per_name': multiple_wanter[multi_room_index].name
            })
            multi_room_index += 1
        multi_apt_index += 1
        
    remaining_multi_wanter_left = len(multi_wanter) - multi_room_index
      	
    
    # single to single
    # single to multi
    # multi to sinlge
