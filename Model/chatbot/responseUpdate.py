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


def trans(questext):
    file = open("./static/intents.json", encoding="UTF-8")
    data = json.loads(file.read())
    requestext = ""
    for i in data['intents']:
        if i['tag'] != 'error':
            for t in i['patterns']:
                if t in questext:
                    print(t)
                    requestext = questext.replace(t, "! " + t + " !")
                    print("[" + questext + "]가 [" + requestext + "]으로 변경됨")
    if requestext == "":
        return questext
    else:
        return requestext


def run(landmark):
    file = open("./static/intents.json", encoding="UTF-8")
    data = json.loads(file.read())

    address = selectLandmarkAddress(landmark)

    weater = address.split('시 ')[1].split('구 ')[0] + "구 날씨"

    for i in data['intents']:
        if i['tag'] == 'address':
            i['responses'] = ["[" + landmark + "]의 주소는 [" + address + "]입니다. <br> <a href='https://map.naver.com/v5/search/" + address + " " + landmark + "' target='_blank'>여기</a>를 누르시면 위치를 보실 수 있습니다."]
        if i['tag'] == 'weather':
            i['responses'] = ["[" + landmark + "]의 날씨 상황은 <br> <a href='https://search.naver.com/search.naver?query=" + weater + "' target='_blank'>여기</a>를 누르시면 날씨를 보실 수 있습니다."]
        if i['tag'] == 'restaurant':
            i['responses'] = ["[" + landmark + "]의 맛집은 <br> <a href='https://map.naver.com/v5/search/" + address + " 맛집' target='_blank'>여기</a>를 누르시면 지도로 보실 수 있습니다."]

    return data
