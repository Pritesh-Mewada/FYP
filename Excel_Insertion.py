from pymongo import MongoClient;
import xlsxwriter


mongoClient = MongoClient();


db = mongoClient.Cyber

collection = db.TCP;

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Dataset.xlsx')
worksheet = workbook.add_worksheet()

row =0
col=0
dataset = collection.find({})

for i in range(0,100000):
    worksheet.write(row, 0,dataset[i]['Ethernet']['src'])
    worksheet.write(row, 1, dataset[i]['TCP']['flags'])
    worksheet.write(row, 2, dataset[i]['TCP']['dport'])
    worksheet.write(row, 3, dataset[i]['TCP']['sport'])
    worksheet.write(row, 4, dataset[i]['IP']['src'])
    worksheet.write(row, 5, dataset[i]['IP']['proto'])
    worksheet.write(row, 6, dataset[i]['IP']['tos'])
    worksheet.write(row, 7, dataset[i]['IP']['dst'])
    worksheet.write(row, 8, dataset[i]['IP']['len'])
    worksheet.write(row, 9, dataset[i]['IP']['version'])
    worksheet.write(row, 10, dataset[i]['IP']['flags'])
    worksheet.write(row, 11, dataset[i]['IP']['ttl'])
    row = row+1

workbook.close()