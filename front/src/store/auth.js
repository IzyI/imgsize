import $axios from '../axios-instance';
import router from "../router";


export default {
    state: {
        access_token: localStorage.getItem('access_token'),
        id_user: localStorage.getItem('id_user'),
        name: localStorage.getItem('name'),

    },
    getters: {
        isAuthenticated: state => !!state.access_token,
        getIdUsr: state => state.id_user,
    },
    mutations: {
        mu_set_auth(state, payload) {
            state.access_token = payload.meta.access_token;
            state.id_user = payload.data.id;
            state.name = payload.data.name;
            localStorage.setItem("access_token", state.access_token);
            localStorage.setItem("id_user", state.id_user);
            localStorage.setItem("name", state.name);

        }
    },
    actions: {
        ac_set_auth({commit}, payload) {
            commit("mu_set_auth", payload);
        },
        ac_logout({commit}) {
            commit("mu_set_auth", {meta: "", data: ""});
            localStorage.removeItem("access_token");
            localStorage.removeItem("id_user");
            localStorage.removeItem("name");
        },
        ac_login({commit}, payload) {
            return new Promise((resolve, reject) => {

                $axios.get('/auth', {
                    params: {
                        name: payload.name,
                        password: payload.password
                    }
                }).then(function (response) {
                    let d = response.data;
                    if (!d["error-code"]) {
                        commit("mu_set_auth", d);
                        $axios.setAuthAccess();
                        resolve(true);
                        router.push({name: 'ImgSize'})
                    } else {
                        reject(d);
                    }
                }, error => {
                    reject(error);
                });
            })
        },
    }
}
