import tabula
from os import listdir
from os.path import isfile, join

def get_Table_Value(TABLE,SEARCH):
  found = False
  global total
  for i,value in enumerate(TABLE):
    if type(value) != str:
      continue

    if value == SEARCH:
      found = True
      continue
    
    if found == True:
      (v1,v2) = value, TABLE[i+1]
      if v1.isnumeric():
        total += int(v1)
      if v2.isnumeric():
        total += int(v2)
      
      SEARCH = SEARCH.replace("\r","")
      print(f"{SEARCH} - 招生名額 : {v1}")
      print(f"{SEARCH} - 預計甄試人數 : {v2}")
      break

# Get Files
onlyfiles = [f for f in listdir(".\data") if isfile(join(".\data", f))]

for file in onlyfiles:

  # Read PDF
  result = tabula.read_pdf(f".\data\{file}",pages=1)

  keys = result[0].keys() # len = 17
  allItems = result[0].values.tolist() # len = 17

  Accept = keys[2]
  Alter = keys[2 + 1]
  
  Accept_ROW = {}
  compiType = ""
  for index,i in enumerate(allItems):
    for j,value in enumerate(i):
      if type(value) != str or len(Accept_ROW) == 4:
        continue
      if "招生群(類)別" in value:
        compiType = i[j+1]
      
      if "一般考生" in value or "低收或中低收入戶" in value or "原住⺠考生" in value or "離島考生" in value:
        Accept_ROW[value] = i
        # Accept_ROW = i
        continue

      """ if "預計甄試人數" in value:
        Alter_ROW = allItems[index+1]
        continue """

  print("=====================================")
  print(f"檔案名稱 : {file}")

  # print(keys[1]) # 學校名稱
  print(next(x for x in keys if "學校名稱" in x))
  print(f"類群 : {compiType}")

  total = 0
  for key, value in Accept_ROW.items():
    get_Table_Value(value,key)
  print(f"總招生名額 : {total}")
  
  # get_Table_Value(Alter_ROW,"預計甄試人數")
print("=====================================")