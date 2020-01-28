<template>
    <div>
        <div v-if="$route.path!=='/admin'" class="md-toolbar-row">
            <div class="md-toolbar-section-start">
                LOGO
            </div>
            <md-tabs md-alignment="centered">
                <md-tab id="tab-products" md-label="Products" to="/products"></md-tab>
                <md-tab id="tab-faq" md-label="FAQ" to="/faq"></md-tab>

                <div v-if="$store.state.login===true">
                    <md-tab id="tab-orders" md-label="My orders" to="/orders"></md-tab>
                    <md-tab id="tab-user" :md-label="user.first_name+' '+user.last_name" to="/account">
                    </md-tab>
                </div>
            </md-tabs>
            <div v-if="$store.state.login===false">
                <md-button to="/login">Sign in</md-button>
            </div>
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