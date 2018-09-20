import redis
import pandas as pd

r = redis.Redis(
    host='localhost',
    port=6379)

r.set('test-key', 'test-value')
value = r.get('test-key')
value = r.get('test-key')
print(value)

df = pd.read_excel('PriceTrend.xlsx')
print(df.info().)

date = df.loc[1,"Date"].date()
price = int(df.loc[1,"SU 1"])
print("su1= {:d}".format(price))

diHashFormat = "DI:VI#{viId}:{year}:{month}:{day}"
viId = "540101022"
year = date.year
month = date.month
day =  date.day
diKey = diHashFormat.format(viId=viId, year=year, month=month, day=day)
print(diKey)

ddHashFormat = "SU:{rateId}#DD:{wf}:{wb}#RANK:{rank}"
rateId = 101
wf = wb = 7
rank = 1
suKey = ddHashFormat.format(rateId=rateId, wf=wf, wb=wb, rank=rank)

print(suKey)

r.hmset(diKey, {suKey: price})

print(r.hget(diKey, suKey).decode())