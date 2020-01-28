<template>
  <div>products</div>
</template>

<script>
    import Navbar from "./Navbar";

    export default {
        name: "Products",
        components: {Navbar},
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