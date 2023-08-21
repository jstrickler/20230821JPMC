import pickle

with open('potus.pic','rb') as POTUS:
    presidents = pickle.load(POTUS)

for p in presidents:
    print("{} {} {}".format(p.firstname, p.lastname, p.party))
