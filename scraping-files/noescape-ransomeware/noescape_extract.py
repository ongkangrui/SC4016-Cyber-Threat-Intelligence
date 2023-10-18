import csv
from noescape_helper import *

dataType = {'Data Type - Databases': ['databases', 'SQL', 'SAP'],
            'Data Type - Applications': ['applications', 'program'],
            'Data Type - Emails': ['emails', 'passwords'], 
            'Data Type - Source Code': ['code'],
            'Data Type - Business Information': ['projects', 'documents', 'resumes', 'contracts', 'commercial', 'insurance', 'statements', 'certificates', 'internal', 'signed'],
            'Data Type - Designs': ['drawings', 'designs', 'media', 'projects'],
            'Data Type - Financial Information': ['financial', 'accounting', 'balances', 'invoices', 'financials', 'tax', 'budgets', 'fiscal', 'bank'],
            'Data Type - Research Information': ['research', 'studies'],
            'Data Type - Employee Information': ['employees', 'employee', 'personal', 'HR', 'payrolls', 'payroll', 'scans', 'vaccine', 'criminal', 'medication', 'numbers'],
            'Data Type - Customer Information': ['customer', 'customers', 'address', 'client', 'numbers'],
            'Data Type - Company Information': ['company', 'duration', 'operation'],
            'Data Type - Backup Systems Information': ['backups'],
            'Data Type - Supply Systems Information': ['suppliers'],
            'Data Type - Business Deals Information': ['partners', 'contracts', 'clients', 'negotiations'],
            'Data Type - Manufacturing Information': ['manufacturing'],}

file = open('csv-files/noescape.csv', 'w+', newline='', encoding='utf-8')
writer = csv.writer(file)
headers = (['Count','Company Targeted', 'Publish Date', 'Attacker', 'Industry', 'Latitude', 'Longitude', 'Location of Attack', 'Leak Size (In MB)'])
for key in dataType:
    headers.append(key)
writer.writerow(headers)


rawfile = open('csv-files/noescaperaw.csv', 'r')
reader = csv.DictReader(rawfile)
attacker = "NoEscape"
count = 1
for company in reader:
    companyTargeted = company['company_name']
    print(companyTargeted)
    publishDate = getDate(company['created_at'])
    industry = getIndustry(company['company_name'], company['text'])
    latitude, longitude = getCoord(company['company_address'])
    locationOfAttack = company['company_address']
    leakSize = getLeakSize(company['available_data'])
    dataLeaked = getDataType(company['text'], dataType)
    row = ([count,companyTargeted,publishDate,attacker,industry,latitude,longitude,locationOfAttack,leakSize] + dataLeaked)
    writer.writerow(row)
rawfile.close()
file.close()