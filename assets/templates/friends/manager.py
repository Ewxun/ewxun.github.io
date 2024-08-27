import json, os

flistloc = "assets/templates/friends/flist.json"
#    <li>Me <3</li>

def renew_template():
  data = ""
  with open(flistloc, "r") as f:
    flist = json.loads(f.read())

  nlist = [name["name_en"].lower().replace(" ", "_") for name in flist]
  for name in nlist:
    if f"{name}.html" in os.listdir("assets/templates/friends/profiles"):
      data += f"    <li><a href=\"https://www.ewxun.ml/friends/view/{name}\">{name.title().replace('_', ' ')}</a></li>\n"
    else:
      data += f"    <li>{name.title().replace('_', ' ')}</li>"

  with open("assets/templates/friends/home_template.html", "r") as f:
    oritem = f.read()

  with open("assets/templates/friends/home.html", "w") as f:
    f.write(oritem.replace("%%dalist%%", data))