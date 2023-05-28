weather = {
    'city': 'Тула',
    'temperature': 16,
}

print(weather['city'])
weather['temperature'] -=  5
print(weather)
print(weather.get('country'))
print(weather.get('country', 'Россия'))
weather['date'] = '15.05.2023'
print(len(weather))
