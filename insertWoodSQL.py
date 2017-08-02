from csvreader import *

p = readCSV('temp_wood.csv')
t = open('insertwood.sql', 'w')
del p[0]
trystr = "BEGIN TRY \n"
insertstr = "INSERT INTO dbo.EHSSURVEY_WoodThickness ([WoodID],[Amount],[Thickness],[CF],[Units])\n VALUES"
sql = trystr + insertstr

for i in p:
    empty = 0
    wid = i[0]
    amt = i[1]
    thk = i[2]
    cf = i[3]
    units = i[4]
    
    if thk == '':
        empty = 1
        thk = "NULL"
    if amt == '':
        empty = 1
        amt == "NULL"
    if cf == '':
        empty = 1
        cf == "NULL"
    if units == '':
        empty = 1
        units == "NULL"

    if i == p[-1]:
        valstr = " (" + wid + "," + amt + "," + thk + "," + cf + ",'" + units + "')\n"
    valstr = " (" + wid + "," + amt + "," + thk + "," + cf + ",'" + units + "'),\n"
    if empty == 1:
        print(repr(i))
        print(valstr)
        print()
        

    sql +=  valstr

catchsql = """end try
begin catch
    --returns the complete original error message as a result set
    SELECT
        ERROR_NUMBER() AS ErrorNumber
        ,ERROR_SEVERITY() AS ErrorSeverity
        ,ERROR_STATE() AS ErrorState
        ,ERROR_PROCEDURE() AS ErrorProcedure
        ,ERROR_LINE() AS ErrorLine
        ,ERROR_MESSAGE() AS ErrorMessage

    --will return the complete original error message as an error message
    DECLARE @ErrorMessage nvarchar(400), @ErrorNumber int, @ErrorSeverity int, @ErrorState int, @ErrorLine int
    SELECT @ErrorMessage = N'Error %d, Line %d, Message: '+ERROR_MESSAGE(),@ErrorNumber = ERROR_NUMBER(),@ErrorSeverity = ERROR_SEVERITY(),@ErrorState = ERROR_STATE(),@ErrorLine = ERROR_LINE()
    RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState, @ErrorNumber,@ErrorLine)
end catch"""

sql += catchsql
t.write(sql)
t.close()
