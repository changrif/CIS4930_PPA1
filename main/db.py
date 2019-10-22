from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.pymongo_db

def getTime():
    today = datetime.datetime.now()
    return today.strftime("%Y-%m-%d %H:%M:%S%p")

def getBMI():
    bmis = db.bmis
    bmiList = [];
    if bmis.count() > 0:
        for obj in bmis.find():
            obj.pop('_id', None)
            bmiList.append(obj)
    return bmiList

def printAllBMI():
    bmis = db.bmis
    
    if bmis.count() > 0:
        for obj in bmis.find():
            print("\n " + obj['timestamp'] + "\t Input: [feet: " + str(obj['feet']) + ", inches: " + str(obj['inches']) + ", weight: " + str(obj['weight']) + "]\n \t\t\t Output: [bmi: " + str(obj['bmi']) + ", category: " + obj['category'] + "]")

def saveBMI(feet, inches, weight, category, bmiNum):
    bmis = db.bmis

    bmi_data = {
        'feet': int(feet),
        'inches': int(inches),
        'weight': int(weight),
        'bmi': bmiNum,
        'category': category,
        'timestamp': getTime()
    }
    bmis.insert_one(bmi_data)
    bmi_data.pop('_id', None)
    return bmi_data

def getEmails():
    emails = db.emails
    emailList = [];
    if emails.count() > 0:
        for obj in emails.find():
            obj.pop('_id', None)
            emailList.append(obj)
    return emailList

def printAllEmails():
    emails = db.emails
    
    if emails.count() > 0:
        for obj in emails.find():
            print("\n " + obj['timestamp'] + "\t Input: [email: " + str(obj['email']) + "]\n \t\t\t Output: [validated: " + str(obj['validated']) + "]")
            
def saveEmail(verified, address):
    emails = db.emails
    
    email_data = {
        'email': address,
        'validated': verified,
        'timestamp': getTime()
    }
    emails.insert_one(email_data)
    email_data.pop('_id', None)
    return email_data