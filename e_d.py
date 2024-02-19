import base64

r = "rajasekharreddy"
ed = base64.b64encode(r.encode('utf-8')).decode('utf-8')
print(ed)


s = "cmFqYXNla2hhcnJlZGR5"
db = base64.b64decode(s)
ds = db.decode('utf-8')
print(ds)
