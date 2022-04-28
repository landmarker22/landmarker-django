from datetime import datetime

import cx_Oracle
import common.oracle_db as odb
import Model.gallery.gallery_class as gclass

def select_all():
    conn = odb.connect()
    cursor = None
    query = 'SELECT * ' \
            'FROM L_GALLERY ' \
            'JOIN L_USER USING (USER_NO)'
    gallery_list = []

    try:
        cursor = conn.cursor()
        result = cursor.execute(query)
        print(result)
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
    finally:
        cursor.close()
        odb.close(conn)
    print('gallery_list : ', gallery_list)
    return gallery_list

def select_one(g_no):
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

            detail_list.append(row_dict)

    except Exception as msg:
        print('Detail select_one() detail 에러 발생 : ', msg)

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
    return detail_list, comment_list, c_count_result
    # return detail_result, comment_result, c_count_result
