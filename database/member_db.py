from database.db_connection import get_connection

class MemberDB:

    def create_member(self, data):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                """
                insert into members (name, email)
                values(%s, %s) 
                """,
                (data["name"], data["email"])
            )

            connection.commit()
            return {"message": "A new member was added to database"}
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()


    def get_all_memmbers(self):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                """
            select * from members
                """
            )

            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
    
    def get_member_by_id(self, id):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                """
            select * from members where id = %s
                """,
                (id,)
            )
            result = cursor.fetchone()
            return result

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

    
    def update_member(self, id: int, data: dict):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                """
            update members set name = %s, email = %s where id = %s
                """,
                (data["name"], data["email"], id)
            )

            connection.commit()
            return {"message": f"the member with the {id} was updated"}

        except Exception as e:
            print(e)
        
        finally:
            cursor.close()


    def deactivate_member(self, id: int):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:

            cursor.execute(
                """
            update members set is_active = %s where id = %s
                """,
                (False, id)

            )

            connection.commit()
            return {"message": f"the member with the id {id} was successfuly deactivate"}
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

    
    def activate_member(self, id: int):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:

            cursor.execute(
                """
                update members set is_active = %s where id = %s
                """,
                (True, id)
            )

            connection.commit()
            return {"message": f"the member with the id {id} has been activate"}
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()
    

    def increment_borrows(self, id: int):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:

            cursor.execute(
                """
            update members set total_borrows = total_borrows + %s where id = %s
                """,
                (1,id)

            )

            connection.commit()
            return {"message": f"total_borrows was in id {id} was updated successfuly"}
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()


    def count_active_members():

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:

            cursor.execute(
                """
                select count(is_active) from members where is_active = %s
                """,
                (True,)
            )

            result = cursor.fetchone()
            return result
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()

        
    def get_top_member():

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                """
                select max(total_borrows) as top_member from members
                """
            )

            result = cursor.fetchone()
            return result
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()

        
            

