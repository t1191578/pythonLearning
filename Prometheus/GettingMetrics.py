from  flask import Flask ,request
from flask_restful import Resource, Api
import requests
app =Flask(__name__)
api = Api(app)

#cluster = {'metric': {'name':"slurm_nodes_idle" ,'instance':"35.209.219.226:8080",'job':"slurm2"},
 #          'value':{0:1593766788.942, '1':"3"}}

resp = requests.get('http://15.206.250.89:9090/api/v1/query?query=slurm_cpus_total{job=%22slurm2%22}')
if resp.status_code != 200:

    raise ApiError('GET /cluster/ {}'.format(resp.status_code))
#print(resp.json())
val= resp.json()
cluster = val['data']['result'][0]

class Cluster(Resource):

    def get(self, name, cpus_idle):
        if cluster['metric']['job'] == name:
            return {'cluster': cluster['metric']['job'], 'slurm_cpus_idle': cluster['value'][1]}, 200
        else:
            return None, 404

    def get(self, name, cpus_idle):
        if cluster['metric']['job'] == name:
            return {'cluster': cluster['metric']['job'], 'slurm_cpus_idle': cluster['value'][1]}, 200
        else:
            return None, 404

api.add_resource(Cluster, '/cluster/<string:name>/<string:cpus_idle>')
api.add_resource(Cluster, '/cluster/<string:name>/<string:nodes_idle>')
#api.add_resource(Cluster, '/cluster/<string:name>/<string:memory_available>')
app.run(port=5000)