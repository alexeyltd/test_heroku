<template>
    <md-app>
        <md-app-toolbar>
            <navbar :login="login" :user="user"></navbar>
        </md-app-toolbar>
        <md-app-content>
            <div class="md-layout md-alignment-top-center">
                <md-tabs>
                    <template slot="md-tab" slot-scope="{ tab }">
                        {{ tab.label }} <i class="badge" v-if="tab.data.badge">{{ tab.data.badge }}</i>
                    </template>
                    <md-tab id="tab-settings" md-label="Settings" @click="change_state('settings')"></md-tab>
                    <md-tab id="tab-notification" md-label="Notification" :md-template-data="{ badge: newPosts }"
                            @click="change_state('notifications')"></md-tab>
                    <md-tab id="tab-sign_out" md-label="Sign out" @click="sigh_out"></md-tab>

                </md-tabs>
            </div>

            <div v-if="state==='settings'">
                <div class="md-layout md-alignment-top-center">
                    <md-card>
                        <md-card-header>

                            <md-card-header-text>
                                <div class="md-title">Account</div>
                                <div class="md-subhead">User</div>
                            </md-card-header-text>
                            <md-card-media>
                                <img :src="require('@/assets/profile.png')" alt="People">
                            </md-card-media>
                        </md-card-header>
                        <md-card-content>
                            <md-toolbar :md-elevation="1">
                                <span class="md-title">{{user.first_name}} {{user.last_name}}</span>
                            </md-toolbar>
                            <md-toolbar :md-elevation="1">
                                <span class="md-title">{{user.email}}</span>
                            </md-toolbar>
                        </md-card-content>
                    </md-card>
                </div>
            </div>
            <div v-else>
                <div class="md-layout md-alignment-top-center">
                    <md-card>
                        <md-card-header>
                            <div class="md-title">Card without hover effect</div>
                        </md-card-header>

                        <md-card-content>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio.
                            Dolores, sed accusantium quasi non.
                        </md-card-content>
                    </md-card>
                    <md-card>
                        <md-card-header>
                            <div class="md-title">Card without hover effect</div>
                        </md-card-header>

                        <md-card-content>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio.
                            Dolores, sed accusantium quasi non.
                        </md-card-content>
                    </md-card>
                    <md-card>
                        <md-card-header>
                            <div class="md-title">Card without hover effect</div>
                        </md-card-header>

                        <md-card-content>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio.
                            Dolores, sed accusantium quasi non.
                        </md-card-content>
                    </md-card>
                </div>
            </div>
        </md-app-content>
    </md-app>
</template>

<script>
    import Navbar from "../Navbar";

    export default {
        name: "Account",
        components: {Navbar},
        data: () => ({
            login: false,
            user: null,
            state: 'settings',
            newPosts: 3
        }),
        methods: {
            change_state(state) {
                this.state = state;
            },
            sigh_out() {
                this.$store.commit('unset_user');
                this.$router.push('/login')
            }
        },
        created() {
            this.user = this.$store.state.user;
            this.login = this.$store.state.login;
        }
    }
</script>

<style scoped>
    .badge {
        width: 19px;
        height: 19px;
        display: flex;
        justify-content: center;
        align-items: center;
        position: absolute;
        top: 2px;
        right: 2px;
        background: red;
        border-radius: 100%;
        color: #fff;
        font-size: 10px;
        font-style: normal;
        font-weight: 600;
        letter-spacing: -.05em;
        font-family: 'Roboto Mono', monospace;
    }
</style>