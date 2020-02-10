<template>
  <div>products</div>
</template>

<script>

    export default {
        name: "Products",
        data: () => ({
            login: false,
            user: null
        }),
        methods: {},
        created() {
            this.user = this.$store.state.user;
            this.login = this.$store.state.login;
        }
    }
</script>

<style scoped>

</style>