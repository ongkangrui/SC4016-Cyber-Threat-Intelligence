from geopy.geocoders import Nominatim
import time

def getDataType(text, dataType):
    dataFiles = [0] * 15
    data = text.split()
    for key in dataType:
        for i in dataType[key]:
            for j in data:
                if i.lower() == j.lower():
                    dataFiles[list(dataType).index(key)] = 1
    return dataFiles

def getDate(date):
    months = {'Jan': '01',
         'Feb': '02',
         'Mar': '03',
         'Apr': '04',
         'May': '05',
         'Jun': '06',
         'Jul': '07',
         'Aug': '08',
         'Sep': '09',
         'Oct': '10',
         'Nov': '11',
         'Dec': '12'}
    formatDate = date.split(' ')
    date = formatDate[2] + '-' + months[formatDate[1]] + '-' + formatDate[0]
    return date

def getIndustry(companyName, text):
    industries = {'GovernmentAgency': ['national','instituto','government', 'defense', 'homeland security','federal','state', 'social', 'county', 'confederation','ministry'], 
              'Agriculture': ['agriculture', 'crop', 'farms'], 
              'Supermarket': ['supermarket', 'grocery'], 
              'Technology': ['technology-based','technology','wireless', 'communication', 'digital'],
              'Security': ['security', 'secure','intelligence', 'surveillance', 'reconnaissance'],
              'Motor/Vehicular': ['vehicles','driving','car','drive', 'motorcycles', 'snowmobiles'],
              'Medical': ['medical', 'health', 'hospital', 'clinic', 'pharmaceutical', 'pathology'],
              'RealEstate': ['estate'],
              'School': ['school', 'college'],
              'Airline': ['airline','flights'],
              'ConsultingServices': ['consulting'],
              'Cosmetics': ['cosmetics', 'suplements', 'beauty', 'skin care'],
              'NonProfitOrganisation': ['community', 'in need', 'communities', 'voluntary'],
              'Water': ['water'],
              'Legal': ['legal', 'law'],
              'HeavyMachineryManufacturer': ['forklifts'],
              'Accountancy': ['accountants'],
              'Pipes': ['tubular'],
              'Fuel/Oil': ['fuel', 'petrol','propance', 'petroleum'],
              'Construction/Renovation': ['barrier', 'roofing', 'waterproofing', 'construction', 'building'],
              'Aerospace': ['turbine engine'],
              'Unions': ['union'],
              'DrinkManufacturer': ['drink'],
              'ConventionCentre': ['meeting', 'exhibition'],
              'Accessories': ['accessories'],
              'Glass': ['glass'],
              'Food': ['food'],
              'Welding': ['metal', 'material'],
              'Finance': ['commerce'],
              'Retailer': ['consumer'],
              'Diamond': ['diamond'],
              'Cinema/Movie': ['PVR Ltd.'], 
              'Multimedia': ['multimedia', 'television', 'productions', 'films', 'advertising'],
              'Drilling': ['drilling', 'rigs']}
    
    description = companyName.split() + text.split()
    industry = "none"
    for keywords in industries:
        for keyword in industries[keywords]:
            for word in description:
                if keywords == word.lower():
                    industry = keywords
                    return industry
    return industry

def getLeakSize(leakSize):
    leakSize = leakSize.split()
    if leakSize[1].lower() == 'gb':
        return float(leakSize[0]) * 1000
    return float(leakSize[0])

def getCoord(address):
    address = address.split(',')
    geolocator = Nominatim(user_agent="qwertyytrewq")
    try:
        time.sleep(1)
        location = geolocator.geocode(address[0])
        if location is None:
            return [0, 0]
        else:
            latitude = location.latitude
            longitude = location.longitude
            return [latitude, longitude]
    except:
        return [0, 0]