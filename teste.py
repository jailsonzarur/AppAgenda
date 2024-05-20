from datetime import datetime

data = "19/05/2024"

data_teste = datetime.strptime(data, '%d/%m/%Y')
print(type(data_teste.date()))