import common.oracle_db as odb


def deleteKey(link_key):
    conn = odb.connect()
    cursor = None

    query = "DELETE FROM L_LINK " + \
            "WHERE LINK_KEY = '" + link_key + "' "


    result = 0
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = 1
    except Exception as msg:
        print('deleteKey() 에러 발생 : ', msg)
        result = 0
    finally:
        cursor.close()
        odb.close(conn)
        return result


def deleteDate():
    conn = odb.connect()
    cursor = None

    query = "DELETE FROM L_LINK " + \
            "WHERE LINK_DATE NOT BETWEEN (SYSDATE - 5/24/60) AND SYSDATE "

    result = 0
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = 1
    except Exception as msg:
        print('deleteDate() 에러 발생 : ', msg)
        result = 0
    finally:
        cursor.close()
        odb.close(conn)
        return result


def selectLink(link_key):
    conn = odb.connect()
    cursor = None

    query = "SELECT * " + \
            "FROM L_LINK " + \
            "WHERE LINK_KEY = '" + link_key + "' AND " + \
            "LINK_DATE BETWEEN (SYSDATE - 5/24/60) AND SYSDATE "

    result = 0
    try:
        cursor = conn.cursor()
        print(1)
        result = cursor.execute(query).fetchone()
        print(2)
        print("user_no : " + str(result[0]))
    except Exception as msg:
        print('selectLink() 에러 발생 : ', msg)
    finally:
        cursor.close()
        odb.close(conn)
        return str(result[0])


def selectUser(user_no):
    conn = odb.connect()
    cursor = None
    user = {}

    query = "SELECT * " + \
            "FROM L_USER " + \
            "WHERE USER_NO = " + user_no

    try:
        cursor = conn.cursor()
        print(1)
        result = cursor.execute(query).fetchone()
        print(2)
        user = {'user_no': result[0], 'user_email': result[1], 'user_name': result[2],
                    'user_badge': result[3], 'login_ok': result[4], 'user_admin': result[5],
                    'user_date': result[6].strftime('%Y-%m-%d %H:%M:%S')}
        print(user)
    except Exception as msg:
        print('selectLink() 에러 발생 : ', msg)
    finally:
        cursor.close()
        odb.close(conn)
        return user


def userLoad(request):
    try:
        user = selectUser(request.session['user_no'])
        return user
    except KeyError:
        return 0
