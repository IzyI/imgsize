<template>
    <v-content class="start_bg">
        <v-container
                fill-height
                class="d-flex justify-center align-center"

        >
            <v-row
                    align="center"
                    justify="center"
            >
                <pre>IMG Sizer</pre>
            </v-row>
        </v-container>
    </v-content>
</template>
<script>
    export default {
        props: {},
        methods: {  },
    }
</script>

<style scoped>


    .start_bg {
        color: #2a3537;
        font-size: 1.3rem;
        text-shadow: 1px 1px 2px #ffffff, 0 0 1em #5cbabc;
        background: url("../assets/bg1.jpg") no-repeat center center;
        background-size: cover;
        filter: blur(1px) ;
        overflow: hidden;
        margin-bottom: 0;
    }
</style>
