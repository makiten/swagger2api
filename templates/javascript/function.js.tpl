const {{ function }} = ({% if args|length > 0 %}{{ ', '.join(args) }}{% endif %}) => {
    {% if data and method in ['patch', 'post', 'put'] %}
    const data = {
    {% for k, v in data.items() %}
        {{ k }}: {{ v }}{% if not loop.last %},{% endif %}
    {% endfor %}
    }
    {% endif %}
    return $http.{{ method }}('{{ endpoint }}'{% if data %}, data{% endif %}{% if config %}, {{ config }}{% endif %})
        .then(r => {
            cb(r.data)
        })
        .catch(e => {
            cb(e)
        })
}
