<template>
    <div id="navigation">
        <notifications group="main" position="bottom right"/>
    </div>
</template>

<script>

    export default {
        name: 'Navigation',
        methods: {
            loggout: function () {
                this.$router.push({name: 'Logout'})
            },
            btn_panel_filter: function () {
                this.$store.dispatch("ac_panel_filter");
            }
        },
        data() {
            return {
                menu_item_user: [

                ],
            };
        },

        created() {
        },
        computed: {
            onMob: function () {
                return this.$vuetify.breakpoint.xsOnly
            },
            getPermission: function () {
                return this.$store.state.auth.permission === 'user.tsj'
            }
        },
    };
</script>

<style scoped lang="scss">
    #navigation{
        margin: 0;
        padding:0;
    }
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

    .mipa {
        padding-left: 3rem;
        transition: 0.5s;
    }

    .v-navigation-drawer--mini-variant {
        .mipa {
            padding-left: 1rem;
        }
    }

</style>