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
                <md-input type="password" name="password" id="password" autocomplete="password" v-model="password"
                />
            </md-field>
        </md-card-content>
        <!--todo accept privacy politics-->
        <md-card-actions class="md-layout md-alignment-top-center">
            <md-button type="button" class="md-primary" @click="login_user">Log In</md-button>
        </md-card-actions>
        <md-card-actions class="md-layout md-alignment-top-center">
            <md-button type="button" class="md-primary" @click="recovery_user">
                <small>Recovery account</small>
            </md-button>
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
            accept: null,
            password: null
        }),
        methods: {
            login_user() {
                if (this.email && this.password) {
                    this.$api.post("/account/login", {
                        email: this.email,
                        password: this.password
                    }).then((data) => {
                        if (data.data.result === 'success') {
                            this.$store.commit('set_user', {
                                user: data.data.user,
                                token: data.data.token
                            });
                            this.$router.push('/account')
                        } else {
                            this.$snotify.error(data.data.msg)
                        }
                    }).catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                } else {
                    this.$snotify.warning('Fill code please')
                }

            },
            recovery_user() {
                let result = prompt('Reset password?', 'type your email');
                this.$api.post("/account/recovery", {
                    email: this.email,
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.$snotify.info('We send new password on your email!')
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });


            }
        },
    }
</script>

<style scoped>

</style>