from connection import ConnectDB
from income import Income

class ManageIncome:
    INSERT = 'INSERT INTO accounting(student_id, date, amount) VALUES(%s, %s, %s)'
    SELECTALL = 'SELECT * FROM accounting ORDER BY student_id'
    GRAPH = 'SELECT date, SUM(amount) AS total_amount FROM accounting GROUP BY date ORDER BY date'

    @classmethod
    def insert(cls, income):
        connection = None
        try:
            connection = ConnectDB.getConnection()
            cursor = connection.cursor()
            values = (income.student_id, income.date, income.amount)
            cursor.execute(cls.INSERT, values)
            connection.commit()    
        except Exception as e:
            print(f'Error inserting income: {e}')
        finally:
            if connection is not None:
                cursor.close()
                ConnectDB.freeConnection(connection)

    @classmethod
    def selectAll(cls):
        connection = None
        try:
            connection = ConnectDB.getConnection()
            cursor = connection.cursor()
            cursor.execute(cls.SELECTALL)
            income_db =cursor.fetchall()
            # Mapeo de clase/tabla income
            income_registers = []
            for income in income_db:
                income = Income(income[0], income[1], income[2], income[3])
                income_registers.append(income)
            return income_registers
        except Exception as e:
            print(f'Error getting income data: {e}')
        finally:
            if connection is not None:
                cursor.close()
                ConnectDB.freeConnection(connection)


    @classmethod
    def search_by_id(cls, id_search):
        income_registers = cls.selectAll()
        income_by_id = []
        for income in income_registers:
            if income.student_id == id_search:
                income_by_id.append(income)
        return income_by_id

    @classmethod
    def get_chart_data(cls):
        connection = None
        try:
            connection = ConnectDB.getConnection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(cls.GRAPH)
            chart_data =cursor.fetchall()
            return chart_data # returns a list of dictionaries [{'date':..., 'total_amount':...}, ...]
        except Exception as e:
            print(f'Error getting chart data: {e}')
            return []
        finally:
            if connection is not None:
                cursor.close()
                ConnectDB.freeConnection(connection)
