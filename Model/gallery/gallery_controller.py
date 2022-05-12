import common.oracle_db as odb
import Model.gallery.gallery_class as gclass
from datetime import datetime
from dateutil import tz


def select_all(u_no, op):
    conn = odb.connect()
    cursor = None
    gallery_list = []

    if op == '0' or op == 0:
        query = 'SELECT * ' \
                'FROM L_GALLERY ' \
                'JOIN L_USER USING (USER_NO) ' \
                'ORDER BY GALLERY_DATE DESC'
        print(query)
        try:
            cursor = conn.cursor()
            result = cursor.execute(query)

            for row in result:
                print(row)
                if row[9] is None:
                    r9 = ''
                else:
                    r9 = row[9]
                # print(type(row[6].strftime('%Y-%m-%d, %H:%M:%S')))
                row_dict = {'g_no': row[1], 'u_no': row[0], 'content': row[2],
                            'photopath': row[3], 'hashtag': row[4], 'rcount': row[5],
                            'date': row[6].strftime('%Y-%m-%d %H:%M:%S'), 'u_name': row[8], 'u_badge': r9}
                # print('row_dict : ', row_dict)

                # ref = gclass.Gallery(row_dict)  # Gallery 객체 생성
                # print('gclass.Gallery.info(ref) : ', gclass.Gallery.info(ref))
                # gallery_list.append(ref)

                gallery_list.append(row_dict)

        except Exception as msg:
            print('Gallery select_all_lately() 에러 발생 : ', msg)

    else:
        query = "SELECT * FROM(SELECT * FROM L_GALLERY T JOIN L_USER U ON U.USER_NO = T.USER_NO) A \
        RIGHT JOIN (SELECT COUNT(*) CNT, G.GALLERY_NO FROM L_GALLERY G LEFT JOIN L_LIKE L \
        ON G.GALLERY_NO = L.GALLERY_NO GROUP BY G.GALLERY_NO) B \
        ON A.GALLERY_NO = B.GALLERY_NO ORDER BY CNT DESC"
        print(query)
        try:
            cursor = conn.cursor()
            result = cursor.execute(query)

            for row in result:
                if row[10] is None:
                    r9 = ''
                else:
                    r9 = row[10]
                # print(type(row[6].strftime('%Y-%m-%d, %H:%M:%S')))
                row_dict = {'g_no': row[0], 'u_no': row[1], 'content': row[2],
                            'photopath': row[3], 'hashtag': row[4], 'rcount': row[5],
                            'date': row[6].strftime('%Y-%m-%d %H:%M:%S'), 'u_name': row[9], 'u_badge': r9}
                # print('row_dict : ', row_dict)

                gallery_list.append(row_dict)

        except Exception as msg:
            print('Gallery select_all() 에러 발생 : ', msg)

    query = 'SELECT * ' \
            'FROM L_LIKE ' \
            'WHERE USER_NO = ' + str(u_no)

    try:
        cursor = conn.cursor()
        like_result = cursor.execute(query).fetchall()

    except Exception as msg:
        print('Gallery select_all() like 에러 발생 : ', msg)

    finally:
        cursor.close()
        odb.close(conn)

    if int(u_no) > 0:
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

    return gallery_list


def select_one(g_no, u_no):
    comment_list = []
    conn = odb.connect()
    cursor = None
    query = 'SELECT * ' \
            'FROM L_COMMENT ' \
            'JOIN L_USER USING (USER_NO) ' \
            'WHERE GALLERY_NO = ' + g_no + \
            'order by comment_date desc'

    try:
        cursor = conn.cursor()
        result = cursor.execute(query)

        for row in result:
            row_dict = {'cu_name': row[6], 'content': row[3], 'c_date': row[4].strftime('%Y-%m-%d %H:%M:%S'),
                        'ru_no': row[0], 'c_no': row[1]}
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
            if row[9] is None:
                r9 = ''
            else:
                r9 = row[9]
            row_dict = {'u_no': row[0], 'g_no': row[1], 'content': row[2],
                        'photopath': row[3], 'hashtag': row[4], 'rcount': row[5],
                        'g_date': row[6].strftime('%Y-%m-%d %H:%M:%S'), 'gu_name': row[8], 'gu_badge': r9}
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


def insert_gallery(dic):
    conn = odb.connect()
    cursor = None

    if dic.get('hashtag')[0] != '#':
        hashtag = '#' + dic.get('hashtag')
    else:
        hashtag = dic.get('hashtag')

    query = "INSERT INTO L_GALLERY VALUES(L_GN_S.NEXTVAL, " + \
            str(dic['user_no']) + ", '" + str(dic['content']) + "', '" + str(dic['image']) + "', '" + hashtag + \
            "', DEFAULT, TO_DATE('" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "', 'RRRR-MM-DD HH24:MI:SS'))"
    print(query)

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except Exception as msg:
        print('Detail insert_gallery() 에러 발생 : ', msg)

    finally:
        cursor.close()
        odb.close(conn)

    return '갤러리작성완료'


def insert_reply(g_no, u_no, reply):
    conn = odb.connect()
    cursor = None

    query = "INSERT INTO L_COMMENT VALUES(L_CN_S.NEXTVAL, " + str(g_no) + ", " + str(u_no) + ", '" + str(
        reply) + "', DEFAULT)"

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except Exception as msg:
        print('Detail insert_reply() 에러 발생 : ', msg)

    finally:
        cursor.close()
        odb.close(conn)

    return '댓글작성완료'


def modify_gallery(dic):
    conn = odb.connect()
    cursor = None

    if dic.get('hashtag')[0] != '#':
        hashtag = '#' + dic.get('hashtag')
    else:
        hashtag = dic.get('hashtag')

    query = "update l_gallery set gallery_content = '" + dic['content'] + "', " + \
            "hashtag = '" + hashtag + "' where gallery_no = " + str(dic.get('g_no'))

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except Exception as msg:
        print('Detail modify_gallery() 에러 발생 : ', msg)

    finally:
        cursor.close()
        odb.close(conn)

    return '갤러리수정완료'


def delete_gallery(g_no):
    conn = odb.connect()
    cursor = None

    query = "delete from l_comment where gallery_no = " + str(g_no)

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except Exception as msg:
        print('Detail delete_gallery_comment() 에러 발생 : ', msg)

    query = "delete from l_gallery where gallery_no = " + str(g_no)

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except Exception as msg:
        print('Detail delete_gallery() 에러 발생 : ', msg)

    finally:
        cursor.close()
        odb.close(conn)

    return '갤러리삭제완료'


def delete_reply(c_no):
    conn = odb.connect()
    cursor = None

    query = "delete from L_COMMENT where comment_no = " + str(c_no)

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except Exception as msg:
        print('Detail delete_reply() 에러 발생 : ', msg)

    finally:
        cursor.close()
        odb.close(conn)

    return '댓글삭제완료'


def gallike(g_no, u_no, onoff):
    conn = odb.connect()
    cursor = None

    if onoff == '1':
        query = 'DELETE FROM L_LIKE ' \
                'WHERE GALLERY_NO = ' + str(g_no) + ' AND USER_NO = ' + str(u_no)
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
                'VALUES(' + str(u_no) + ', ' + str(g_no) + ', DEFAULT)'
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
