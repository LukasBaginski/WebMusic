import flask, json, random
import mysql.connector

PROJECT_PATH = "/Users/lukas/Documents/Programmieren/WebMusic"
DATA_PATH = PROJECT_PATH + "/data"

GET = ["GET"]
POST = ["POST"]
GETPOST = ["GET", "POST"]

app = flask.Flask(__name__)
db = mysql.connector.connect(
    host="192.168.243.57",
    username="webmusic",
    password="WebMusic22",
    database="webmusic"
)
cursor = db.cursor()

def reconnect():
    try: db.ping()
    except: db.reconnect()
    cursor = db.cursor()

def create_token(length: int = 30):
    out = ""
    for _ in range(length):
        r = random.randint(0, 2)
        if r == 0: out += chr(random.randint(65, 90))
        elif r == 1: out += chr(random.randint(97, 122))
        elif r == 2: out += chr(random.randint(48, 57))
        if _ % 6 == 0 and _ > 0: out += "-"
    return out

def check_token(token):
    sql = "SELECT token FROM users WHERE users.token = %s"
    cursor.execute(sql, (token))
    data = cursor.fetchall()[0]
    return len(data) > 0

@app.route("/")
def index():
    return "..."

@app.route("/login", methods=POST)
def login():
    reconnect()
    sql = "SELECT token FROM users WHERE users.username = %s AND users.password = %s;"
    cursor.execute(sql, (username, password))
    data = cursor.fetchall()
    if len(data) > 0:
        data = data[0]
        resp = flask.Response(json.dumps({"status": "success"}))
        token = data[0]
        resp.set_cookie("token", token)
        return resp
    return flask.Response("Unauthorized", 401)

@app.route("/song", methods=POST)
def song():
    reconnect()
    cookies = flask.request.cookies
    token = cookies.get("token")
    if not token: return json.dumps({"status": "missing token"})
    if check_token(token):
        data = json.loads(flask.request.decode("UTF-8"))
        song_id = data.get("song_id")
        if not song_id: return json.dumps({"status": "missing song_id"})
        # TODO: Get song quality (flac, m4a, mp3, ogg, ...)
        return flask.send_from_directory(DATA_PATH, f"/songs/{song_id}.flac")

app.run(host="0.0.0.0", host=80)
