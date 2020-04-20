<template>
    <div></div>
</template>
<script>

    export default {
        created() {
            this.$store.dispatch("ac_logout");
            this.$router.push({name: 'Login'})
        },
    }
</script>