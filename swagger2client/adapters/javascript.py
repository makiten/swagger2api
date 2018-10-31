from jinja2 import Environment, FileSystemLoader
import json
import os

__templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'templates', 'javascript')
env = Environment(loader=FileSystemLoader(__templates_dir))


def convert(swagger):
    """

    :param swagger:
    :return:
    :rtype: string
    """
    data = json.loads(swagger)

    vals = create_template_vars_from_swagger(data)

    return render(vals)


def create_template_vars_from_swagger(data):
    """

    :param data:
    :rtype: dict

    """
    vals = {}

    if 'schemes' in data and data['schemes'].length > 0:
        if 'https' in data['schemes']:
            vals['proto'] = 'https'
        else:
            vals['proto'] = data['schemes'][0]
    else:
        vals['proto'] = 'http'
        # raise Exception('Could not find an API scheme.')
    vals['base_path'] = '{0}{1}'.format(data['host'], data['basePath'])

    vals['actions'] = []
    for endpoint, actions in data['paths'].items():
        action = {
            'endpoint': endpoint
        }

        for method, details in actions.items():
            action['method'] = method
            action['function'] = details['summary'] if details['summary'] != '' else details['operationId']
            if method.lower() in ['patch', 'put', 'post']:
                action['data'] = {}
                for p in details['parameters']:
                    if p['in'] == 'body':
                        action['data'][p['name']] = p['name']
            if 'parameters' in details:
                action['args'] = [
                    '{0} = \'\''.format(p['name']) if 'required' in p and not p['required'] else p['name'] for p in
                    details['parameters']]
        vals['actions'].append(action)

    return vals


def render(vals=None):
    """

    :param vals:
    :rtype: string
    """
    outputs = []

    inits_tpl = env.get_template('inits.js.tpl')
    header_tpl = env.get_template('header.js.tpl')
    function_tpl = env.get_template('function.js.tpl')
    footer_tpl = env.get_template('footer.js.tpl')
    exports_tpl = env.get_template('exports.js.tpl')

    functions = [a['function'] for a in vals['actions']]
    outputs.append(inits_tpl.render(proto=vals['proto'], base_path=vals['base_path']))
    for action in vals['actions']:
        outputs.append(header_tpl.render(section=''))
        outputs.append(function_tpl.render(function=action['function'],
                                           args=action['args'],
                                           method=action['method'],
                                           data=action['data'],
                                           endpoint=action['endpoint']))
        outputs.append(footer_tpl.render(section=''))
    outputs.append(exports_tpl.render(functions=functions))


    return '\r\n'.join(outputs)
