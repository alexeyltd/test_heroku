<template>
    <div>
        <md-app>
            <md-app-toolbar class="md-primary md-small">
                <navbar></navbar>
            </md-app-toolbar>
            <md-app-content>
                <router-view></router-view>
                <Footer></Footer>
            </md-app-content>
        </md-app>
        <vue-snotify></vue-snotify>
    </div>
</template>

<script>
    import Navbar from "./components/Navbar";
    import Footer from "./components/Footer";

    export default {
        components: {Footer, Navbar}
    }
</script>

<style lang="scss">
    @import "~vue-snotify/styles/material.css";

    .md-app-content {
        min-height: 800px;
    }

</style>
