'''apply methods in pandas , it is a useful method used to carry out a specific task for a column'''
import numpy as np
import pandas as pd

file=pd.read_csv(r"C:\Users\soham\Downloads\tips.csv")
file=file.set_index('Payment ID')
print(file)
#for example if we want to print the last 4 digits of CC number , we dont have a function to print last 4 digits of an int 
#so we define a function 
def cc(num):
    return str(num)[-4:]

# print(cc(123454321)) returns last 4 digits
#now if we want to apply this function to the column CC number we use apply() method 
file['last4']=file['CC Number'].apply(cc)#added new column of last 4 digits 
print(file)

'''applying on multiple columns and using lambda functions'''
#we could have done the upper task using a lambda function by 
file['last5']=file['CC Number'].apply(lambda num: str(num)[-5:])
print(file)
#working with multiple columns
#for example we take total bill column and tip column
def qual(Total_bill,tip):
    if tip/Total_bill > 0.25:
        return 'good'
    else :
        return 'bad'
    
    
file['Tipqual']=file[['total_bill','tip']].apply(lambda file: qual(file['total_bill'],file['tip']),axis=1)
print(file)

#vectorize 
#by passing the .vectorize() the function is aware that it has to work with numpy array 
#The vectorize function is provided primarily for convenience, not for performance. The implementation is essentially a for loop.

file['Tipqual']=np.vectorize(qual)(file['total_bill'],file['tip'])
print(file)

'''sorting and other methods on your dataframe'''
file.sort_values('tip') # sorts the tip column in ascending order
file.sort_values(['tip','size'])#we can sort multiple columns 
#value_counts,Nice method to quickly get a count per category. Only makes sense on categorical columns.
file['sex'].value_counts()
#Quickly replace values with another one.
print(file['Tipqual'].replace(to_replace='bad',value='ok'))
#the unique function is used to see the unique values 
file['size'].unique()
#replacing multiple values by mapping 
my_map = {'Dinner':'D','Lunch':'L'}
file['time'].map(my_map)
#we use drop_duplicates to remove duplicate items
#eq we have a data frame 
simple_df = pd.DataFrame([1,1,1,1,2,2,2,2],['a','b','c','d','e','f','g','h'])
simple_df.drop_duplicates()
#we can use between function to know if how many rows have values between a , b 
file['total_bill'].between(10,20,inclusive=True)
#we can use the nlargest and nsmallest 
file.nlargest(10,'tip')#it returns the top 10 rows which have the highest values in column tip
file.nsmallest(10,'tip')#it returns the top 10 rows which have the lowest values in column tip
#we can use the sample function to return any random n rows 
file.sample(5)#returns 5 random rows 
