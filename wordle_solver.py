import re
import datetime
import requests


wordle_js = requests.get("https://www.powerlanguage.co.uk/wordle/main.e65ce0a5.js")
c_words = re.search("(?P<w_list>\"cigar\".*?\"shave\")", wordle_js.text).group("w_list").split(",")
f_min= datetime.datetime(year=2021, month=6, day=18)
today = datetime.datetime.now()

print(f"""__        __            _ _        ____        _
\ \      / /__  _ __ __| | | ___  / ___|  ___ | |_   _____ _ __
 \ \ /\ / / _ \| '__/ _` | |/ _ \ \___ \ / _ \| \ \ / / _ \ '__|
  \ V  V / (_) | | | (_| | |  __/  ___) | (_) | |\ V /  __/ |
   \_/\_/ \___/|_|  \__,_|_|\___| |____/ \___/|_| \_/ \___|_|
                                                                by Satoki
{'-'*70}
Today: {c_words[(today-f_min).days - 1][1:-1]}
Tommorow: {c_words[(today-f_min).days][1:-1]}
{'-'*70}""")