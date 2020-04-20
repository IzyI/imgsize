module.exports = {
    "transpileDependencies": [
        "vuetify"
    ]
    ,

    devServer: {
        proxy: {
            '^/user': {
                target: "http://127.0.0.1:5000",
                ws: true,
                changeOrigin: true
            },
            '^/auth': {
                target: "http://127.0.0.1:5000"
            },
            '^/upload': {
                target: "http://127.0.0.1:5000"
            }
        }

    }
};