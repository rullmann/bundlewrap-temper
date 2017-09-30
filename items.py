directories = {
    '/opt/usb-thermometer': {
        'mode': '0755',
    },
}

git_deploy = {
    '/opt/usb-thermometer': {
        'repo': 'https://github.com/petervojtek/usb-thermometer.git',
        'rev': 'master',
        'needs': ['directory:/opt/usb-thermometer'],
    },
}

files = {
    '/opt/usb-thermometer/make-temper.sh': {
        'source': 'make_temper.sh',
        'mode': '0755',
        'content_type': 'mako',
        'needs': ['git_deploy:/opt/usb-thermometer'],
        'triggers': ['action:temper_make'],
    },
    '/etc/udev/rules.d/99-tempsensor.rules': {
        'source': '99-tempsensor.rules',
        'mode': '0644',
    },
}

actions = {
    'temper_make': {
        'command': '/opt/usb-thermometer/make-temper.sh',
        'triggered': True,
    },
}

if node.has_bundle('collectd'):
    files['/etc/collectd.d/temper.conf'] = {
        'source': 'collectd.conf',
        'mode': '0640',
        'triggers': ['svc_systemd:collectd:restart'],
    }

    files['/opt/usb-thermometer/collectd.sh'] = {
        'source': 'collectd.sh',
        'mode': '0755',
        'triggers': ['svc_systemd:collectd:restart'],
    }