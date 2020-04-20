<template>
    <v-content>
        <v-container
                 fill-height
                class="d-flex justify-center align-center"
        >
            <v-row
                    align="center"
                    justify="center"
            >
                <v-col
                        cols="12"
                        sm="8"
                        md="4"
                >


                    <v-card color="error">
                        <v-card-title class=" text-center">
                            <v-spacer></v-spacer>
                            <div>ERROR 404</div>
                            <v-spacer></v-spacer>
                        </v-card-title>
                        <v-card-text class="display-1  text-center">
                            Чего то ты не туда попал.<br> Страницы не существет.
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn @click.stop="goLogin" color="red darken-3">
                                Может вернемся в Начало начал
                            </v-btn>
                            <v-spacer></v-spacer>
                        </v-card-actions>
                    </v-card>

                </v-col>
            </v-row>
        </v-container>
    </v-content>
</template>

<script>
    import router from "../router";

    export default {
        props: {},
        methods: {
            goLogin() {
            router.push({name: 'Login'})
            }
        },
    }
</script>

