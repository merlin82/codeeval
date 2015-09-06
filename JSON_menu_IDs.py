import sys
import json
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    id = 0
    s = json.loads(test)
    for item in s["menu"]["items"]:
        try:
            if "label" in item:
                id += item["id"]
        except:
            pass
    print id
test_cases.close()

