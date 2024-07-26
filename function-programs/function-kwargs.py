def printData(**data):
    print(data)
    print(type(data))
    print(len(data))
    print(data['name'])
    print(data['surname'])
    print(data['city'])
    print(data['bloodgroup'])

printData(name='Waseem',surname='Attar',city='Solapur',bloodgroup='O+')