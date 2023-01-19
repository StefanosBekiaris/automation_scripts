import pymssql

class SqlDb:
    def __init__(self, serverString, db, user, password) -> None:
        print(f"Connecting to DB {db}...")
        self.__con = pymssql.connect(serverString, user, password, db)
        self.__cursor = self.__con.cursor(as_dict=True)
        self.__counter = 1
        
    def exec_non_read_query(self, query) -> None:
        cursor = self.__cursor
        cursor.execute(query)
        self.__con.commit()
        print(f'Query {self.__counter} executed!')
        self.__counter += 1 
            
    def exec_get_query(self, query) -> dict:
        cursor = self.__cursor
        cursor.execute(query)        
        print(f'Query {self.__counter} executed!')
        self.__counter += 1 
        
        print("Fetching results...")
        results = cursor.fetchall()
        return results
    
    def __exit__(self, type, value, traceback):
        print("Connection to DB closed...")
        self.__con.close()
    
    def __del__(self):
        print("Connection to DB closed...")
        self.__con.close()
    
    
