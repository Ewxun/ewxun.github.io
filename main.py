from flask import Flask, request, send_file, render_template, redirect
import json

from assets.templates.friends.manager import renew_template

app = Flask('Ewxun Files', template_folder="assets/templates", static_folder="assets/templates")


with open("idlist.pdf","rb") as f:
  dabytes = f.read()
with open("assets/downloads/newlist.pdf", "wb") as f:
  f.write(dabytes)


@app.route('/')
def homepage():
  return render_template("mainpage/index.html")
  #return '<title>Ewxun\'s Website</title><h1>Welcome To Ewxun\'s Site</h1><body>This is where I keep my stuff.</body>'

@app.route("/mcskin")
def mcskins():
  try:
    skin = request.args["type"].lower()
    if skin not in ["normal", "xmas", "maid"]:
      raise ValueError
  except:
    return "All my Minecraft Skins Storage"
  return send_file(f"assets/mcskins/{skin}_Ewxun.png", mimetype="image/png")

@app.route("/dlfile")
def downloads():
  reqargs = request.args
  
  if "filename" not in reqargs.keys():
    return "No Filename was Provided"
  if "filename" in reqargs.keys() and "." not in reqargs["filename"]:
    return "Filename needs to include its extension"
  if "path" not in reqargs.keys():
    filename = reqargs["filename"]
    dapath = "assets/downloads/"
  if "filename" in reqargs.keys() and "path" in reqargs.keys():
    filename = reqargs["filename"]
    dapath = reqargs["path"]

  return send_file(dapath+filename, as_attachment=True)

@app.route("/science")
def scimeet():
  with open("meetlink.txt", "r") as f:
    meetlink = f.read()
  return redirect(meetlink)

@app.route("/friends/create")
def eng_friends_create():
  return render_template("friends/create.html")

@app.route("/friends", methods=["GET","POST"])
def eng_friend_home():
  dbloc = "assets/templates/friends/flist.json"
  if request.method == "POST":
    with open(dbloc, "r") as f:
      flist = json.loads(f.read())
    print(request.form)
    newfriend = dict(request.form)
    flist.append(newfriend)
    with open(dbloc, "w") as f:
      f.write(json.dumps(flist, indent=2, ))
      return redirect("https://www.ewxun.ml/friends")
  else:
    return render_template("friends/home.html")

@app.route("/friends/view/<name>")
def view_friend(name):
  try:
    return render_template(f"friends/profiles/{name}.html")
  except:
    return "Non Existant"

@app.route("/anonymous_qna")
def anon_qna():
  return render_template("qna/index.html")

@app.route("/anonymous_qna/submit", methods=["POST"])
def anon_qna_receive():
  #print(request.form)
  with open("qna.txt", "a") as f:
    f.write(request.form["message"])
    f.write("\n")
  return "OK"

@app.route("/anonymous_qna/view", methods=["GET"])
def anon_qna_view():
  with open("qna.txt", "r") as f:
    cont = f.read()
  return "<style>body{font-size: 100px; font-family: comic sans ms;}</style><body>"+f"{cont}</body>".replace("\n", "<br><br>")


renew_template()
app.run(host='0.0.0.0', port=8080)