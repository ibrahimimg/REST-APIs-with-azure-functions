import logging

import azure.functions as func
import pymongo
import os
from bson.json_util import dumps
from bson import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    _id = req.params.get('id')

    try:
        client = pymongo.MongoClient(os.environ.get('MongoDB_conn'))
        database = client['func_DB']
        collection = database['tasks']
        # find a task with the specified id and delete it
        q = collection.find_one_and_delete({"_id": ObjectId(_id)})
        
        # check if query returned a data or not
        if q is not None:
            return func.HttpResponse("Deleted", status_code=204)
        else:
            return func.HttpResponse('Task doest not exist!', status_code=404)
    
    except:
        return func.HttpResponse("Something went wrong!", status_code=500)
