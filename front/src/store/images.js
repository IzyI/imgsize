import $axios from '../axios-instance';
import myutils from "../myutils";


export default {
    state: {
        array_images: [],
        array_images_del_id: [],
        array_files: []

    },
    getters: {
        isArrayImages: state => state.array_images,
    },
    mutations: {
        mu_add_array_images(state, payload) {
            state.array_images.push(payload);
        },

        mu_set_array_files(state, payload) {
            state.array_files = payload;
        },

        mu_set_array_images(state, payload) {

            state.array_images = payload;
        },
        mu_del_slice_array_images(state, payload) {
            state.array_images.splice(payload, 1);
        },
        mu_replace_array_images(state, payload) {
            state.array_images[payload.id].file = payload.file;
        }
    },
    actions: {
        ac_add_array_images({commit}, payload) {
            commit("mu_add_array_images", payload);
        },
        ac_replace_array_images({commit}, payload) {
            commit("mu_replace_array_images", payload);
        },
        ac_set_array_images({commit}, payload) {
            commit("mu_set_array_images", payload);
        },
        ac_del_slice_array_images({commit}, payload) {
            commit("mu_del_slice_array_images", payload);
        },
        ac_allFiles({commit}) {
            return new Promise((resolve, reject) => {
                let url = '/user/' + this.state.auth.id_user + '/img';

                $axios.get(url).then(function (response) {
                    let d = response.data;
                    if (!d["error-code"]) {
                        commit("mu_set_array_files", d.data);
                        resolve(true);
                    } else {
                        reject(d);
                    }
                }, error => {
                    console.log("error ac_allFiles: " + error);
                    reject(error);
                });
            })
        },
        ac_delFiles({commit}) {
            return new Promise((resolve, reject) => {
                let url = '/user/' + this.state.auth.id_user + '/img';

                $axios.delete(url).then(function (response) {
                    let d = response.data;
                    if (!d["error-code"]) {
                        commit("mu_set_array_files",[]);
                        resolve(true);
                    } else {
                        reject(d);
                    }
                }, error => {
                    console.log("error ac_delFiles: " + error);
                    reject(error);
                });
            })
        },
        ac_ExportZIP() {
            return new Promise((resolve, reject) => {
                let url = '/user/' + this.state.auth.id_user + '/img/zip';
                $axios({
                    url: url,
                    method: 'GET',
                    responseType: 'blob',
                }).then(function (response) {
                    let d = response;
                    if (!d["error-code"]) {
                        resolve(d);
                    } else {
                        reject(d);
                    }
                }, error => {
                    console.log("error ac_ExportZIP: " + error);
                    reject(error);
                });
            })
        },
        ac_upload_array_images({commit}) {
            return new Promise((resolve, reject) => {
                var s = this.state;
                var pr = new Promise((resolve, reject) => {
                    uploadFile(0, resolve, reject, s, commit);
                });
                console.log("END ac_upload_array_images");
                pr.then(function () {
                    resolve(true);
                }).catch(function (err) {
                    reject(err);
                })


            });

        },
    }
}


function uploadFile(index, resolve, reject, state, commit) {
    if (index === state.images.array_images.length) {
        resolve(true);
        return
    }
    let file = state.images.array_images[index];
    let formData = new FormData();
    formData.append(
        'files' + index,
        myutils.dataURLtoFile(file.file, file.name),
    );
    $axios.post('/user/' + state.auth.id_user + '/img/upload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        },
    }).then(function (response) {
        let d = response.data;
        if (!d["error-code"]) {
            commit("mu_del_slice_array_images", index);
            uploadFile(index, resolve, reject, state, commit);
        } else {
            reject(d);
            return
        }
    }, error => {
        reject(error);
        console.log(error);
        return
    });
}








