from datetime import datetime
from datetime import datetime

import cx_Oracle
import common.oracle_db as odb
import Model.gallery.gallery_class as gclass

def select_all(user, ob):
    conn = odb.connect()
    cursor = None
    gallery_list = []
    if ob == 0:
        query = 'SELECT * ' \
                'FROM L_GALLERY ' \
                'JOIN L_USER USING (USER_NO) ' \
                'ORDER BY GALLERY_DATE DESC'
    else:
        query = 'select gallery_no, count(*) c \
                from l_like \
                group by gallery_no \
                ORDER by c desc'

    try:
        cursor = conn.cursor()
        result = cursor.execute(query)

        # 각 행을 하나씩 추출해서, Gallery 클래스 객체 생성함
        # 행의 컬럼값들을 꺼내서 Gallery 인스턴스의 초기값으로 설정
        for row in result:
            print(type(row[6].strftime('%Y-%m-%d, %H:%M:%S')))
            row_dict = {'g_no': row[1], 'u_no': row[0], 'content': row[2],
                        'photopath': row[3], 'hashtag': row[4], 'rcount': row[5],
                        'date': row[6].strftime('%Y-%m-%d %H:%M:%S'), 'u_name': row[8]}
            print('row_dict : ', row_dict)

            # ref = gclass.Gallery(row_dict)  # Gallery 객체 생성
            # print('gclass.Gallery.info(ref) : ', gclass.Gallery.info(ref))
            # gallery_list.append(ref)

            gallery_list.append(row_dict)

    except Exception as msg:
        print('Gallery select_all() 에러 발생 : ', msg)

    query = 'SELECT * ' \
            'FROM L_LIKE ' \
            'WHERE USER_NO = ' + str(user)

    try:
        cursor = conn.cursor()
        like_result = cursor.execute(query).fetchall()

    except Exception as msg:
        print('Gallery select_all() like 에러 발생 : ', msg)

    finally:
        cursor.close()
        odb.close(conn)
    print('like_result : ', like_result)
    if user > 0:
        for g in gallery_list:
            for l in like_result:
                if l[1] == g['g_no']:
                    g['like'] = 1
                    break
                else:
                    g['like'] = 0
    else:
        for g in gallery_list:
            g['like'] = 0

    print('gallery_list : ', gallery_list)
    return gallery_list

def select_one(g_no, u_no):
    detail_list = []
    comment_list = []
    conn = odb.connect()
    cursor = None
    query = 'SELECT * ' \
            'FROM L_COMMENT ' \
            'JOIN L_USER USING (USER_NO) ' \
            'WHERE GALLERY_NO = ' + g_no

    try:
        cursor = conn.cursor()
        result = cursor.execute(query)

        for row in result:
            row_dict = {'cu_name': row[6], 'content': row[3], 'c_date': row[4].strftime('%Y-%m-%d %H:%M:%S')}
            # print('comment row_dict : ', row_dict)

            comment_list.append(row_dict)

    except Exception as msg:
        print('Detail select_one() comment 에러 발생 : ', msg)

    query = 'SELECT * ' \
            'FROM L_GALLERY ' \
            'JOIN L_USER USING (USER_NO) ' \
            'WHERE GALLERY_NO = ' + g_no

    try:
        cursor = conn.cursor()
        # detail_result = cursor.execute(query).fetchall()
        result = cursor.execute(query)

        for row in result:
            row_dict = {'u_no': row[0], 'g_no': row[1], 'content': row[2],
                        'photopath': row[3], 'hashtag': row[4], 'rcount': row[5],
                        'g_date': row[6].strftime('%Y-%m-%d %H:%M:%S'), 'gu_name': row[8]}
            # print('detail row_dict : ', row_dict)

        #     detail_list.append(row_dict)
        detail = row_dict

    except Exception as msg:
        print('Detail select_one() detail 에러 발생 : ', msg)

    query = 'SELECT COUNT(*) ' \
            'FROM L_LIKE ' \
            'WHERE GALLERY_NO = ' + g_no

    try:
        cursor = conn.cursor()
        like_count = cursor.execute(query).fetchone()

    except Exception as msg:
        print('Detail select_one() like_count 에러 발생 : ', msg)

    query = 'SELECT COUNT(*) ' \
            'FROM L_LIKE ' \
            'WHERE GALLERY_NO = ' + g_no + ' AND USER_NO = ' + str(u_no)

    try:
        cursor = conn.cursor()
        like = cursor.execute(query).fetchone()

    except Exception as msg:
        print('Detail select_one() like_count 에러 발생 : ', msg)

    query = 'SELECT COUNT(*) ' \
            'FROM L_COMMENT ' \
            'JOIN L_USER USING (USER_NO) ' \
            'WHERE GALLERY_NO = ' + g_no

    try:
        cursor = conn.cursor()
        c_count_result = cursor.execute(query).fetchone()

        # for row in result:
        #     row_dict = {'c_count': row[0]}
        #     # print('c_count row_dict : ', row_dict)
        #
        #     comment_list.append(row_dict)

    except Exception as msg:
        print('Detail select_one() c_count 에러 발생 : ', msg)
    finally:
        cursor.close()
        odb.close(conn)

    # print('detail_list : ', detail_list)
    # print('comment_list : ', comment_list)
    return detail, comment_list, like_count, like, c_count_result
    # return detail_result, comment_result, c_count_result

def gallike(g_no, u_no, onoff):
    conn = odb.connect()
    cursor = None

    if onoff == '1':
        query = 'DELETE FROM L_LIKE ' \
                'WHERE GALLERY_NO = ' + g_no + ' AND USER_NO = ' + u_no
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        except Exception as msg:
            print('Gallery like() off 에러 발생 : ', msg)
        finally:
            cursor.close()
            odb.close(conn)

    else:
        query = 'INSERT INTO L_LIKE ' \
                'VALUES(' + u_no + ', ' + g_no + ')'
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        except Exception as msg:
            print('Gallery like() on 에러 발생 : ', msg)
        finally:
            cursor.close()
            odb.close(conn)

    return '좋아요 변경됨'

def search(s):
    conn = odb.connect()
    cursor = None
    search_list = []

    query = 'SELECT * ' \
            'FROM L_GALLERY ' \
            'JOIN L_USER USING (USER_NO)' \
            "WHERE HASHTAG LIKE '%" + s + "%' " \
            "ORDER BY GALLERY_DATE DESC"
    try:
        cursor = conn.cursor()
        result = cursor.execute(query)

        for row in result:
            print(type(row[6].strftime('%Y-%m-%d, %H:%M:%S')))
            row_dict = {'g_no': row[1], 'u_no': row[0], 'content': row[2],
                        'photopath': row[3], 'hashtag': row[4], 'rcount': row[5],
                        'date': row[6].strftime('%Y-%m-%d %H:%M:%S'), 'u_name': row[8]}
            print('row_dict : ', row_dict)

            # ref = gclass.Gallery(row_dict)  # Gallery 객체 생성
            # print('gclass.Gallery.info(ref) : ', gclass.Gallery.info(ref))
            # gallery_list.append(ref)

            search_list.append(row_dict)

    except Exception as msg:
        print('Gallery search() 에러 발생 : ', msg)
    finally:
        cursor.close()
        odb.close(conn)

    print(search_list)
    return search_list
