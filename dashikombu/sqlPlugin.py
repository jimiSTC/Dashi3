import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:stc-tess-db1' 
database = 'impresario' 

username = os.getenv("pyusername")
password = os.getenv("pyuser_db_pass")

def Dashi2():
    #print("test.....................dashi")
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("EXEC [dbo].[LRP_STC_INTRANET_SALES_TODAY]")
    dashi2Results = list(cursor.fetchall())
    print(dashi2Results)
    #dashi2Resultsform = [dashi2Results]
    #dashi2Results[0][4][5] = round((dashi2Results[0][4][5]),2 )
    #dashi2Resultsform = dashi2Resultsform [0][ '%.2f' % elem for elem in dashi2Results ]
    #print(round((dashi2Resultsform[0][3][5]),2))
    cursor.close()
    cnxn.close()
    return dashi2Results


def Donation():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("EXEC [dbo].[LRP_STC_DONATIONS_TODAY]")
    dashiDonation = list(cursor.fetchall())
    print(dashiDonation)
    cursor.close()
    cnxn.close()
    return dashiDonation

