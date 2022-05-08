import json
import common.oracle_db as odb


def selectLandmarkAddress(landmark):
    conn = odb.connect()
    cursor = None
    landmarkAddress = ""

    query = "SELECT * " + \
            "FROM L_LANDMARK " + \
            "WHERE LANDMARK_NAME = '" + landmark + "'"
    try:
        cursor = conn.cursor()
        result = cursor.execute(query).fetchone()
        landmarkAddress = result[2]
        print(landmarkAddress)
    except Exception as msg:
        print('selectLandmarkAddress() 에러 발생 : ', msg)
    finally:
        cursor.close()
        odb.close(conn)
        return landmarkAddress


def run(landmark):
    file = open("./static/intents.json", encoding="UTF-8")
    data = json.loads(file.read())

    for i in data['intents']:
        if i['tag'] == 'address':
            i['responses'] = ["[" + landmark + "]의 주소는 [" + selectLandmarkAddress(landmark) + "]입니다."]
        if i['tag'] == 'weather':
            i['responses'] = ["날씨야"]
        if i['tag'] == 'restaurant':
            i['responses'] = ["맛집이야"]

    return data
