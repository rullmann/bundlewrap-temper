directories = {
    "/opt/usb-thermometer": {
        "mode": "0755",
    },
}

git_deploy = {
    "/opt/usb-thermometer": {
        'repo': "https://github.com/petervojtek/usb-thermometer.git",
        'rev': "master",
        'needs': [
            "directory:/opt/usb-thermometer",
        ],
    },
}

files = {
    '/opt/usb-thermometer/make-temper.sh': {
        'source': "make_temper.sh",
        'owner': "root",
        'mode': "0755",
        'content_type': "mako",
        'needs': [
            "git_deploy:/opt/usb-thermometer",
        ],
        'triggers': [
            "action:temper_make",
        ],
    },
}

actions = {
    'temper_make': {
        'command': "/opt/usb-thermometer/make-temper.sh",
        'triggered': True,
    },
}

if node.has_bundle("collectd"):
    files['/etc/collectd.d/temper.conf'] = {
        'source': "collectd.conf",
        'mode': "0640",
        'owner': "root",
        'group': "root",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    }

    files['/opt/usb-thermometer/collectd.sh'] = {
        'source': "collectd.sh",
        'mode': "0755",
        'owner': "nobody",
        'group': "root",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    }