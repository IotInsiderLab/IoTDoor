
from flask import Blueprint, json

from datetime import datetime
from flask import render_template
from Door import app

from flask import Response
from flask import request
import json
import time
from flask import Response, Flask
db = Blueprint('db', __name__)
#uri =app.config["kafkaurl"]


import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
# Initialize the Cosmos client
endpoint = ""
key = ''

# <create_cosmos_client>
#client = cosmos_client.CosmosClient(endpoint, {'masterKey': key})
client = cosmos_client.CosmosClient(endpoint, {'masterKey': key})

database_name = 'cartdemo'

container_name = 'doorstatus'
#database = client.ReadDatabase("dbs/" + database_name)
#database = client.get_database_client(database_name)
#container = database.get_container_client(container_name)
#container = client.ReadContainer("dbs/" + database['id'] + "/colls/" + container_name)
# Enumerate the returned items
import json


@db.route('/status/<string:deviceid>', methods=['GET'])
def dAT(deviceid):
    query = "SELECT top 1 c.DoorStatus FROM c order by c._ts desc"

    dat = []
    for item in  client.QueryItems("dbs/" + database_name + "/colls/" + container_name,
                              query,
                              {'enableCrossPartitionQuery': True}):
        dat.append(item)
    res = json.dumps(dat, indent=True)

    
    
    resp = Response(response=res,
                    status=200,
                    mimetype="application/json")
    return resp




