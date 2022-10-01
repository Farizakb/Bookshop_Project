
import pymysql
import pymysql.cursors
import sys
# Connect to the database
connection = pymysql.connect(host='localhost',
                             port = 3306,
                             user='root',
                             password='Salam',
                             database='Books',
                             cursorclass=pymysql.cursors.DictCursor)

def create_table():
    with connection.cursor() as cursor:

        sql ="""
            create table if not exists Book_info(
                id int(11) unsigned Auto_increment primary key,
                title varchar(25) not null,
                author varchar(25) not null,
                exist boolean not null,
                price int(11) not null


            );

        """

        cursor.execute(sql)
    connection.commit()




def create_book(T,A,E,P):
    with connection.cursor() as cursor:

        sql ="""
            insert into Book_info(title,author,exist,price)
            values(%s,%s,%s,%s)


        """
        values = (T,A,E,P)
        cursor.execute(sql,values)
    connection.commit()





def show_all():
    with connection.cursor() as cursor:

        sql="""
            select * from Book_info



        """
        cursor.execute(sql)
        result = cursor.fetchall()
    for i in result:
        print(i)
    


def show_book(I):
    with connection.cursor() as cursor:

        sql="""
            select * from Book_info where id=%s



        """
        cursor.execute(sql,I)
        result = cursor.fetchall()
        print(result)






def change_status(id):
    with connection.cursor() as cursor:

        sql="""
            select exist from Book_info where id=%s



        """
        cursor.execute(sql,id)
        result = cursor.fetchall()
        print(result[0]["exist"])
        value = result[0]["exist"]
        if value == 0:
            with connection.cursor() as cursor:

                chg="""
                    update Book_info set exist = 1 where id=%s


                """
                cursor.execute(chg,id)
            connection.commit()
            
        else:
            with connection.cursor() as cursor:

                chg="""
                    update Book_info set exist = 0 where id=%s


                """
                cursor.execute(chg,id)
            connection.commit()
        print(result)




def change_price(id,prc):
    with connection.cursor() as cursor:
        sql="""
        update Book_info set price = %s where id = %s

        """
        values = (prc,id)
    
        cursor.execute(sql,values)
    connection.commit()





def remove_book(id):
    with connection.cursor() as cursor:
        sql="""
        delete from Book_info where id = %s

        """
        cursor.execute(sql,id)
    connection.commit()




def search_book(word):
    with connection.cursor() as cursor:
        sql ="""
        select * from Book_info where title like %s or author like %s
        """
        values = (f"%{word}%",f"%{word}%")
        cursor.execute(sql,values)
        print(cursor.fetchall())







command = sys.argv    

print(command)
if "add" and  "table" in command:
    create_table()


elif "book" and "add" in command:
    create_book(
        input("Kitabin adini qeyd edin: "),
        input("Yazarin adini qeyd edin: "),
        input("Kitabin movcud olub olmadigin qeyd edin (0 ve 1 ile): "),
        input("Kitabin qiymetini qeyd edin: ")
    )


elif "show" and "all" in command:
    show_all()

elif "show" and "book" in command:
    show_book(input("Kitabi id-sini daxil edin: "))

elif "change" and "status" in command:
    change_status(input("Kitabin id sini daxil edin: "))

elif "change" and "price" in command:
    change_price(
        input("Kitabin id sini daxil edin: "),
        input("Kitabin yeni qiymetini daxil edin: "))

elif "remove" in command:
    remove_book(input("Kitabin id sini daxil edin: "))
elif "search" in command:
    search_book(input("Yazar adi yaxu Kitabin adini qeyd edin: "))
else:
    print('Wrong input!')


