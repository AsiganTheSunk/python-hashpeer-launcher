#!/usr/bin/python3

# Basic Command from the server
message_separator = '////////////' * 10

#
LOCAL_HOST = '127.0.0.1'

#
DNS_SERVERS = {
    'google_0': '8.8.8.8',
    'google': '8.8.4.4',
    'cloud_flare': '1.1.1.1',
    'comodo_0': '8.26.56.26',
    'comodo_1': '8.20.247.20',
    'quad9_0': '9.9.9.9',
    'quad9_1': '149.112.112.112',
    'yandex.dns_0': '77.88.8.8',
    'yandex.dns_1': '77.88.8.1',
    'dns.watch_0': '84.200.69.80',
    'dns.watch_1': '84.200.70.40',
    'lvl3_0': '209.244.0.3',
    'lvl3_1': '208.244.0.4',
    'dns_advantage_0': '156.154.70.1',
    'dns_advantage_1': '156.154.71.1',
    'open_mic_0': '46.151.208.154',
    'open_mic_1': '128.199.248.105',
    'dyn_0': '216.146.35.35',
    'dyn_1': '216.146.36.36',
    'safedns_0': '195.46.39.39',
    'safedns_1': '195.46.39.40',
    'cleanbrowsing_0': '185.228.168.9',
    'cleanbrowsing_1': '185.228.169.9',
    'verising_0': '64.6.64.6',
    'verising_1': '64.6.65.6',
    'alternativedns_0': '198.101.242.72',
    'alternativedns_1': '23.253.163.53',
    'smartvyper_0': '208.76.50.50',
    'smartvyper_1': '208.76.51.51',
    'uncensoreddns_0': '91.239.100.100',
    'uncensoreddns_1': '89.233.43.71',
    'hurricaneelectric_0': '74.82.42.42',
    'puntcat_0': '109.69.8.51',
    'ultradns_0': '156.154.71.1',
    'ultradns_1': '156.154.70.1',
    'sprintlink_0': '204.97.212.10',
    'sprintlink_1': '199.2.252.10',
    'sprintlink_2': '204.117.214.10',
    'momentum_0': '209.55.1.220',
    'momentum_1': '209.55.0.110',
    'directmediaasn_0': '204.194.232.200',
    'directmediaasn_1': '204.194.234.200',
    'nttcomunications_0': '208.67.220.220'
}