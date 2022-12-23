# -------------------------------
# -------------79-80-------------
# -------------------------------

# -------------------------------
# ---------Assignment-1----------
# -------------------------------


import datetime

date = datetime.datetime(2021, 6, 25)
dateNow = datetime.datetime(2021, 8, 10)

print(f"Days From 2021-06-25 To 2021-08-10 Is => {(dateNow - date).days}")


# -------------------------------
# ---------Assignment-2----------
# -------------------------------


import datetime

#https://strftime.org/

print((datetime.datetime.now()).strftime("%Y-%m-%d"))
print((datetime.datetime.now()).strftime("%b %d, %Y"))
print((datetime.datetime.now()).strftime("%d - %b - %Y"))
print((datetime.datetime.now()).strftime("%d / %b / %Y"))
print((datetime.datetime.now()).strftime("%d / %B / %Y"))
print((datetime.datetime.now()).strftime("%a, %d %B %Y"))




