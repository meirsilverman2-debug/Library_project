* # LIBRARY_PROJECT :🤫📖
---
* ##  system description :📝
(my nieces michali suggestion for the imogi)

* This library system will contain an API meaning we are building a server with the FastAPI that will be connected to our msql database and will manage the book data table and the data member table this intier system will opperate and work only with different HTTP requests that you will receive  on Swagger UI or on Postman manager.

---
---

* ## HOW TO RUN IT :▶️

* step 1.
~~~
git clone https://github.com/meirsilverman2-debug/Library_project.git
~~~
* step 2.
~~~
pip install -r requirements.txt
~~~
* step 3.
~~~
uvicorn main:app --reload
~~~
---
---
* ## File structure :📁
~~~
library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore
~~~
---
* ## How to create a doker container :
* Run the following code in your terminal.
~~~
docker run --name (name of your choice) -e MYSQL_ROOT_PASSWORD=(of your choice) -e MYSQL_DATABASE=(name of your choise) -p 3306:3306 -v (name of your choice):/var/lib/mysql -dmysql:latest
~~~
---
* ## Tables Strucrure :
* ### Books :
~~~
טבלת books — שדות
שדה הסבר
id מפתח ראשי
title כותרת הספר, עמודה לא ריקה, מקסימום 50 תווים
author שם המחבר, עמודה לא ריקה, מקסימום 50 תווים
genre ערכי genre מותרים:
מומש — Fiction | Non-Fiction | Science | History | Other
כעמודת ENUM במסד הנתונים, כל ערך אחר מחזיר שגיאה,
עמודה לא ריקה
available_is האם הספר זמין להשאלה — FALSE מסמן הושאל
עמודה לא ריקה
id_member_by_borrowed מזהה החבר שמחזיק את הספר — NULL אם זמין
~~~
* ### Members :
~~~
שדה הסבר
id מפתח ראשי
name שם החבר, עמודה לא ריקה, מקסימום 50 תווים
email כתובת מייל — ייחודית, עמודה לא ריקה
active_is האם החבר פעיל — FALSE לא יכול להשאיל
עמודה לא ריקה
borrows_total מונה סה"כ השאלות — עולה ב1- בכל השאלה
עמודה לא ריקה
~~~
---
* ## Low of the system :
~~~
חוקי מערכת
חוק נושא הכלל
1 יצירת ספר המשתמש שולח genre/author/title — המערכת מוסיפה
is_available=True, borrowed_by=NULL
ערך כל — Fiction / Non-Fiction / Science / History / Other להיות חייב genre 2
אחר מחזיר שגיאה
יש לוודא הן בהוספה )POST )והן בעדכון )PATCH)
3 יצירת חבר המשתמש שולח email/name — המערכת מוסיפה ,True=active_is
total_borrows=0
4 email חייב להיות ייחודי — אם קיים כבר מחזיר שגיאה
5 חבר לא פעיל אם False=active_is — אי אפשר להשאיל ספר
6 ספר לא זמין אי אפשר להשאיל ספר שכבר מושאל )False=available_is)
7 מקסימום
ספרים
חבר לא יכול להחזיק יותר מ3- ספרים בו-זמנית
8 החזרת ספר ניתן להחזיר ספר רק אם הוא מושאל לאותו חבר שמחזיר אותו
~~~
---
* ## List of endpoints :

* ### book endpoints :
~~~
מה היא עושה מי קורא לה מתודה
create_book(data) POST /books INSERT לטבלת books —
is_available=True,
borrowed_by=NULL
get_all_books() GET /books הספרים כל רשימת מחזירה
get_book_by_id(id) GET /books/{id} פי על אחד ספר מחזירה
או ID
None
update_book(id, data) PUT /books/{id} שנשלחו שדות מעדכן
set_available(id, val,
member_id)
PUT
/books/{id}/return/{
member_id}
PUT
/books/{id}/borrow/{
member_id}
מעדכן is_available
ו-borrowed_by_member_id
סופר את סך כל הספרים במסד summary/reports/ GET() books_total_count
הנתונים
count_available_books() GET /reports/summary עם ספרים סופר
is_available=True
מה היא עושה מי קורא לה מתודה
count_borrowed_books() GET /reports/summary עם ספרים סופר
is_available=False
count_by_genre(genre) GET
/reports/books-by-ge
nre
סופר ספרים לפי ז'אנר
count_active_borrows_by
_member(member_id)
PUT
/books/{id}/borrow/{
member_id}
סופר כמה ספרים החבר מחזיק
כרגע )לאכיפת חוק 7( — ספירת
books עם
borrowed_by_member_id
השווה ל-id_
~~~
* ### Members endpoints :
~~~
מה היא עושה מי קורא לה מתודה
count_borrowed_books() GET /reports/summary עם ספרים סופר
is_available=False
count_by_genre(genre) GET
/reports/books-by-ge
nre
סופר ספרים לפי ז'אנר
count_active_borrows_by
_member(member_id)
PUT
/books/{id}/borrow/{
member_id}
סופר כמה ספרים החבר מחזיק
כרגע )לאכיפת חוק 7( — ספירת
books עם
borrowed_by_member_id
השווה ל-id_
~~~
---
* ## Program flow :







