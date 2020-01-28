<template>
    <div>
        <md-app>
            <md-app-toolbar>
                <navbar></navbar>
            </md-app-toolbar>
            <md-app-content>
                <router-view></router-view>
            </md-app-content>
        </md-app>
        <vue-snotify></vue-snotify>
    </div>
</template>

<script>
    import Navbar from "./components/Navbar";

    export default {
        components: {Navbar}
    }
</script>

<style lang="scss">
    @import "~vue-snotify/styles/material.css";
</style>
