<template>
    <div>
        <div class="md-toolbar-row">
            <div class="md-toolbar-section-start">
                LOGO
            </div>
            <md-tabs class="md-primary" md-alignment="centered">
                <md-tab id="tab-products" md-label="Products" to="/products"></md-tab>
                <div v-if="login_status">
                    <md-tab id="tab-orders" md-label="My orders" to="/orders"></md-tab>
                    <md-tab id="tab-user" :md-label="user_now.first_name+' '+user_now.last_name" to="/account">
                    </md-tab>
                </div>
                <div v-else>
                    <md-tab id="tab-sign_in" md-label="Sign in" to="/login"></md-tab>
                </div>
                <md-tab id="tab-faq" md-label="FAQ" to="/faq"></md-tab>
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
        },
        data: () => ({
            login_status: null,
            user_now: null,
        }),
        methods: {
            sigh_out() {
                this.$store.commit('unset_user');
                this.$router.push('/login')
            }
        },
        created() {
            if (localStorage.getItem('login')) {
                this.$store.commit('set_user_from_localstorage');
                this.login_status = true;
                this.user_now = this.$store.state.user;
            } else {
                this.login_status = this.login;
                if (this.user === null) {
                    this.user = {
                        first_name: 'Empty',
                        last_name: 'Empty'
                    }
                } else {
                    this.user_now = this.$store.state.user;
                }
            }
        }
    }
</script>

<style scoped>

</style>