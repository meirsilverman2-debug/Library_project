from database.db_connection import get_connection

class BookDB:
    
    def create_book(self, data):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                """
                insert into books (title, author, genre) values(%s, %s, %s) ;
                """,
                (data["title"], data["author"], data["genre"])
            )

            connection.commit()
            return {"message": "book was successfuly created"}

        except Exception as e:
            print(f"(1) {e}")

        finally:    
            cursor.close()   



    def get_all_books(self):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                """
                select * from books ;
                """
            )

            data = cursor.fetchall()
            return data
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

    
    def get_book_by_id(self, id):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                """
                select * from books where id = %s ;
                """,
                (id,)
            )

            data = cursor.fetchall()
            return data
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()


    def update_book(self, id, data):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                update books
                set title = %s, author = %s, genre = %s
                where id = %s ;
                """,
                (data["title"], data["author"], data["genre"], id)
            )
            
            connection.commit()
            return {"message": "book was updated ;"}
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
    

    def set_available(self, id, val, member_id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
            update books set is_available = %s, borrowed_by_member_id = %s where id = %s ;
                """,
                (val, member_id, id)
            )

            connection.commit()
            return {"message": "update status complet ;"}
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()



    def count_total_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
            select count(*) as total_books from books ;

                """
            )

            result = cursor.fetchone()
            return result["total_books"]
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

    
    def count_available_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                select count(is_available) from books where is_available=1 ;
                """
            )

            result = cursor.fetchone()
            return result

        except Exception as e:
            print(e)
        

        finally:
            cursor.close()


    def count_borrowed_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                select count(is_available) from books where is_available=0 ;
                """
            )

            result = cursor.fetchone()
            return result


        except Exception as e:
            print(e)
        

        finally:
            cursor.close()


    def count_by_genre(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                select 
                count(*) as total_genre
                from books
                group by genre
                """
            )

            result = cursor.fetchall()
            return result


        except Exception as e:
            print(e)
        

        finally:
            cursor.close()

    def count_active_borrow_by_member(self, member_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                select count(borrowed_by_member_id) as total_book from books where borrowed_by_member_id = %s
                """,
                (member_id,)
            )

            result = cursor.fetchall()
            return result


        except Exception as e:
            print(e)
        

        finally:
            cursor.close()





    