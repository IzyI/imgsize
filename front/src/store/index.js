import Vue from 'vue'
import Vuex from 'vuex'
import auth from './auth'
import images from "./images";
Vue.use(Vuex);


export default new Vuex.Store({
    modules: {
        auth,
        images
    },
    state: {
    },
    getters: {
    },
    mutations: {

    },
    actions: {

    },

})
