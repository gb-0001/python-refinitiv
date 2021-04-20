import pandas

'''
df = pandas.read_csv('files/hrdata.csv') # retourne un DataFrame
print(type(df['Hire Date'][0]))
'''

'''
df = pandas.read_csv('files/hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
#print(df)
print(type(df['Hire Date'][0]))
'''

df = pandas.read_csv('files/hrdata.csv', 
  index_col='Employee', 
  parse_dates=['Hired'],
  header=0,
  names=['Employee', 'Hired', 'Salary', 'Sick Days'])

#print(type(df['Sick Days'][0])) # <class 'numpy.int64'>

s = 0 # somme
num_employee = 0
for salary in df['Salary']:
  num_employee += 1
  s += salary
print(round(s/num_employee, 2))