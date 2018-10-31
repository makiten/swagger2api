import axios from 'axios'

const $http = axios.create({
    baseURL: '{{ proto }}://{{ base_path }}',
    timeout: 1000
})
