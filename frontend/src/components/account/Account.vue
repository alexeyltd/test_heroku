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
                    <md-tab id="tab-notification" md-label="Notification"
                            :md-template-data="{ badge: notifications_new.length }"
                            @click="change_state('notifications')"></md-tab>
                    <md-tab id="tab-sign_out" md-label="Sign out" @click="sigh_out"></md-tab>

                </md-tabs>
            </div>

            <div v-if="this.state==='settings'">
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
                                <span class="md-title">{{this.user.first_name}} {{this.user.last_name}}</span>
                            </md-toolbar>
                            <md-toolbar :md-elevation="1">
                                <span class="md-title">{{this.user.email}}</span>
                            </md-toolbar>
                        </md-card-content>
                    </md-card>
                </div>
                <div v-if="this.user.confirm_status===0">
                    <div class="md-layout md-alignment-top-center">
                        <md-card>
                            <md-card-header>
                                <md-card-header-text>
                                    <div class="md-title">Confirm code</div>
                                </md-card-header-text>
                            </md-card-header>
                            <md-card-content>
                                <md-field>
                                    <label>Input code here</label>
                                    <md-input v-model="code"></md-input>
                                    <md-button @click="confirm()">Submit</md-button>
                                </md-field>
                            </md-card-content>
                        </md-card>
                    </div>
                </div>
            </div>
            <div v-else>
                <div v-if="notifications_old.length===0 && notifications_new.length===0">
                    <div class="md-layout md-alignment-top-center">
                        <md-button class="md-raised" @click="get_notify()">Dont have notifications. Click for update.
                        </md-button>
                    </div>
                </div>
                <div v-for="i in notifications_new">
                    <div class="md-layout md-alignment-top-center">
                        <md-card>
                            <md-card-header>
                                <md-card-header-text>
                                    <i class="badge"></i>
                                    <div class="md-title">Actions left aligned</div>
                                    <div class="md-subhead">Subtitle here</div>
                                </md-card-header-text>
                                <md-button class="md-icon-button" md-menu-trigger @click="set_notify_old(i)">
                                    X
                                </md-button>
                            </md-card-header>
                            <md-card-content>
                                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio.
                                Dolores, sed accusantium quasi non, voluptas eius illo quas, saepe voluptate pariatur in
                                deleniti minus sint. Excepturi.
                            </md-card-content>
                        </md-card>
                    </div>
                </div>
                <div v-for="i in notifications_old">
                    <div class="md-layout md-alignment-top-center">
                        <md-card>
                            <md-card-header>
                                <md-card-header-text>
                                    <div class="md-title">GOT IT!</div>
                                    <div class="md-subhead">Subtitle here</div>
                                </md-card-header-text>
                                <md-button class="md-icon-button" md-menu-trigger @click="delete_notify(i)">
                                    X
                                </md-button>
                            </md-card-header>

                            <md-card-content>
                                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio.
                                Dolores, sed accusantium quasi non, voluptas eius illo quas, saepe voluptate pariatur in
                                deleniti minus sint. Excepturi.
                            </md-card-content>
                        </md-card>
                    </div>
                </div>
            </div>
        </md-app-content>
    </md-app>
</template>

<script>
    import Navbar from "../Navbar";
    import {mapState} from 'vuex';

    export default {
        name: "Account",
        components: {Navbar},
        data: () => ({
            state: 'settings',
            code: null,
            notifications_new: [],
            notifications_old: []
        }),
        methods: {
            change_state(state) {
                this.state = state;
            },
            sigh_out() {
                this.$store.commit('unset_user');
                this.$router.push('/login')
            },
            set_notify_old(id) {
                this.notifications_new.shift();
                this.notifications_old.unshift(1);
            },
            delete_notify(id) {
                this.notifications_old.shift();
            },
            confirm() {
                if (this.code) {
                    this.$api.post("/account/confirm", {
                        email: this.$store.state.user.email,
                        code: this.code
                    }).then((data) => {
                        if (data.data.result === 'success') {
                            this.user.confirm_status = 1;
                            this.$store.commit('set_user', {
                                user: this.user,
                                token: data.data.token
                            });
                            this.$snotify.info('Account confirmed!')

                        } else {
                            this.$snotify.error(data.data.msg)
                        }
                    }).catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                } else {
                    this.$snotify.warning('Fill all fields please')
                }
            },
            get_notify() {
                this.notifications_new.push(1);
            }
        },
        computed: mapState([
            'user', 'login'
        ]),
        created() {
            this.get_notify()
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