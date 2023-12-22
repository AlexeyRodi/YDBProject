import ydb

from buyers_reader import reader
from dbclient import ydb_client
from serialize import to_json_array
from exception import ConnectionFailure

import json

pool = ydb.SessionPool(ydb_client.create_driver())

def bad_request(code: int = 400, body = None):
  return { 
    'statusCode': code,
    'body': body
  }

def usual_responce(result):
  return { 
    'statusCode': 200,
    'body': to_json_array(result[0].rows)
  }

def automobile_get_request(parameters):
  if parameters['data'] == 'buyers_list':
    return usual_responce(pool.retry_operation_sync(reader.buyers_with_purchase))
  else:
    return bad_request('Incorrect query parameters')

def handler(event, context):
  if(event['httpMethod'] == 'GET'):
    return automobile_get_request(event['queryStringParameters'])
  else:
    return bad_request()
  return {
    'statusCode': 200
  }