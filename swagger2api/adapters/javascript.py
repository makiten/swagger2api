import json


def convert(swagger):
    data = json.loads(swagger)
    vals = {}
    if data['schemes'].length > 0:
        if 'https' in data['schemes']:
            vals['proto'] = 'https'
        else:
            vals['proto'] = data['schemes'][0]
    else:
        raise Exception('Could not find an API scheme.')
    vals['base_path'] = '{0}{1}'.format(data['host'], data['basePath'])

    vals['actions'] = []
    for endpoint, actions in data['paths'].items():
        action = {
            'endpoint': endpoint
        }

        for method, details in actions.items():
            action['method'] = method
            action['function'] = details['operationId']
        vals['actions'].append(action)

    return vals
