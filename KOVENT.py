namber = int(input("Enter the seconds: "))
years = namber //31536000
namber %=31536000
months = namber //2592000
namber %=2592000
days = namber //86400
namber %=86400
hours = namber //3600
namber %=3600
minutes = namber //60
seconds = namber %60
print(years, '/', months, '/', days)
print(hours, ':', minutes, ':', seconds)
