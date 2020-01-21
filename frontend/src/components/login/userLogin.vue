<template>
    <div>
        <md-card-content>
            <md-field>
                <label for="email">Email</label>
                <md-input type="email" name="email" id="email" autocomplete="email" v-model="email"
                />
            </md-field>

            <md-field>
                <label for="password">Password</label>
                <md-input type="password" name="password" id="password" autocomplete="password"
                />
            </md-field>
        </md-card-content>
        <!--todo accept privacy politics-->
        <md-card-actions class="md-layout md-alignment-top-center">
            <md-button type="button" class="md-primary" @click="login_user">Log In</md-button>
        </md-card-actions>
        <md-card-actions class="md-layout md-alignment-top-center">
            <md-button type="button" class="md-primary" @click="recovery_user"><small>Recovery account</small></md-button>
        </md-card-actions>
    </div>
</template>

<script>
    export default {
        name: "userLogin",
        data: () => ({
            email: null,
            first_name: null,
            last_name: null,
            accept: null
        }),
        methods: {
            login_user() {
                this.$store.commit('set_user', {
                    user: {first_name: 'Artem', last_name: 'Shuvaev', email: this.email},
                    token: '1254s'
                });
                this.$router.push('/')
            },
            recovery_user() {
                this.$router.push('/recovery')
            }
        },
    }
</script>

<style scoped>

</style>