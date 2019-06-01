from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import json
from rq import Queue
from redis import Redis
from data_processing import task
from . import config

redis_host = config.REDIS_HOST
redis_port = config.REDIS_PORT
source = config.SOURCE_FILE_PATH
destination = config.DESTINATION_FILE_PATH


redis_conn = Redis(host=redis_host, port=redis_port)



def compute_score(query_list, set_words):
    return float(len(set(query_list) & set(set_words.split(",")))/len(query_list))

def read_file():
	df = pd.read_csv(destination)
	return df

class DataProcessingAPI(APIView):
	def get(self, request):
		q = Queue("task", connection=redis_conn)
		job = q.enqueue(task.text_to_dataframe, source=source,destination=destination,timeout='2h')
		return Response({"Response":"Started"})

class ScoreAPI(APIView):
	def get(self, request):
		try:
			df = read_file()
			final = df.head(20)
			final['json'] = final.apply(lambda x: json.loads(x.to_json()), axis=1)
			return Response(json.loads(final['json'].to_json()))
		except Exception as e:
			return Response({"error":e, "response":"File not be present"})

	def post(self, request, format=None):
		query_string = request.data['query']
		query_list = query_string.split(",")
		df = read_file()
		df['score'] = df['set_words'].apply(lambda x: compute_score(query_list,x))
		final = df.sort_values(["score","review/score"],ascending=False).reset_index(drop=True).head(20)
		final['json'] = final.apply(lambda x: json.loads(x.to_json()), axis=1)
		return Response(json.loads(final['json'].to_json()))
# Create your views here.
