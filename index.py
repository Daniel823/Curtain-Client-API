from flask import request
from flask_api import FlaskAPI, status, exceptions
import json
from modules import MicroController as mc

app = FlaskAPI(__name__)

@app.route("/state", methods=['GET'])
def get():
    """
    GET :   returns the item state with 2** status code
            4**, 5** accordingly if MicroController is not avaliable
    """
    return json.dumps(mc.getState())

@app.route("/update/<int:action>/", methods=['POST'])
def post(action):
    """
    POST :  tells the client what to do ie. close/open the blind
            returns status codes 2**, 4**, 5** accordingly
    """
    if(mc.updateState(action)):
        return status.HTTP_200_OK

    return status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    app.run(debug=False)
