# Grafana Dashboards for Ceph monitoring

This package provides a few Grafana dashboards, that should help
monitor a ceph cluster. The dasboards are based the prometheus as a data
source and expect prometheus to collect data from node_exporter and ceph_exporter
(https://github.com/prometheus/node_exporter and https://github.com/digitalocean/ceph_exporter).
The dashboards are installed to /var/lib/grafana-dashboards-ceph. Make sure to set the
following config in /etc/grafana/grafana.ini:
```
    [dashbords.json]
        enabled = true
        path = /var/lib/grafana-dashboards-ceph
```
