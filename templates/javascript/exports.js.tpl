export default {
{% for f in functions %}
   {{ f }}{% if not loop.last %},{% endfor %}
{% endfor %}
}
