import sqlite3
import os

database_path = os.path.abspath("db.sqlite3")
conn = sqlite3.connect(database_path)

c = conn.cursor()

def first_query(X, Y):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""
            SELECT cc.id, cc.name
            FROM customer_customer cc
            JOIN customer_order co ON cc.id = co.customer_id
            JOIN customer_ordermodel com ON co.id = com.order_id
            JOIN customer_menuitem cm ON com.menu_item_id = cm.id
            WHERE cm.category_id IN
                (SELECT cct.id
                FROM customer_category cct
                WHERE cct.name = @Y)
            GROUP BY cc.id
            HAVING COUNT(DISTINCT cm.id) >= @X 
            """, (X, Y))

    return c.fetchall()


def second_query(X):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""
            SELECT co.id
            FROM customer_order co
            JOIN customer_shippingaddress csa ON co.id = csa.order_id
            WHERE csa.city = @X AND co.is_shipped = 1
    """, (X,))

    return c.fetchall()


def third_query(X):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""
            SELECT cc.id, cc.name
            FROM customer_customer cc
            JOIN customer_order co ON cc.id = co.customer_id
            GROUP BY cc.id
            HAVING COUNT(co.id) >= @X
    """, (X,))

    return c.fetchall()


def fourth_query(X):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""
            SELECT cm.id, cm.name, COUNT(*) as count
            FROM customer_menuitem cm
            JOIN customer_ordermodel com ON cm.id = com.menu_item_id
            JOIN customer_order co ON com.order_id = co.id
            JOIN customer_customer cc ON co.customer_id = cc.id
            WHERE cc.email = ?
            GROUP BY cm.id
    """, (X,))

    return c.fetchall()

print(fourth_query('alina333alina888@gmail.com'))


def fifth_query(X):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""
            SELECT cm.id, cm.name
            FROM customer_menuitem cm
            WHERE cm.category_id IN
                (SELECT cct.id
                FROM customer_category cct
                WHERE cct.name = @X)
    """, (X,))

    return c.fetchall()


def sixth_query(X):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""
        SELECT cm.id, cm.name
        FROM customer_menuitem cm
        JOIN customer_ordermodel com ON cm.id = com.menu_item_id
        JOIN customer_order co ON com.order_id = co.id
        WHERE cm.name = @X OR (
            cm.name <> @X AND
            co.customer_id IN (
                SELECT co2.customer_id
                FROM customer_ordermodel com2
                JOIN customer_order co2 ON com2.order_id = co2.id
                JOIN customer_menuitem cm2 ON com2.menu_item_id = cm2.id
                WHERE cm2.name = @X
            )
        )
        GROUP BY cm.id, cm.name
        HAVING COUNT(DISTINCT co.customer_id) = (
            SELECT COUNT(DISTINCT co3.customer_id)
            FROM customer_ordermodel com3
            JOIN customer_order co3 ON com3.order_id = co3.id
            JOIN customer_menuitem cm3 ON com3.menu_item_id = cm3.id
            WHERE cm3.name = @X
        )
        ORDER BY cm.id;
    """, (X,))

    return c.fetchall()

print(sixth_query('Salmon sashimi'))


def seventh_query(X):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""
            SELECT cm1.id, cm1.name
            FROM customer_menuitem AS cm1
            WHERE EXISTS (
                SELECT com1.order_id
                FROM customer_ordermodel AS com1
                WHERE com1.menu_item_id = cm1.id
                AND com1.order_id IN (
                    SELECT com2.order_id
                    FROM customer_ordermodel AS com2
                        JOIN customer_menuitem AS cm3 ON cm3.id = com2.menu_item_id
                    WHERE cm3.name = @X
                )
            )
            AND NOT EXISTS(
                SELECT com3.order_id
                FROM customer_ordermodel AS com3
                    JOIN customer_menuitem AS cm4 ON cm4.id = com3.menu_item_id
                WHERE cm4.name = @X
                AND com3.order_id NOT IN (
                    SELECT com4.order_id
                    FROM customer_ordermodel AS com4
                        JOIN customer_menuitem AS cm5 ON cm5.id = com4.menu_item_id
                    WHERE cm5.name = @X
                )
            );
    """, (X,))

    return c.fetchall()

print(seventh_query('Yamamoto'))

def eighth_query(X):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT c2.id, c2.name
        FROM customer_customer AS c1
        JOIN customer_order AS o1 ON c1.id = o1.customer_id
        JOIN customer_ordermodel AS om1 ON o1.id = om1.order_id
        JOIN customer_menuitem AS m1 ON om1.menu_item_id = m1.id
        JOIN customer_ordermodel AS om2 ON om1.menu_item_id = om2.menu_item_id
        JOIN customer_order AS o2 ON om2.order_id = o2.id
        JOIN customer_customer AS c2 ON o2.customer_id = c2.id
        WHERE (c1.email = @X OR c2.email = @X) AND c2.id <> c1.id
        AND (
            SELECT COUNT(DISTINCT om3.menu_item_id)
            FROM customer_customer AS c3
            JOIN customer_order AS o3 ON c3.id = o3.customer_id
            JOIN customer_ordermodel AS om3 ON o3.id = om3.order_id
            WHERE c3.email = c2.email
        ) = (
            SELECT COUNT(DISTINCT om4.menu_item_id)
            FROM customer_customer AS c4
            JOIN customer_order AS o4 ON c4.id = o4.customer_id
            JOIN customer_ordermodel AS om4 ON o4.id = om4.order_id
            WHERE c4.email = @X
        )
        ORDER BY c2.id;
    """, (X,))

    return c.fetchall()

print(eighth_query('alina333alina888@gmail.com'))

conn.close()