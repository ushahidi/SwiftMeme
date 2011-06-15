# SwiftMeme Controllers
# =====================
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from config  import *
from flask   import Flask, jsonify, request
from gateway import Gateway

app = Flask(__name__)
gateway = Gateway(GATEWAY_BASE, GATEWAY_KEY, GATEWAY_SECRET)

@app.route("/api/authenticate", methods=["POST"])
def login():
    return jsonify(gateway.authenticate(**request.form))

@app.route("/api/register", methods=["POST"])
def register():
    return jsonify(gateway.register(**request.form))

@app.route("/api/getmemeanalytics", methods=["POST"])
def getmemeanalytics():
    return jsonify(gateway.getmemeanalytics(**request.form))

@app.route("/api/getmemecontent", methods=["POST"])
def getmemecontent():
    return jsonify(gateway.getmemecontent(**request.form))

@app.route("/api/getmemeoverview", methods=["POST"])
def getmemeoverview():
    return jsonify(gateway.getmemeoverview(**request.form))

def main():
    app.debug = DEBUG_MODE
    app.run(host=HOST_IP)

if __name__ == "__main__":
    main()
