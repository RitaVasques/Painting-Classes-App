from connection import ConnectDB
from student import Student

class ManageStudent:
    SELECTALL = 'SELECT * FROM students ORDER BY student_id'
    SELECT_ID = 'SELECT * FROM students WHERE student_id=%s'
    INSERT = 'INSERT INTO students(name, schedule, email, phone) VALUES(%s, %s, %s, %s)'
    UPDATE = 'UPDATE students SET name=%s, schedule=%s, email=%s, phone=%s WHERE student_id=%s'
    DELETE = 'DELETE FROM students WHERE student_id=%s'

    @classmethod
    def selectAll(cls):
        connection = None
        try:
            connection = ConnectDB.getConnection()
            cursor = connection.cursor()
            cursor.execute(cls.SELECTALL)
            clients_db =cursor.fetchall()
            # Mapeo de clase/tabla cliente
            clientes = []
            for client_db in clients_db:
                cliente = Student(client_db[0], client_db[1], client_db[2], client_db[3], client_db[4])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Error getting students data: {e}')
        finally:
            if connection is not None:
                cursor.close()
                ConnectDB.freeConnection(connection)

    @classmethod
    def select_by_id(cls, id_search):
        connection = None
        try:
            connection = ConnectDB.getConnection()
            cursor = connection.cursor()
            values = (id_search, )
            cursor.execute(cls.SELECT_ID, values)
            output =cursor.fetchone()
            student= Student(output[0], output[1], output[2], output[3], output[4])
            return student
        except Exception as e:
            print(f'Error selection student by id: {e}')
        finally:
            if connection is not None:
                cursor.close()
                ConnectDB.freeConnection(connection)

    @classmethod
    def insert(cls, student):
        connection = None
        try:
            connection = ConnectDB.getConnection()
            cursor = connection.cursor()
            values = (student.name, student.schedule, student.email, student.phone)
            cursor.execute(cls.INSERT, values)
            connection.commit()    
        except Exception as e:
            print(f'Error inserting a student: {e}')
        finally:
            if connection is not None:
                cursor.close()
                ConnectDB.freeConnection(connection)

    @classmethod
    def update(cls, student):
        connection = None
        try:
            connection = ConnectDB.getConnection()
            cursor = connection.cursor()
            values = (student.name, student.schedule, student.email, student.phone, student.student_id)
            cursor.execute(cls.UPDATE, values)
            connection.commit()
        except Exception as e:
            print(f'Error updating a student: {e}')
        finally:
            if connection is not None:
                cursor.close()
                ConnectDB.freeConnection(connection)

    @classmethod
    def delete(cls, student):
        connection = None
        try:
            connection = ConnectDB.getConnection()
            cursor = connection.cursor()
            values = (student.student_id,) # Need the , at the end to be a tuple
            cursor.execute(cls.DELETE, values)
            connection.commit()
        except Exception as e:
            print(f'Error deleting a student: {e}')
        finally:
            if connection is not None:
                cursor.close()
                ConnectDB.freeConnection(connection)
