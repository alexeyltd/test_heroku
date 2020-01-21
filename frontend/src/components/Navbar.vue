<template>
    <div>
        <div class="md-toolbar-row">
            <md-tabs class="md-primary" md-alignment="centered">
                <div v-if="login">
                    <md-tab id="tab-orders" md-label="My orders" to="/orders"></md-tab>
                    <md-tab id="tab-user" :md-label="user.first_name+' '+user.last_name" to="/account">
                    </md-tab>
                    <!--<md-tab id="tab-sign_out" md-label="Sign out" @click="sigh_out"></md-tab>-->
                </div>
                <div v-else>
                    <md-tab id="tab-products" md-label="Products" to="/products"></md-tab>
                    <md-tab id="tab-faq" md-label="FAQ" to="/faq"></md-tab>
                    <md-tab id="tab-sign_in" md-label="Sign in" to="/login"></md-tab>
                </div>
            </md-tabs>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Navbar",
        props: {
            login: Boolean,
            user: {
                first_name: String,
                last_name: String,
                email: String
            }
        }, data: () => ({
            user: this.user,
            login: this.login
        }),
        methods: {
            sigh_out() {
                this.$store.commit('unset_user');
                this.$router.push('/login')
            }
        },
    }
</script>

<style scoped>

</style>