import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import axios from './axios-instance';
import Notifications from 'vue-notification'
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import VueCropper from 'vue-cropper'

Vue.use(VueCropper);

Vue.use(Notifications);
Vue.filter('timestampToDate', function (value) {
    var d = new Date();
    d.setTime(value * 1000);
    return ('0' + d.getHours()).slice(-2) + ':' + ('0' + d.getMinutes()).slice(-2);
});

Vue.filter('timesFormatted', function (value) {


    var sec = value;
    var min = Math.floor((sec / 60) % 60);
    var hour = Math.floor(((sec / 60) / 60) % 24);
    var day = Math.floor(((sec / 60) / 60) / 24);

    if (day !== 0) {
        day = 'Дней: ' + day + "<br>"
    } else {
        day = ""
    }

    if (hour !== 0) {
        hour = 'Часов: ' + hour + "<br>"
    } else {
        hour = ""
    }

    if (min !== 0) {
        min = 'Минут: ' + min
    } else {
        min = ""
    }
    var days = day + hour + min;
    return days;
});

Vue.directive('uppercase',
    {
        inserted: function (el, _, vnode) {
            el.addEventListener('input', async function (e) {
                e.target.value = e.target.value.toUpperCase()
                vnode.componentInstance.$emit('input', e.target.value.toUpperCase())
            })
        }
    });


Vue.config.productionTip = false;
Vue.prototype.axios = axios;
Vue.use(Loading);


new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app');
