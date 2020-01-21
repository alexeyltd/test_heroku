<template>
    <md-app>
        <md-app-toolbar>
            <navbar :login="false" :user="null"></navbar>
        </md-app-toolbar>
        <md-app-content>
            recovery
        </md-app-content>
    </md-app>
</template>

<script>
    import Navbar from "../Navbar";

    export default {
        name: "userRecovery",
        components: {Navbar},
    }
</script>

<style scoped>

</style>