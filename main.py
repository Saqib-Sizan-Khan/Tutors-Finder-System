import pandas as pd
from educator.models import HomeEducator,OutsideEducator,HomeEducatorSubjects,OutsideEducatorSubjects
from home.models import Subjects

#home educator data read
df = pd.read_csv("Home_Educator_Info.csv")
for i in range(len(df)):
    he = HomeEducator(homeTutorName=df["Home Educator Name"][i],homeTutorEmail=df["Email"][i],university=df["University"][i],department=df["Department"][i],experience=df["Experience"][i],homeTutorLocation=df["Location"][i],homeTutorContact=df["Contact"][i],homeTutorPassword=df["Password"][i],homeTutorRating=df["Rating"][i])
    he.save()

#outside educator data read
df = pd.read_csv("Outside_Educator_Info.csv")
for i in range(len(df)):
    oe = OutsideEducator(outsideTutorName=df["Outside Educator Name"][i],outsideTutorEmail=df["Email"][i],institute=df["Institute"][i],designation=df["Designation"][i],outsideTutorLocation=df["Location"][i],outsideTutorContact=df["Contact"][i],outsideTutorPassword=df["Password"][i],outsideTutorRating=df["Rating"][i])
    oe.save()

#Home educator subject
df = pd.read_csv("HomeEducatorSubject.csv")
for i in range(len(df)):
    hes = HomeEducatorSubjects(firstSubject=df["Subject 1"][i],secondSubject=df["Subject 2"][i],thirdSubject=df["Subject 3"][i])
    hes.save()

#Outside educator subject
df = pd.read_csv("OutsideEducatorSubject.csv")
for i in range(len(df)):
    oes = OutsideEducatorSubjects(firstSubject=df["Subject 1"][i],secondSubject=df["Subject 2"][i],thirdSubject=df["Subject 3"][i])
    oes.save()

# educators = HomeEducator.objects.filter(location='Mirpur')
# for educator in educators:
#     print(educator.name,educator.id)
