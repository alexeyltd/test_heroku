<template>
    <md-app>
        <md-app-toolbar>
            <navbar :login="login" :user="user"></navbar>
        </md-app-toolbar>
        <md-app-content>
            {{this.user}}
        </md-app-content>
    </md-app>
</template>

<script>
    import Navbar from "../Navbar";

    export default {
        name: "Account",
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