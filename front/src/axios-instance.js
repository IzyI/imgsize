import axios from 'axios'

const VueAxios = axios.create({});
if (localStorage.getItem('access_token')) {
    VueAxios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('access_token')
} else {
    VueAxios.defaults.headers.common['Authorization'] = ''
}


VueAxios.setAuthAccess = function () {

    this.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('access_token')
};

VueAxios.setAuthRefresh = function () {
    this.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('refresh_token')
};



export default VueAxios