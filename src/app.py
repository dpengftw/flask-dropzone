# -*- coding: utf-8 -*-
"""
    :author: Grey Li <withlihui@gmail.com>
    :copyright: (c) 2017 by Grey Li.
    :license: MIT, see LICENSE for more details.
"""
import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE=os.getenv('DROPZONE_ALLOWED_FILE_TYPE', 'default'),
    DROPZONE_MAX_FILE_SIZE=os.getenv('DROPZONE_MAX_FILE_SIZE', 30,
    DROPZONE_MAX_FILES=30,
    DROPZONE_PARALLEL_UPLOADS=os.getenv('DROPZONE_PARALLEL_UPLOADS', 9),  # set parallel amount
    DROPZONE_UPLOAD_MULTIPLE=True,  # enable upload multiple
)

dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
