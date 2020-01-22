<template>
    <div id="main">
        <md-app>
            <md-app-toolbar>
                <navbar :login="$store.state.login" :user="user"></navbar>
            </md-app-toolbar>
            <md-app-content>
                {{order}}
            </md-app-content>
        </md-app>
    </div>
</template>

<script>
    import Navbar from "../Navbar";

    export default {
        name: 'Order',
        components: {Navbar},
        data: () => ({
            user: null,
            order: null,
        }),
        methods: {
            get_order(){
                return {
                    id: this.$route.params.id,
                    name: 'name',
                    title: 'title',
                    status: 'status'
                }
            }
        },
        created() {
            this.user = this.$store.state.user;
            this.order = this.get_order()
        }
    }

</script>

<style>

</style>