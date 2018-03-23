from pymongo import MongoClient;
import xlsxwriter


mongoClient = MongoClient();


db = mongoClient.Cyber


collection = db.TCP;

collection = db.cowrie

dataset = db.cowrie.find({"eventid":"cowrie.session.connect"})






# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('cowrieSessionConnect.xlsx')
worksheet = workbook.add_worksheet()

row =0
col=0




for i in range(0,dataset.count()):
    dictobject=dict(dataset[i])
    object = list(dictobject.keys())
    for c in range(0,len(object)):
        worksheet.write(row, c, str(dictobject[object[c]]));
    row = row+1

workbook.close()