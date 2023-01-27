import json
with open("./data/faps.json") as f:
    fap_data = json.load(f)

final_html = """
<style>
.fap-entry {
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  border: 2px solid #5B8FB9;
  margin: 10px;
  padding-left: 10px;
  padding-bottom: 10px;

  @media screen and (prefers-color-scheme: light) {
    border: 2px solid #301E67;
  }
}

body {
  background-color: #03001C;
  color: #B6EADA;
}
@media screen and (prefers-color-scheme: light) {
  body {
    background-color: #B6EADA;
    color: #03001C;
  }
}
</style>
"""
for fap in fap_data:
    final_html += f"""
<div class="fap-entry">
<h2 class="entry">Entry Number: {fap["entry"]}</h2>
<div class="datetime">Date & Time: {fap["datetime"]}</div>
<div class="duration">Duration: {fap["duration"]}</div>
<div class="comment">Comment: "{fap["comment"]}"</div>
</div>
    """

with open("faps.html", "w+") as f:
    f.write(final_html)
