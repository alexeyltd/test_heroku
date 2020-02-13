<template>
    <div>
        <div v-if="$route.path!=='/admin'" class="md-toolbar-row">
            <div class="md-toolbar-section-start">
                LOGO
            </div>
            <md-toolbar class="md-transparent" md-elevation="0">
                <!--<md-tabs class="md-primary" md-sync-route >-->
                <md-button id="tab-products" md-label="Home" to="/home" style="color: white">Home</md-button>
                <md-button id="tab-orders" md-label="My orders" to="/orders" style="color: white">My orders</md-button>
                <md-button id="tab-faq" md-label="FAQ" to="/faq" style="color: white">FAQ</md-button>

                <div  class="md-toolbar-section-end">
                    <div v-if="$store.state.login===true">
                        <md-button id="tab-user" to="/account" style="color: white">{{this.user.first_name}}
                            {{this.user.last_name}}
                        </md-button>
                    </div>
                    <!--</md-tabs>-->
                    <div v-if="$store.state.login===false">
                        <md-button to="/login" style="color: white">Sign in</md-button>
                    </div>
                </div>
            </md-toolbar>
        </div>
        <div v-else>
            <div class="md-title">
                ADMIN
            </div>
        </div>
    </div>
</template>

<script>
    import {mapState} from 'vuex';

    export default {
        name: "Navbar",
        data: () => ({}),
        methods: {},
        created: function () {
            if (localStorage.getItem('login')) {
                this.$store.commit('set_user_from_localstorage');
            }
        },
        computed: mapState([
            'user', 'login'
        ]),
    }
</script>

<style scoped>

</style>