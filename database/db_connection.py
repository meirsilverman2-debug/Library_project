import mysql.connector

def get_connection():
    return mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    port=3306,
    password="1234",
    database="library_db")


def create_tables():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)
    try:

        cursor.execute(
            """
            create table books(
            id int auto_increment primary key,
            title varchar(50) not null,
            author varchar(50) not null,
            genre enum('fiction', 'non-fiction', 'science', 'history', 'other') not null,
            is_available boolean not null default True,
            borrowed_by_member_id int null 
            )
            
            """
                    )

        cursor.execute(
            """
           create table members(
            id int primary key auto_increment,
            name varchar(50) not null,
            email varchar(100) unique not null,
            is_active boolean not null default false,
            total_borrows int not null default 0 )
            """
        )
    except Exception as e:
        print(f"ERROR: {e}")