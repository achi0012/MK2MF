"""
Collect results for each test to generate an HTML report.
$ python report_gen.py 5974_Golden_DTV_3-2-1_1_220310161818.json 5974_Golden_DTV_3-2-1_1_220310141442
"""
import base64, json, os, sys
from jinja2 import Template
from PIL import Image
from io import BytesIO

REPORT_NAME = sys.argv[1].replace(".json", "")

RESULTS_FILE = os.path.normpath(os.path.join(os.getcwd(), sys.argv[1]))
# print(RESULTS_FILE)
with open(RESULTS_FILE, "r") as f:
  results = json.load(f)

print(results["gold"])

GOLDEN_RECORD = sys.argv[2]
print(GOLDEN_RECORD)

# Summarize data for templating
def findMatch(results, gold):
  for pair in results["paired"]:
    if pair["gold"] == gold:
      return pair

def getImageData(clip_name, file_name):
  FILE_PATH = os.path.normpath(
    os.path.join(
      "C:\\MicroFocus\\MediaServer_12.10.0_WINDOWS_X86_64\\output\\target_frames", 
      clip_name, file_name
    )
  )
  image = Image.open(FILE_PATH)
  MAX_SIZE = (200, 200)
  image.thumbnail(MAX_SIZE)

  buffered = BytesIO()
  image.save(buffered, format="PNG")
  image_byte_str = base64.b64encode(buffered.getvalue())
  image_b64_str = image_byte_str.decode("ascii")

  return f'data:image/png;base64,{image_b64_str}'

matches = []
for g in results["gold"]:
  print(g)
  match = findMatch(results, g)

  if match:
    matches.append({
      "probe": match["probe"],
      "similarity": match["similarity"],
      "probe_img": getImageData(REPORT_NAME, match["probe"]),
      "gold": g,
      "gold_img": getImageData(GOLDEN_RECORD, g+".png")
    })
  else: 
    matches.append({
      "probe": None,
      "similarity": None,
      "probe_img": None,
      "gold": g,
      "gold_img": getImageData(GOLDEN_RECORD, g+".png")
    })

anomalies = []
for u in results["unpaired"]:
  anomalies.append({
    "data": u,
    "probe_img": getImageData(REPORT_NAME, u["probe"])
  })

# Produce templated report
TEMPLATE_FILE = os.path.join(os.getcwd(), "report.html.jinja")
with open(TEMPLATE_FILE, "r") as f:
  jt = Template(f.read())

REPORT_FILE = RESULTS_FILE.replace(".json", ".html")
with open(REPORT_FILE, "w") as f:
  f.write(jt.render({
    "n_paired": len(results["paired"]),
    "matches": matches, 
    "anomalies": anomalies, 
    "test_file": REPORT_NAME,
    "golden_file": GOLDEN_RECORD
  }))
