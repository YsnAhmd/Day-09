employees=[{'Id':1,'Name':'Nazmul','Salary':123},
{'Id':2,'Name':'Saiful','Salary':45},
{'Id':3,'Name':'Atiq','Salary':789},
{'Id':4,'Name':'Monjur','Salary':632}]

print('%5s %25s %10s' % ('Id','Name','Salary:'))

print(40*'=')
for x in employees:
    print('%5s %25s %10s' % (x['Id'],x['Name'],x['Salary']))
#print using formate command
print('\n\n%-5s %-25s %-10s' % ('Id','Name','Salary:'))

print(40*'=')
for x in employees:
    print('{0:<5} {1:<25} {2:<10}'.format(x['Id'],x['Name'],x['Salary']))


