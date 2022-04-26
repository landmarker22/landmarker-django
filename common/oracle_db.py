# oracle_db.py

import cx_Oracle

# 사용자 정의 변수
dbURL = "localhost:1521/xe"
dbUSER = "c##student2"  # 아이디
dbPASSWD = "student2"  # 비번


def oracle_init():  # 애플리케이션 구동시 딱 한번 실행되어야 함
    cx_Oracle.init_oracle_client(lib_dir="C:\instantclient_21_3")


def connect():
    try:
        print(cx_Oracle.connect(dbUSER, dbPASSWD, dbURL))
        return cx_Oracle.connect(dbUSER, dbPASSWD, dbURL)
    except Exception as msg:
        print('오라클 연동 관련 에러 발생 : ', msg)


def close(conn):
    try:
        conn.close()
    except Exception as msg:
        print("오라클 연동 해제 에러 발생 : ", msg)


def commit(conn):
    try:
        conn.commit()
    except Exception as msg:
        print("오라클 트랜잭션 커밋 에러 발생 : ", msg)


def rollback(conn):
    try:
        conn.rollback()
    except Exception as msg:
        print("오라클 트랜잭션 롤백 에러 발생 : ", msg)
