nowh, nowm, nows = map(int, input().split(":"))
starth, startm, starts =  map(int, input().split(":"))

time = starth * 3600 + startm * 60 + starts - (nowh * 3600 + nowm * 60 + nows)

if time < 0 :
    time += 60 * 60 * 24

rh = time // 3600
rm = (time % 3600) // 60
rs = time % 60

print("%02d:%02d:%02d" % (rh, rm, rs))

