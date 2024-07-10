import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")
ENDPOINT_SCHEMA_URL  = os.environ.get("ENDPOINT_SCHEMA_URL")
BOOTSTRAP_SERVER = 'pkc-l7j7w.asia-east1.gcp.confluent.cloud:9092'
SECURITY_PROTOCOL = 'SASL_SSL'
SSL_MECHANISM = 'PLAIN'
SCHEMA_REGISTRY_API_KEY = os.environ.get("SCHEMA_REGISTRY_API_KEY")
SCHEMA_REGISTRY_API_SECRET = os.environ.get("SCHEMA_REGISTRY_API_SECRET")

dbname = os.environ.get("DB_NAME")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
port = os.environ.get("PORT")

def config_values():
	return API_KEY, ENDPOINT_SCHEMA_URL, API_SECRET_KEY, BOOTSTRAP_SERVER, SECURITY_PROTOCOL, SSL_MECHANISM, SCHEMA_REGISTRY_API_KEY, SCHEMA_REGISTRY_API_SECRET
	
def db_values():
	return dbname, user, password, host, port
