<template>
    <div>
        faq
    </div>
</template>

<script>
    import Navbar from "./Navbar";

    export default {
        name: "Faq",
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