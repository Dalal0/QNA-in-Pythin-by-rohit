import random

# list of states
d = {
    'andra pardesh':'hyderabad',
    'arunachal pardesh':'itanger',
    'assam':'dispur',
    'bihar':'patna',
    'chhattisgarh':'ragpur',
    'goa':'panji',
    'gujrat':'ghandinagar',
    'haryanan':'chandigarh',
    'Himachal pardesh':'shimla',
    'Jammu and kasmir':'jammu',
    'jkarkhand':'ranchi',
    'Kerala':'Thiruvananthapuram',
    'Madya Pradesh':'Bhopal',
    'Maharashtra':'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
     'Mizoram': 'Aizawi',
    'Nagaland': 'Rohima',
     'Orissa': 'Bhubaneshwar',
    "Punjab": 'Chandigarh',
    'Rajasthan':'Jaipur',
    'Sikkim':'Gangtok',
    'Tamil Nadu':'Chennai',
    'Telagana': 'Hyderabad',
    'Tripura':'Agartala',
    'Uttaranchal':'Dehradun',
    'Uttar Pradesh':'Lucknow',
    'West Bengal':'Kolkata',
    }
# created student class and other def etc....
class student:
    def __init__(self, state, random1, random2, random3, random4):

        self.state = state
        self.random3 = random1
        self.random1 = random2
        self.random4  = random3
        self.random2 = random4
    def quiz(self):
       return 'Que: What is the capital of %s? \n 1: %s \n 2: %s \n 3: %s \n 4: %s' % (self.state, self.random1, self.random2, self.random3, self.random4)

try:
    def gen():
        # generate option
        state = random.choice(list(d.keys()))
        option = set(random.choice(list(d.values())) for i in range(1,4))
        option.add(d[state])
        lists = list(option)

        # checking list items and etc....
        if len(lists) == 4 and (lists[0] != lists[1] != lists[2] != lists[3]) and (d[state] in lists):
            que = student(state, lists[0], lists[1], lists[2], lists[3])
            print(que.quiz())
        else:
            # if lists hasn't 4 item and they ain't matching to each other and key not in list, so it will refresh list
            gen()

    gen()
except Exception as e:
    print(e)


