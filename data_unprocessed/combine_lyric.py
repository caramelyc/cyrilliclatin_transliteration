combine =[]

with open("data_cyrillic.txt") as xh:
  with open('data_latin.txt') as yh:
    with open("data_combined.txt","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists
      #combine = list(zip(ylines,xlines))
      #Write to third file
      for i in range(len(xlines)):
        xlines[i]=xlines[i].strip()
        if not xlines[i]:
          continue
        line = xlines[i] + '|' + ylines[i]
        zh.write(line)