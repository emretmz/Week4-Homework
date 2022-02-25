import requests
from random import shuffle
llist=[]
for i in range(10):
    my_list=[]
    r = requests.get('https://randomuser.me/api/')
    x=r.json()["results"]
    my_list.append(x[0]['name']['first'])
    my_list.append(x[0]['name']['last'])
    my_list.append(x[0]['location']['city'])
    my_list.append(x[0]['location']['country'])
    print("name:",my_list[0],"last:",my_list[1],"city:",my_list[2],"country:",my_list[3])

    txt = ''.join(my_list).replace(' ','').lower()
    print(txt)
    txtlist = list(txt)
    shuffle(txtlist)
    txt = ''.join(txtlist)
    print(txt)
    llist.append(txt)
print("the longest shuffle wors is:",max(llist,key=len))


