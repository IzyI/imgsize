<template>
    <v-content>
        <v-container
                fluid
                fill-height
                class="d-flex justify-center align-center"
        >
            <v-row
                    align="center"
                    justify="center"
            >
                <v-col
                        cols="12"
                        sm="12"
                        md="4"
                >
                    <v-card class="elevation-12">
                        <v-toolbar
                                color="primary"
                                class="font-weight-bold"
                        >
                            <v-spacer></v-spacer>
                            <v-toolbar-title font-weight-bold class="white--text">ВХОД</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-card-text>
                            <v-form>

                                <v-text-field
                                        label="Логин"
                                        name="name"
                                        prepend-icon="mdi-cellphone"
                                        type="text"
                                        v-model="name"
                                />

                                <v-text-field
                                        id="password"
                                        label="Пароль"
                                        name="password"
                                        prepend-icon="mdi-lock"
                                        type="password"
                                        v-model="password"
                                />


                            </v-form>
                        </v-card-text>

                        <v-card-actions>
                            <v-spacer/>
                            <v-btn color="primary" @click="authMe" :disabled="disabledauth">ОК</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-content>
</template>

<script>
    import myutils from "../myutils";
    export default {
        props: {},
        data() {
            return {
                name: this.$store.state.auth.name,
                password: "",
                disabledauth: false,
            }
        },
        computed: {},
        created() {
            if (this.$store.getters.isAuthenticated) {
                this.$router.push({name: 'ImgSize'})

            }
        },
        methods: {
            authMe: function () {

                let name = this.name;
                let password = this.password;
                this.disabledauth = true;
                var v = this;
                this.$store.dispatch('ac_login', {name, password}).then(function () {
                        v.disabledauth = false;
                    }
                ).catch(function (err) {
                    console.log(err)
                    myutils.notifError(v, err);
                }).finally(() => {
                    v.disabledauth = false;
                });
            }
        }
    }
</script>