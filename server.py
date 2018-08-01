import random

from pyecharts import Scatter3D
from flask import Flask, render_template
import unfinished_check

app = Flask(__name__)


# REMOTE_HOST = "https://pyecharts.github.io/assets/js"
REMOTE_HOST = "static/assets-master/js"


@app.route("/")
def hello():
    tl = unfinished_check.unfiished_excel_check_result()
    return render_template(
        "pyecharts.html",
        title="待验证补丁未完成统计",
        myechart=tl.render_embed(),
        host=REMOTE_HOST,
        script_list=tl.get_js_dependencies(),
    )

if __name__ == '__main__':
    app.run()