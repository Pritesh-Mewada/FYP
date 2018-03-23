from scapy.all import  *
from packetToJson import *
from pymongo import MongoClient;

mongoClient = MongoClient();


db = mongoClient.Cyber

collection = db.Test;


for j in range(151,170):
    a = rdpcap("Pcap/nobit"+str(j))

    for i in range(0,len(a),1):
        print("Packet inserted"+str(i))
        data = a[0].show()
        x = packetToJson(data)
        y = {}
        y['packet'] = x
        collection.insert_one(y['packet'])
