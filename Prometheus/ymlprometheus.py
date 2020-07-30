influx - precision  rfc3339 - username admin - password '123'

# influx -precision rfc3339 -username admin -password '123'
> show measurements
>  SELECT * FROM go_info
>  SELECT * FROM go_info WHERE time >= '2020-07-14'

remote_write:
  - url: "http://15.206.42.79:8086/api/v1/prom/write?db=hpcmetrics&u=admin&p=123"

remote_read:
  - url: "http://localhost:8086/api/v1/prom/read?db=prometheus&u=username&p=password"

global:

external_labels:
dc: europe1
alerting:
alert_relabel_configs:
- source_labels: [dc]
regex: (.+)\d +
target_label: dc
alertmanagers:
- static_configs:
- targets: ['prom1:9093', 'prom2:9093']

remote_write:
- url: "http://15.206.42.79:8086/api/v1/prom/write?db=hpcmetrics"
- url: "http://13.232.15.89:8080/receive"

remote_read:
- url: "http://15.206.42.79:8086/api/v1/prom/read?db=hpcmetrics"

-----------------

# my global config
global:
scrape_interval: 15
s  # Set the scrape interval to every 15 seconds. Default is every 1 minute.
evaluation_interval: 15
s  # Evaluate rules every 15 seconds. The default is every 1 minute.
# scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
alertmanagers:
- static_configs:
- targets:
# - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
# - "first_rules.yml"
# - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
# The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
- job_name: 'gcp_slurm_cluster'

# metrics_path defaults to '/metrics'
# scheme defaults to 'http'.

static_configs:
- targets: ['35.208.120.32:8080']
- job_name: 'slurm2'
static_configs:
- targets: ['35.209.219.226:8080']
remote_write:
- url: "http://15.206.42.79:8086/api/v1/prom/write?db=prom1metrics&u=pr&p=111"

remote_read:
- url: "http://15.206.42.79:8086/api/v1/prom/read?db=prom1metrics&u=pr&p=111"

-----------------------