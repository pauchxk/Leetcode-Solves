#write a function to convert a given date to YYY-MM-DD format.

date = '30th Jun 2004'
#year
year = date[-4:]
#month
monthset = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
ndate = date.split()
if ndate[1] in monthset:
    month = monthset.index(ndate[1])
    month += 1
    month = str(month)
    if len(month) == 1:
        month = '0' + month
#day
day = ndate[0]
nday = day[:-2]
if len(nday) == 1:
    nday = '0' + nday

formatted_date = f"{year}-{month}-{nday}"
print(formatted_date)