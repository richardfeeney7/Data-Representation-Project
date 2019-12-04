import mysql.connector   #  pip3 install mysql-connector-python

class musicDAO:
  db=""
  def __init__(self):
    self.db = mysql.connector.connect( 
    host="localhost",
    user="root",
    password="root",
    database="music"
    )

# POP MUSIC SECTION
  def getAllPOP(self):
    cursor = self.db.cursor() 
    sql="select * from popMusic" 
    cursor.execute(sql)
    results = cursor.fetchall() 
    returnArray = []
    for result in results:
      returnArray.append(self.musicDict(result))
    return returnArray

  def findByIdPOP(self, id):
    cursor = self.db.cursor()
    sql="select * from popMusic where id = %s" 
    values = (id,)
    cursor.execute(sql, values) 
    result = cursor.fetchone() 
    return self.musicDict(result)


  def createPOP(self, values):
    cursor = self.db.cursor()
    sql="insert into popMusic (artist, album, price) values (%s,%s,%s)" 
    cursor.execute(sql, values)
    self.db.commit() 
    return cursor.lastrowid  


  def updatePOP(self, values):
    cursor = self.db.cursor()
    sql = "update popMusic set artist = %s, album = %s, price = %s where id = %s" 
    cursor.execute(sql, values)
    self.db.commit()
    print("update Successful")


  def deletePOP(self, id):
    cursor = self.db.cursor()
    sql="delete from popMusic where id = %s"
    values = (id,) 
    cursor.execute(sql, values)
    self.db.commit() 


  # convert pop result to a dictionary
  def musicDict(self,result):
    colnames = ["id", "artist","album","price"]
    item ={}
    # check if there is a result, otherwise return empty {}
    if result:
      for i, colName in enumerate(colnames):
        value = result[i]
        item[colName] = value
    return item

# Disco MUSIC SECTION
  def getAllDISCO(self):
      cursor = self.db.cursor() 
      sql="select * from discoMusic" 
      cursor.execute(sql)
      results = cursor.fetchall() 
      returnArray = []
      for result in results:
        returnArray.append(self.musicDict(result))
      return returnArray

  def findByIdDISCO(self, id):
    cursor = self.db.cursor()
    sql="select * from discoMusic where id = %s" 
    values = (id,)
    cursor.execute(sql, values) 
    result = cursor.fetchone() 
    return self.musicDict(result)


  def createDISCO(self, values):
    cursor = self.db.cursor()
    sql="insert into discoMusic (artist, album, price) values (%s,%s,%s)" 
    cursor.execute(sql, values)
    self.db.commit() 
    return cursor.lastrowid  


  def updateDISCO(self, values):
    cursor = self.db.cursor()
    sql="update discoMusic set artist= %s, album=%s, price=%s where id = %s" 
    cursor.execute(sql, values)
    self.db.commit()


  def deleteDISCO(self, id):
    cursor = self.db.cursor()
    sql="delete from discoMusic where id = %s"
    values = (id,) 
    cursor.execute(sql, values)
    self.db.commit() 


  # convert pop result to a dictionary
  def musicDict(self,result):
    colnames = ["id", "artist","album","price"]
    item ={}
    # check if there is a result, otherwise return empty {}
    if result:
      for i, colName in enumerate(colnames):
        value = result[i]
        item[colName] = value
    return item

# ROCK MUSIC SECTION
  def getAllROCK(self):
      cursor = self.db.cursor() 
      sql="select * from rockMusic" 
      cursor.execute(sql)
      results = cursor.fetchall() 
      returnArray = []
      for result in results:
        returnArray.append(self.musicDict(result))
      return returnArray

  def findByIdROCK(self, id):
    cursor = self.db.cursor()
    sql="select * from rockMusic where id = %s" 
    values = (id,)
    cursor.execute(sql, values) 
    result = cursor.fetchone() 
    return self.musicDict(result)


  def createROCK(self, values):
    cursor = self.db.cursor()
    sql="insert into rockMusic (artist, album, price) values (%s,%s,%s)" 
    cursor.execute(sql, values)
    self.db.commit() 
    return cursor.lastrowid  


  def updateROCK(self, values):
    cursor = self.db.cursor()
    sql="update rockMusic set artist= %s, album=%s, price=%s where id = %s" 
    cursor.execute(sql, values)
    self.db.commit()


  def deleteROCK(self, id):
    cursor = self.db.cursor()
    sql="delete from rockMusic where id = %s"
    values = (id,) 
    cursor.execute(sql, values)
    self.db.commit() 


  # convert pop result to a dictionary
  def musicDict(self,result):
    colnames = ["id", "artist","album","price"]
    item ={}
    # check if there is a result, otherwise return empty {}
    if result:
      for i, colName in enumerate(colnames):
        value = result[i]
        item[colName] = value
    return item

musicDAO = musicDAO()