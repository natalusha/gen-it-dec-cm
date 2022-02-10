import mydecorator
import mygenerator
import mysqlcontextmanager
import myiterator


def main():
    myiterator.FancyIterator.print_task_name(mydecorator.__name__)
    a = print(mydecorator.to_dict(["Apple", "Cherry", "Orange"]))
    myiterator.FancyIterator.print_task_name(myiterator.__name__)
    for el in myiterator.FancyIterator(6):
        print(el)
    myiterator.FancyIterator.print_task_name(mygenerator.__name__)
    for el in mygenerator.square_generator(10):
        print(el)
    # another way to show generator results step by step
    # numbers = mygenerator.square_generator(10)
    # print(next(numbers))
    # print(next(numbers))
    # print(next(numbers))
    myiterator.FancyIterator.print_task_name(mysqlcontextmanager.__name__)
    with mysqlcontextmanager.my_sql_context_manager(
        "localhost", "root", " ", "world"
    ) as mydb:
        sql = "SELECT * FROM world.city  LIMIT 10"
        mydb.cursor.execute(sql)
        myresult = mydb.cursor.fetchall()
        for x in myresult:
            print(x)


if __name__ == "__main__":
    main()
