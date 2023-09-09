import pandas as pd

#Load csv file into a data frame
dataframe = pd.read_csv("Employees.csv")
print(dataframe)
print("_____________________________________")

#Remove the duplicates
df1 = dataframe.drop_duplicates()
print(df1)
print("_____________________________________")

#Remove the decimal places in age column
df1['Age'] = df1['Age'].astype(int)
print(df1)
print("_____________________________________")

#Convert USD salary to EGP
From_USD_T0_EGP = 30
df1['Salary(USD)'] = df1['Salary(USD)'].multiply(From_USD_T0_EGP)
df1 = df1.rename(columns={'Salary(USD)': 'Salary(EGP)'})
print(df1)
print("_____________________________________")

#Print the average of ages
Average_age = df1['Age'].mean()
print("The average age is: " + str(Average_age))
print("_____________________________________")

#Print the median salary
median_salary = df1['Salary(EGP)'].median()
print("The median salary is: " + str(median_salary))

#Print the ratio between males and females
No_of_Males = df1['Gender'].value_counts()['M']
No_of_Females = df1['Gender'].value_counts()['F']
Ratio = No_of_Males / No_of_Females
print("Ratio= " + str(Ratio))
print("Then the ratio between males and females is:   " + str(Ratio) + "   :   1")


#Export new csv file
df1.to_csv("EmployeesNewFile.csv")