import json


def StrToJson():

    str = '[{"id": 50002, "nodeList": [{"id": 50023, "nodeList": []}, {"id": 50005, "nodeList": []}, {"id": 50009, "nodeList": []}, {"id": 49988, "nodeList": [{"id": 50022, "nodeList": []}, {"id": 49989, "nodeList": []}, {"id": 49990, "nodeList": []}, {"id": 50038, "nodeList": []}, {"id": 50557, "nodeList": []}]}, {"id": 50001, "nodeList": [{"id": 50003, "nodeList": [{"id": 50032, "nodeList": []}, {"id": 50004, "nodeList": []}, {"id": 50036, "nodeList": []}, {"id": 50037, "nodeList": []}]}, {"id": 49999, "nodeList": [{"id": 50039, "nodeList": []}, {"id": 49991, "nodeList": [{"id": 50010, "nodeList": [{"id": 49981, "nodeList": []}, {"id": 50008, "nodeList": []}, {"id": 50030, "nodeList": []}, {"id": 50559, "nodeList": []}]}, {"id": 49992, "nodeList": []}, {"id": 50033, "nodeList": []}, {"id": 50560, "nodeList": []}, {"id": 49982, "nodeList": [{"id": 49987, "nodeList": []}, {"id": 49986, "nodeList": []}, {"id": 49985, "nodeList": []}, {"id": 49984, "nodeList": []}, {"id": 49983, "nodeList": []}, {"id": 50034, "nodeList": []}, {"id": 50561, "nodeList": []}]}]}, {"id": 49975, "nodeList": [{"id": 49976, "nodeList": []}, {"id": 49977, "nodeList": []}, {"id": 50029, "nodeList": []}, {"id": 50028, "nodeList": []}, {"id": 50035, "nodeList": []}, {"id": 50562, "nodeList": []}, {"id": 49978, "nodeList": [{"id": 49979, "nodeList": []}, {"id": 49980, "nodeList": []}, {"id": 50024, "nodeList": []}, {"id": 50026, "nodeList": []}, {"id": 50025, "nodeList": []}]}]}]}, {"id": 49994, "nodeList": [{"id": 49995, "nodeList": []}]}, {"id": 49996, "nodeList": [{"id": 50011, "nodeList": []}, {"id": 50012, "nodeList": []}, {"id": 50013, "nodeList": []}, {"id": 50014, "nodeList": []}, {"id": 49997, "nodeList": []}, {"id": 50015, "nodeList": []}, {"id": 49998, "nodeList": []}, {"id": 50016, "nodeList": []}, {"id": 50017, "nodeList": []}, {"id": 50018, "nodeList": []}, {"id": 50019, "nodeList": []}, {"id": 50000, "nodeList": []}, {"id": 50020, "nodeList": []}, {"id": 50021, "nodeList": []}, {"id": 50563, "nodeList": []}]}, {"id": 50006, "nodeList": [{"id": 50031, "nodeList": []}, {"id": 49993, "nodeList": []}, {"id": 50565, "nodeList": []}, {"id": 50007, "nodeList": []}, {"id": 50027, "nodeList": []}, {"id": 50566, "nodeList": []}]}]}]}]'
    js = json.loads(str)
    # print(js)
    # for k in js:
    #     print(k)

    return js

def getId(lt, count):
    count += 1
    for l1 in lt:
        for k in l1:
            if k == "id":
                print(count * '\t\t',end='')
                print(l1[k])
            if k == "nodeList":
                getId(l1[k], count)







if  __name__ == '__main__':
    js = StrToJson()
    getId(js, -1)






