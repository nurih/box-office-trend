import psycopg2 as pg
from datetime import datetime


def single_day_top_sales(day):
    conn = None
    try:
        print("Connecting...")
        conn = pg.connect(
            user="pguser",
            password="DTgXLPi1Urz7x6W4p3HCnd",
            host="127.0.0.1",
        )
        print("Connected.")

        query, param = create_query(day)
        print("Running query...")
        cur = conn.cursor()
        cur.execute(query, (param,))
        print(cur.query)
        result = cur.fetchone()
        print("Executed.")
        return result
    except (Exception, pg.DatabaseError) as error:
        print(error)
        raise error
    finally:
        if conn is not None:
            conn.close()


def create_query(day: str):
    try:
        date_parameter = datetime.strptime(day, "%Y-%m-%d").strftime("%Y-%m-%d")
        print("date is ok")

        return (
            f"""SELECT theater, sum(amount) total
                FROM sale
                WHERE day = %s
                GROUP BY theater
                ORDER BY total DESC
                LIMIT 1;""",
            date_parameter,
        )
    except Exception as e:
        print(e)
        raise e


if __name__ == "__main__":
    print(single_day_top_sales("2025-01-01"))
