<template>
    <div>
        <md-card-content>
            <div class="md-layout md-gutter">
                <div class="md-layout-item md-small-size-100">
                    <md-field>
                        <label for="first-name">First Name</label>
                        <md-input name="first-name" id="first-name" autocomplete="given-name" v-model="first_name"
                        />
                    </md-field>
                </div>

                <div class="md-layout-item md-small-size-100">
                    <md-field>
                        <label for="last-name">Last Name</label>
                        <md-input name="last-name" id="last-name" autocomplete="family-name" v-model="last_name"
                        />
                    </md-field>
                </div>
            </div>

            <md-field>
                <label for="email">Email</label>
                <md-input type="email" name="email" id="email" autocomplete="email" v-model="email"
                />
            </md-field>
            <md-field>
                <label for="business_name">Business name* (optional)</label>
                <md-input name="business_name" id="business_name" v-model="business_name"
                />
            </md-field>
            <md-field>
                <label for="password">Password</label>
                <md-input type="password" name="password" id="password" autocomplete="password" v-model="password"
                />
            </md-field>
        </md-card-content>

        <md-card-actions>
            <div class="md-layout md-alignment-top-left">
                <!--todo visual fix-->
                <md-checkbox v-model="accept" class="md-primary">Accept privacy</md-checkbox>
            </div>
            <md-button type="button" class="md-primary" @click="create_user">Create account</md-button>
        </md-card-actions>
    </div>
</template>

<script>
    export default {
        name: "userCreate",
        data: () => ({
            first_name: null,
            last_name: null,
            email: null,
            business_name: null,
            password: null,
            accept: false
        }),
        methods: {
            create_user() {
                this.$store.commit('set_user', {
                    user: {first_name: this.first_name, last_name: this.last_name, email: this.email},
                    token: '1254s'
                });
                this.$router.push('/')
            }
        },
    }
</script>

<style scoped>

</style>