
from wsgiref import simple_server
from flask import Flask
import os
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard
import json

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)


@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return "Flask app is running"




port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()



# It's worth noting that the pip freeze command only lists packages that have been installed using
# pip, so if you have other packages installed in your Python environment that were not installed
# using pip, they will not be listed. Additionally, if you are using a virtual environment, the pip
# freeze command will only list packages installed in that virtual environment, not in the global
# Python environment.