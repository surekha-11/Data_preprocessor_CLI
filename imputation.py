import pandas as pd
from data_description import DataDescription


class Imputation:
    
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    # The Task associated with this class.
    tasks = [
        "\n1. Show number of Null Values",
        "2. Remove Columns",
        "3. Fill Null Values (with mean)",
        "4. Fill Null Values (with median)",
        "5. Fill Null Values (with mode)",
        "6. Show the Dataset"
    ]

    def __init__(self, data):
        self.data = data

    def showColumns(self):
        print("\nColumns\U0001F447\n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        return
    

    def printNullValues(self):
        print("\nNULL values of each column:")
        for column in self.data.columns.values:
            
            print('{0: <20}'.format(column) + '{0: <5}'.format(sum(pd.isnull(self.data[column]))))
        print("")
        return

    def removeColumn(self):
        self.showColumns()
        while(1):
            columns = input("\nEnter all the column"+ self.bold_start + "(s)" + self.bold_end + "you want to delete (Press -1 to go back)  ").lower()

            if columns == "-1":
                break

            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                try:
                 
                    self.data.drop(columns.split(" "), axis = 1, inplace = True)
                except KeyError:
                    print("One or more Columns are not present. Try again.....\U0001F974")
                    continue
                print("Done.......\U0001F601")
                break
            else:
                print("Not Deleting........\U0001F974")
        return

  
    def fillNullWithMean(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mean())
                except KeyError:
                    print("Column is not present. Try again.....\U0001F974")
                    continue
                except TypeError:
                    
                    print("The Imputation is not possible here\U0001F974. Try on another column.")
                    continue
                print("Done......\U0001F601")
                break
            else:
                print("Not changing........\U0001F974")
        return


    def fillNullWithMedian(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].median())
                except KeyError:
                    print("Column is not present. Try again.....\U0001F974")
                    continue
                except TypeError:
                    print("The Imputation is not possible here\U0001F974.Try on another column.")
                    continue
                print("Done......\U0001F601")
                break
            else:
                print("Not changing........\U0001F974")
        return

   
    def fillNullWithMode(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    
                    self.data[column] = self.data[column].fillna(self.data[column].mode()[0])
                except KeyError:
                    print("Column is not present. Try again.....\U0001F974")
                    continue
                except TypeError:
                    print("The Imputation is not possible here\U0001F974. Try on another column.")
                    continue
                print("Done......\U0001F601")
                break
            else:
                print("Not changing........\U0001F974")
        return

    def imputer(self):
        while(1):
            print("\nImputation Tasks\U0001F447")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break

            if choice == -1:
                break

            elif choice==1:
                self.printNullValues()

            elif choice==2:
                self.removeColumn()

            elif choice==3:
                self.fillNullWithMean()

            elif choice==4:
                self.fillNullWithMedian()
            
            elif choice==5:
                self.fillNullWithMode()

            elif choice==6:
                DataDescription.showDataset(self)

            else:
                print("\nWrong Integer value!! Try again..\U0001F974")
        return self.data