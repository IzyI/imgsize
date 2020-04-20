<template>

    <div class="main_admin">
        <navigation></navigation>
        <router-view></router-view>

    </div>

</template>


<script>
    import Navigation from './Navigation.vue'
    export default {
        name: 'Main',
        components: {
            Navigation,
        },
        data: () => ({}),
        methods: {},
        created() {


        },
    };
</script>

<style scoped>


</style>