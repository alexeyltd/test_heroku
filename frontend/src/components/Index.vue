<template>
    <div id="main">
        <md-app>
            <md-app-toolbar>
                <navbar :login="$store.state.login" :user="user"></navbar>
            </md-app-toolbar>
            <md-app-content>
                main content
            </md-app-content>
        </md-app>
    </div>
</template>

<script>
    import Navbar from "./Navbar";

    export default {
        components: {Navbar},
        data: () => ({
            user: null
        }),
        methods: {},
        created: function () {
            if (!this.$store.state.login) {
                this.$router.push({path: 'login', props: true, login: false})
            } else {
                this.user = this.$store.state.user;
            }
        }
    }

</script>

<style>

</style>