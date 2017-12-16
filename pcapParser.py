from scapy.all import  *
from packetToJson import *
from pymongo import MongoClient;

mongoClient = MongoClient();


db = mongoClient.Cyber

collection = db.Test;

a=rdpcap("Pritesh.pcap")


data=a[0].show()

x= packetToJson(data);

y={};
y['packet']=x;

collection.insert_one(y['packet'])





