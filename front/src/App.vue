<template>
    <v-app>
        <router-view></router-view>

        <notifications group="main" position="bottom right"/>
        <v-footer
                absolute
                height="30"
                width="100%"
                color="primary"
        >
                <div   class="text-center d-flex justify-end align-center w100 ">
                <span class="white--text caption">© Made whith love. Motherfucker. {{ new Date().getFullYear() }}</span>
                    </div>
        </v-footer>
    </v-app>
</template>

<script>

    import router from "./router";

    export default {
        name: 'App',
        components: {},
        data: () => ({}),
        methods: {
            goLogin() {
                router.push({name: 'Login'})
            }

        },
        created() {
        },
    };
</script>

<style lang="scss">
    .vue-notification {
        padding: 10px;
        margin: 0 5px 5px;

        font-size: 12px;

        color: #ffffff;
        background: #44A4FC;
        border-left: 5px solid #187FE7;

        &.warn {
            background: #ffb648;
            border-left-color: #f48a06;
        }

        &.error {
            background: #E54D42;
            border-left-color: #B82E24;
        }

        &.success {
            background: #68CD86;
            border-left-color: #42A85F;
        }
    }
        .w100{
            width: 100%;
        }

</style>