const notifError = function (v, err) {
    if(typeof  err =='string'){
         v.$notify({
                group: 'main', type: 'error',
                title: 'Error code: ' + 132,
                text:err
            });
         return
    }
    try {
        if (err["error-code"]) {
            v.$notify({
                group: 'main', type: 'error',
                title: 'Error code: ' + err["error-code"],
                text: err["error-message"]
            });
        } else if (err.response) {
            v.$notify({
                group: 'main', type: 'error',
                title: 'Error code: ' + err.response.status + "/" + err.response.data["error-code"],
                text: err.response.data["error-message"]
            });
        } else {
            if (err.response === undefined) {
                v.$notify({
                    group: 'main', type: 'error',
                    title: 'Error code: *',
                    text: "Что то пошло не так! "
                });
                console.log("Ошибка err.response - undefined")
            } else {
                try {
                    v.$notify({
                        group: 'main', type: 'error',
                        title: 'Error code: ' + err.response.status,
                        text: "Что то пошло не так! "
                    });
                } catch (e) {
                    v.$notify({
                        group: 'main', type: 'error',
                        title: 'Error code: *',
                        text: "Что то пошло не так! "
                    });
                    console.log("Ошибка js! : " + e)
                }
            }
        }
    } catch (e) {
        v.$notify({
            group: 'main', type: 'error',
            title: 'Error code: *',
            text: "Что то пошло не так: "+err.response
        });
        console.log("Ошибка js: " + e)
    }
};

const dataURLtoFile = (dataurl, filename) => {
    const arr = dataurl.split(',');
    const mime = arr[0].match(/:(.*?);/)[1];
    const bstr = atob(arr[1]);
    let n = bstr.length;
    const u8arr = new Uint8Array(n);
    while (n) {
        u8arr[n-1] = bstr.charCodeAt(n-1);
        n -= 1 // to make eslint happy
    }
    console.log(filename);
    return new File([u8arr], filename, {type: mime})
};

export default {notifError,dataURLtoFile}