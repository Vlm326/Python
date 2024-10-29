import psycopg2

def connect_database():
    try:
        connection = psycopg2.connect(
            dbname='file_storage',
            user='vlm326',
            password='123690',
            host='localhost',
            port='5432'
        )
        print("Подключение успешно")
    except Exception as e:
        print(e)

    
def add_file(filename, file_data):
    con = connect_database()
    cursor = con.cursor()
    cursor.exucute("INSERT INTO files (filename, file_data) VALUES (%s, %s)", (filename, psycopg2.Binary(file_data)))


def show_files():
    con = connect_database()
    cursor = con.cursor()
    cursor.execute("SELECT id, filename FROM files")
    files = cursor.fetchall()
    cursor.close()
    con.close()
    return files

