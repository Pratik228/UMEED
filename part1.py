import csv

def writer(name,age,gender,wardnum,zone,travel,tested,incon,cough,fever,breath,hypr,diab,other):
	with open(r'data.csv', 'a', newline='') as csvfile:
		fieldnames = ['name','age','gender','war','zone','travel','tested','incon','cough','fever','breath','hypr','diab','other']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({'name':name,'age':age,'gender':gender,'war':wardnum,'zone':zone,'travel':travel,'tested':tested,'incon':incon,'cough':cough,'fever':fever,'breath':breath,'hypr':hypr,'diab':diab,'other':other})




red_list=["KAR12","KAR13","KAR01","KAR20","KAR25","KAR30"]


    


def datainput():
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    gender=input("Enter your gender:(male or female)\n")
    wardnum=input("Enter your wardnumber:(eg:KAR99)\n")
    zone=input("Are you in a red zone?\n")
    print("Please enter yes if you have the  following symptoms else enter no:")
    c=input("COUGH:\n")
    db=input("RESPIRATORY DISORDERS:\n")
    f=input("FEVER:\n")
    print("Please enter yes if u have the  following co-morbidities else enter no :")
    h=input("HYPERTENSION:\n")
    d=input("DIABETES:\n")
    o=input("OTHERS:\n")
    travel=input("Have you recently travelled abroad? yes or no\n")
    tested=input("Have you been tested by doctors? yes or no\n")
    incon=input("Have you been in contact with any infected person? yes or no\n")
    writer(name,age,gender,wardnum,zone,travel,tested,incon,c,f,db,h,d,o)
    
datainput()