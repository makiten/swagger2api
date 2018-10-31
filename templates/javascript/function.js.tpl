const {{ function }} = ({% if args.length > 0 %}{{ ', '.join(args) }}{% endif %}) => {
    return $http.{{ method }}('{{ endpoint }}'{% if method in ['patch', 'post', 'put'] %}, {{ data }}{% endif %}{% if config %}, {{ config }}{% endif %})
        .then(r => {
            cb(r.data)
        })
        .catch(e => {
            cb(e)
        })
}
