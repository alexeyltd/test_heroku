<template>
    <div>
        <form novalidate class="md-layout md-alignment-top-center">
            <md-card>
                <md-card-header>
                    <div class="md-title">
                        <md-tabs class="md-transparent" md-alignment="fixed">
                            <md-tab id="tab-home" md-label="Log In" @click="change_state('login')"></md-tab>
                            <md-tab id="tab-pages" md-label="Sign In"
                                    @click="change_state('registration')"></md-tab>
                        </md-tabs>
                    </div>
                    <div v-if="state==='login'">
                        <user-login></user-login>
                    </div>
                    <div v-else>
                        <user-create></user-create>
                    </div>
                </md-card-header>
            </md-card>
        </form>
    </div>
</template>

<script>
    import Navbar from "../Navbar";
    import userCreate from "./userCreate";
    import UserLogin from "./userLogin";

    export default {
        name: "Login",
        components: {UserLogin, Navbar, userCreate},
        data: () => ({
            state: null // login or registration
        }),
        methods: {
            change_state(new_state) {
                this.state = new_state;
            }
        },
        created() {
            this.state = 'login'
        }
    }
</script>

<style scoped>

</style>