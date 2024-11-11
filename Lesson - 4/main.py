import pandas as pd

data=pd.read_csv("titanic.csv")

notkids=data.loc[data["Age"]>18,"Name"]#condition ig
print(notkids)
print(data.iloc[9:25,2:5])#sclicing

#changing values
data.iloc[0:3,2]="anukrtit"
print(data.iloc[0:3])

#SAVINGGG
data.to_csv("changedstat.csv")

#creating new coloumns
data["Test"]=data["Fare"]+2
print(data.head())

data["sdsda"]=data["Pclass"]*data["Fare"]
print(data.head())

#RENAMEE
data_renameeed=data.rename(
    columns={
        "Pclass":"Passenger Class"
    }
)

print(data_renameeed.info())

#goruping
print(data[["Age","Fare"]].mean())

print(data.agg({
    "Age":["min","max","median"],
    "Fare":["min","max"]
}))

#i was
print(data[["Sex","Age"]].groupby("Sex").mean())

#ii way 

print(data.groupby("Sex")["Age"].mean())

print(data.groupby(["Sex","Pclass"])["Fare"].mean())

#count of rows in each category
print(data["Pclass"].value_counts())

#sorting the data
a = data.sort_values(by="Age")
print(a[["Name","Age"]])

agee= data.sort_values(by="Age",ascending=False)
print(agee[["Name","Age"]])

#MAKE EVERYTHING SMOLL

data["LOWER"]=data["Name"].str.lower()
print(data.head())

data["DOWN"]=data["Sex"].replace({"male":"M","female":"F"})
print(data.head())