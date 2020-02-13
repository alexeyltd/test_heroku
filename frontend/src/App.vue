<template>
    <div>
        <md-app>
            <md-app-toolbar class="md-primary md-small" style="background-color: #9a5ae4;">
                <div class="container">
                    <navbar></navbar>
                </div>
            </md-app-toolbar>
            <md-app-content>
                <router-view></router-view>
                <Footer></Footer>
            </md-app-content>
            <vue-snotify></vue-snotify>

        </md-app>
    </div>
</template>

<script>
    import Navbar from "./components/Navbar";
    import Footer from "./components/Footer";

    export default {
        components: {Footer, Navbar},
    }
</script>

<style lang="scss">
    @import "css/bootstrap.css";
    @import "css/style.css";
    @import "~vue-material/dist/theme/engine"; // Import the theme engine

    @include md-register-theme("default", (
            primary: #9a5ae4, // The primary color of your application
            accent: #9a5ae4 // The accent or secondary color
    ));
    @import "~vue-material/dist/theme/all"; // Apply the theme

    .md-app-content {
        min-height: 800px;
    }
</style>
